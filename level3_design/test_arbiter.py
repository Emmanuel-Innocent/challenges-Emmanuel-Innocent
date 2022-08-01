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
    """Test for round robin arbiter """

    # Create a 10ns period clock on port clk:
    #this arbiter was design for a 50MHz clock
    #so a period of 20ns is needed
    clock = Clock(dut.clk, 20, units="ns")  
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    token_tb = 0b0001
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    cycle = 0

    cocotb.log.info('#### CTB: Here is my verification test ######')
    
    while (cycle < 5):
        request_queue_tb = random.randint(0,15)       #a 4-bit number is generated for the four request lines
        dut.request_queue.value = request_queue_tb    #assign the number to the request line of the DUT
        E = 0b1   #enable line
        
        #this computes the ideal token value to be compared with the token value from the DUT
        N3 = token_tb[1]&E | token_tb[0]&~E
        N2 = token_tb[2]&E | token_tb[1]&~E
        N1 = token_tb[3]&E | token_tb[2]&~E
        N0 = token_tb[3]&~E | token_tb[0]&E
        await Timer(2.999, units = "sec")    #the time quanta
        await RisingEdge(dut.clk)
        token_tb[3], token_tb[2], token_tb[1], token_tb[0] = N0, N1, N2, N3
        grant_out_tb = token_tb & request_queue_tb      #the token and request line are masked to give the grant output
        await(5, units = "ns")
        
        assert grant_out == grant_out_tb, "the observed grant request line does not match the expected grant output"
        
        cycle = cycle + 1
        
