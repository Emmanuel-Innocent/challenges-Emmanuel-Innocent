# Multiplexer Design Verification
![Screenshot from 2022-07-30 11-44-34](https://user-images.githubusercontent.com/41594627/181907886-8d0b0b63-9384-43e4-8708-5a7792590389.png)

# Verification Strategy
The contrained random verification (CRV) strategy was used in the test of the multiplexer (MUX), the device under test (DUT). In this verification test, randomly generated stimulus was applied to the selector port of the MUX. This processed was looped for a fixed number of times, and for each cylce of the loop the output of the DUT was compared to the expected output(of the golden model). The diagram below describes how this process was carried out.

### Verification Environment
This test is a [CoCoTB] (https://www.cocotb.org/) Python based test. With the rich Python library a randomised test (CRV) -- as descibed in the Verification srategy above -- was done.
