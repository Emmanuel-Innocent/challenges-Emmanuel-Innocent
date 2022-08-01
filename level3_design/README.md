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
- The "golden model" token value `token_tb` is computed with this function:
```
#this computes the ideal token value to be compared with the token value from the DUT
N3 = token_tb[1]&E | token_tb[0]&~E
N2 = token_tb[2]&E | token_tb[1]&~E
N1 = token_tb[3]&E | token_tb[2]&~E
N0 = token_tb[3]&~E | token_tb[0]&E
```

- The grant line of the golden model is then computed as the mask of the request line and the token:

```
#this computes the ideal token value to be compared with the token value from the DUT
N3 = token_tb[1]&E | token_tb[0]&~E
N2 = token_tb[2]&E | token_tb[1]&~E
N1 = token_tb[3]&E | token_tb[2]&~E
N0 = token_tb[3]&~E | token_tb[0]&E
await Timer(2.999, units = "sec")    #the time quanta
await RisingEdge(dut.clk)
token_tb[3], token_tb[2], token_tb[1], token_tb[0] = N0, N1, N2, N3
grant_out_tb = token_tb & request_queue_tb      #the token and request line are masked to give the grant output
```

- The grant output of the "golden model" and the DUT are then "asserted" to check for equivalence

`assert grant_out == grant_out_tb, "the observed grant request line does not match the expected grant output"`


## Is the Verification Complete?
The test was meant to only verify the functional behaviour of the simple round robin arbiter. No verification was done for timing analysis, etc.
