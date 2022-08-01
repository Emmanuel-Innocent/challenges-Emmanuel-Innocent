# Verification of the behaviour of a Simple Round Robin Arbiter

![Screenshot from 2022-07-30 11-44-34](https://user-images.githubusercontent.com/41594627/182002996-7ace628d-8bdd-4560-8181-6833fb666db4.png)

**Fig.1 A screenshot showing my Gitpod id**

## Verification Strategy
The technique used in this test is the equivalence check. Equivalence check involves checking the property of the DUT against the property of the "golden model". The property of the golden model is usually abstracted as a boolean (or logic) or mathematical function. Only the behavioural functionality was verified  in this test.

### Verification Environment
This test is a [CoCoTb](https://www.cocotb.org/) Python based test.
- A random 4-bit number representing the four request line was generated. This number was thenn assigned to the request port of the DUT and the golden model

```
request_queue_tb = random.randint(0,15)       #a 4-bit number is generated for the four request lines
dut.request_queue.value = request_queue_tb    #assign the number to the request line of the DUT
```
