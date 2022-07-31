# Sequence Detector Verification

![Screenshot from 2022-07-30 11-44-34](https://user-images.githubusercontent.com/41594627/182002996-7ace628d-8bdd-4560-8181-6833fb666db4.png)

## Verification Strategy
For this test, the device under test (DUT) is a sequence detector which was implemented as a finite State Machine (FSM). The technique employed in this test was Equivalence Check. Equivalence check involves checking the property of the DUT against the property of the "golden model". The property of the golden model is usually abstracted as a boolean (or logic) or mathematical function.
According to theory, two FSMs (especially Moore Machines) represented as black boxes are equivalent if:
- for every finite input sequence, they produce identical output sequence
- in addition, for Mealy Machine, they must transition to equivalent states for the same finite input sequence.

The states of the "golden model" were encoded as a 3-bit states, then logic functions were derived for the next state transition and output.

### Verification Environment
This test is a [CoCoTb](https://www.cocotb.org/) Python based test.

- After imporing the relevant libraries, both the DUT were initialised to a known state (IDLE STATE)

```
# reset
  dut.reset.value = 1
  s2, s1, s0 = 0, 0, 0      #initialise the current state of the golden model to IDLE state
  await FallingEdge(dut.clk)  
  dut.reset.value = 0
  await FallingEdge(dut.clk)
```

-  A while loop was constructed to run for a long but finite time (say 100 times). This is because with many input sequence the bug will be easily captured.
-  
