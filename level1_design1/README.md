# Multiplexer Design Verification
![Screenshot from 2022-07-30 11-44-34](https://user-images.githubusercontent.com/41594627/181907886-8d0b0b63-9384-43e4-8708-5a7792590389.png)
                                                **fig.1 Screenshot showing my Gitpod id**



## Verification Strategy
The contrained random verification (CRV) strategy was used in the test of the multiplexer (MUX) which was the device under test (DUT). In this verification test, randomly generated stimulus was applied to the selector port of the MUX. This process was looped for a fixed number of times, and for each cycle of the loop the output of the DUT was compared to the expected output(of the golden model). The diagram below describes how this process was carried out.


![Untitled Diagram drawio(1)](https://user-images.githubusercontent.com/41594627/182087295-93d9480f-d239-4f8c-b094-16f05cdf8452.png)
                                                 **fig.2 A diagram showing the verification process**


### Verification Environment
This test is a [CoCoTB](https://www.cocotb.org/) Python based test. With the rich Python libraries a randomised test (CRV) -- as descibed in the overview above -- was done.

Highlighted below are the steps taken to capture the bug in the MUX design:
- After importing the relevant modules, thirty one (31) 2-bit numbers were randomly generated. These numbers were saved in a list and then assigned to the inputs of the DUT.


```
#Generate random 2-bit values for the 31 inputs of the Mux
#and store the values
inp_test = [random.randint(0, 3) for item in range(31)]

#assign these random 2-bit values to each input of the Mux
dut.inp0.value = inp_test[0]
dut.inp1.value = inp_test[1]
dut.inp2.value = inp_test[2]
dut.inp3.value = inp_test[3]
dut.inp4.value = inp_test[4]
dut.inp5.value = inp_test[5]
dut.inp6.value = inp_test[6]
dut.inp7.value = inp_test[7]
dut.inp8.value = inp_test[8]
dut.inp9.value = inp_test[9]
dut.inp10.value = inp_test[10]
dut.inp11.value = inp_test[11]
dut.inp12.value = inp_test[12]
dut.inp13.value = inp_test[13]
dut.inp14.value = inp_test[14]
dut.inp15.value = inp_test[15]
dut.inp16.value = inp_test[16]
dut.inp17.value = inp_test[17]
dut.inp18.value = inp_test[18]
dut.inp19.value = inp_test[19]
dut.inp20.value = inp_test[20]
dut.inp21.value = inp_test[21]
dut.inp22.value = inp_test[22]
dut.inp23.value = inp_test[23]
dut.inp24.value = inp_test[24]
dut.inp25.value = inp_test[25]
dut.inp26.value = inp_test[26]
dut.inp27.value = inp_test[27]
dut.inp28.value = inp_test[28]
dut.inp29.value = inp_test[29]
dut.inp30.value = inp_test[30]
```
- The behavioural descriprion of the golden model is: `mux_out = inp_test[Sel]` .
- A 5-bit number was randomly generated in a while loop and this 5-bit number was then assigned to the selector port of the DUT and the golden model. The while loop was constucted to run for at least 31 times. This is to carter for the case where the generator may generate all the possible thirty-two 5-bit numbers in an exhaustve but random manner, with the selector value with the buggy selection coming last in the iteration. The value '31' was not to be generated as it is a 31 input MUX(according to the design specification).
- For every cycle of the loop the output of the DUT and golden model were "asserted". To prevent the loop from halting prematurely when an assertion error is raised, error handling was employed, and a counter counts how many error is being encountered. Counter value of zero  means no error was raised and the test cases were passed. The test was ran more than once to capture bugs as many as possible.



```
count_failure = 0

for cycle in range(33):

    #Generate a 5-bit number for the selector of the Mux.
    #Value 31 will not be generated since it's a 31-input Mux 
    Sel = random.randint(0, 30)

    dut.sel.value = Sel  #assign to the selector of the DUT

    await Timer(2, units='ns')

    dut._log.info(f'selector={Sel}  sel_in_binary = {bin(Sel)[2:]} model={inp_test[Sel]}  DUT={int(dut.out.value)}')
    try:
        assert dut.out.value == inp_test[Sel]
    except:
        count_failure = count_failure + 1
        #print(count_failure)
        print("Test failed, DUT output value: ", dut.out.value, "not equal to", "expected output value: ",
        inp_test[Sel], "with selector value: ", Sel)
        print("\n")

    else:
        print("Test passed for this selector value")
        print("\n")



    """assert dut.out.value == inp_test[Sel], "Randomised test failed with: {output_DUT}  != {output_model}".format(
        output_DUT = int(dut.out.value), output_model= inp_test[Sel])"""
assert count_failure <= 0, "Test failed. Count_failure = {count_failure}".format(count_failure = count_failure)
```

## Test Scenario
1. For inp_test = [1, 3, 1, 1, 1, 3, 0, 3, 2, 2, 2, 1, 1, 3, 3, 2, 1, 3, 3, 3, 3, 1, 2, 3, 1, 0, 0, 1, 3, 1, 0]
- Test input(selector value): 01100
- Expected output: 01
- Observed output: 00
- Test input(selector value): 01101
- Expected output: 11
- Observed output: 01

2. For inp_test = [0, 2, 0, 1, 0, 2, 0, 1, 0, 3, 3, 0, 2, 1, 3, 3, 2, 0, 3, 0, 0, 0, 0, 0, 0, 2, 3, 3, 0, 0, 3]
- Test input(selector value): 01100
- Expected output: 10
- Observed output: 00
- Test input(selector value): 01101
- Expected output: 01
- Observed output: 10
- Test input(selector value): 11110
- Expected output: 11
- Observed output: 00

From the above results, there is mismatch when the selector value is either '01100' or '01101'. The mismatch for selector value '11110' is due to the obvious reason that value '11110' was set to default value '00' in the design. So it may not be taken as a bug as it may have been intended by the designer.

### Design Bug
On checking the assignment for selector values '1100 and '01101', it was discovered that:
- assignment for '01100' was omitted hence the default ouput value '00' was always observed for it
- assignment for '01101' was repeated twice (including where assignment for 01100 should have been). Hence the first wrong assignment will always be read for '01101'.

```
 5'b01001: out = inp9;  
 5'b01010: out = inp10;
 5'b01011: out = inp11;
 5'b01101: out = inp12;   // the bug
 5'b01101: out = inp13;   // the bug
 5'b01110: out = inp14;
 5'b01111: out = inp15;
 5'b10000: out = inp16;
 ```
## Design Fix
The design has been fix with the correct assignments. The fixed design is in the file "mux_fixed.v".


![Screenshot from 2022-08-01 11-12-49](https://user-images.githubusercontent.com/41594627/182134087-56ab608d-5746-4275-8b58-b470fa02fc1d.png)




## Is The Verification Complete?
Yes it is. The DUT was tested for all valid inputs(the selector and MUX input). However, with how the test was designed selector value "30 (11110)" may be seen as having a bug. This is because in the design, no unique value was assigned for selector value "30", it was assigned a default value '0'. But in the test module, in order to capture all the possible bugs, a random but constrained value was assign to all individual inputs. Therefore, while running the test, assertion error may be raised for selector value "30". But the default value for input "30" may have been intended by the designer.
