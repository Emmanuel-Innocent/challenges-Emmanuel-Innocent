/*
Author  : Emmanuel Innocent
Project : Round Robin Arbiter
Email   : sherlockhudep7@gmail.com
Licence : GNU GPL

*/

/*                                 DESCRIPTION:
This is the design of a simple Round Robin Arbiter, with four (4) request queues.
Since this is an FPGA based project, the time-quanta has been chosen
such that the human eye can observe the changes in the output lines(LED).
For this design 3 seconds was chosen. However, the time slice can easily
be adjusted by changing the value of the "THREE_SECS_FREQ" variable in the code.
The clock should be considered while changing the variable.

A 50MHz clock was used for this project.
*/


module round_robin_arbiter
#(parameter integer THREE_SECS_FREQ = 150000000)
(clk, reset, request_queue, grant_out);

input clk, reset;
input [3:0] request_queue;
output [3:0] grant_out;

  localparam [1:0]
               req_line_1 = 0,
               req_line_2 = 1,
               req_line_3 = 2,
               req_line_4 = 3;

  reg [1:0] current_state, next_state;
reg [3:0] token; // a one-hot ring counter output --- serves as a token
reg enable;
integer time_counter = 0;  //helps count 3 seconds

//State Memory
always @(posedge clk) begin
    if (reset) begin
        current_state <= req_line_1;
    end
    else if (enable == 1'b1)begin
        current_state <= next_state;
    end

end

//measure three (3) seconds
//the time quanta/slice is 3 seconds 
always @ (posedge clk) begin
    time_counter = time_counter + 1;
    if (time_counter == THREE_SECS_FREQ) begin
        enable = 1'b1;
        time_counter = 0;
    end
    else enable = 1'b0;
    
end

//Next State Logic
always @ (current_state, request_queue) begin
    case(current_state)
        req_line_1 : begin
                        token = 4'b0001;
                        next_state = req_line_2;
        end

        req_line_2 : begin
                        token = 4'b0010;
                        next_state = req_line_3;
        end

        req_line_3 : begin
                        token = 4'b0100;
                        next_state = req_line_4;
        end

        req_line_4 : begin
                        token = 4'b1000;
                        next_state = req_line_1;
        end

    endcase


end

//Output Logic
assign grant_out[3:0] = token[3:0] & request_queue[3:0];




endmodule //round_robin_arbiter
