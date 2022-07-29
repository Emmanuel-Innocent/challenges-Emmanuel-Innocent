# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    s2, s1, s0 = 0, 0, 0      #initialise the current state of the golden model to IDLE state
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    cycle = 0

    cocotb.log.info('#### CTB: Here is my verification test ######')
    number_of_cycles = 100
    while (cycle < number_of_cycles):
        dut._log.info(f'{cycle+1} cycle')
        seq_inp = random.randint(0,1)      #generate a 1-bit random number
        
        print("bit sequence:", seq_inp)
        dut.inp_bit.value = seq_inp       #feed in the generated number to the input of the DUT
        x = seq_inp                       #also assign the number to the input of the "golden" FSM model
        
        #the next state logic of the golden model:
        #given the current state and input
        #compute the next state of the golden model
        N2 = s1&s0&x
        N1 = (s0&~x) | (s1&~s0&x)
        N0 = (~s2&~s0&x) | (~s2&~s1&x) | (~s1&s0&x)

        #at positive edge of the clock assign the next state
        #to the current state of the golden model
        await RisingEdge(dut.clk)
        s2 = N2
        s1 = N1
        s0 = N0
        
        await Timer(2.5, units = "us")    #wait for the current state and output to become stable before reading their values
        print("current state of the device under test(DUT): ", dut.current_state.value)
        dut_current_state = dut.current_state.value
        print("current state of the golden model: ", s2, s1 , s0)
        print("\n")
        #the output logic of the golden model:
        output = (s2&~s0) | (s2&~s1)

        #check if the current state of the golden model and DUT are equivalent
        #and if their outputs are identical
        assert dut_current_state[2] == s0,   "the DUT and the golden model did not transition to equivalent state"
        assert dut_current_state[1] == s1,   "the DUT and the golden model did not transition to equivalent state"
        assert dut_current_state[0] == s2,   "the DUT and the golden model did not transition to equivalent state"
        assert dut.seq_seen.value == output, "incorrect output sequence"
        cycle = cycle + 1 
        await FallingEdge(dut.clk)

    


    

    
    


