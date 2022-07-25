# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for the buggy mux mux2"""

    cocotb.log.info('##### CTB Challenge: Here is my test ########')
    
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
    

    #out_test = [inp_test[index] for index in range(32)]
    print("This is the list of the 31 randomly generated 2-bit mux input: ", inp_test)

    #This loop should be repeated for at least 31 times
    #reason: (1) assuming the worst-case scenario where the bug is due to only
    #one selector value. Numbers may be generated for each of the selector
    #values such that the selector value with the bug may be generated
    #at the last iteration. (2) with short iteration,
    #the selector value with the bug may never be generated,
    #so iteration should be longer to increase the chance of capturing the bug

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

