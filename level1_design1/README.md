# Multiplexer Design Verification
![Screenshot from 2022-07-30 11-44-34](https://user-images.githubusercontent.com/41594627/181907886-8d0b0b63-9384-43e4-8708-5a7792590389.png)

# Verification Strategy
The contrained random verification (CRV) strategy was used in the test of the multiplexer (MUX), the device under test (DUT). In this verification test, randomly generated stimulus was applied to the selector port of the MUX. This processed was looped for a fixed number of times, and for each cylce of the loop the output of the DUT was compared to the expected output(of the golden model). The diagram below describes how this process was carried out.

### Verification Environment
This test is a [CoCoTB](https://www.cocotb.org/) Python based test. With the rich Python libraries a randomised test (CRV) -- as descibed in the Verification srategy above -- was done.

Highlighted below were the step taken to capture the bug in the MUX design:
- After importing the relevant modules, thirty one (31) 2-bit numbers were randomly generated. This numbers were saved in a list and assign to bothe the input of the DUT and the golden model.
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
