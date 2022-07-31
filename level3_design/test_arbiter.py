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

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    s2, s1, s0 = 0, 0, 0      #initialise the current state of the golden model to IDLE state
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    #cycle = 0

    cocotb.log.info('#### CTB: Here is my verification test ######')
