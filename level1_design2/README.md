# Sequence Detector Verification

![Screenshot from 2022-07-30 11-44-34](https://user-images.githubusercontent.com/41594627/182002996-7ace628d-8bdd-4560-8181-6833fb666db4.png)

# Verification Strategy
For this test, the device under test (DUT) is a sequence detected which is basically a finite State Machine (FSM). The technique employed in this test was Equivalence Check. Equivalence check involves checking the property of the DUT against the property of the golden model. The property of the golden model is usually abstracted as a boolean (or logic) function.
According to theory, two FSMs (especially Moore Machines) represented as black boxes are equivalent if:
- for every finite input sequence, they produce identical output sequence
- in addition, for mealy machine, they must transition to equivalent states for the same finite input sequence.
