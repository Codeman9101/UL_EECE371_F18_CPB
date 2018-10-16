module Assignment_3
(
	input [7:0] a,
	input [7:0] b,
	input clk, aclr, clka, c,
	output reg [15:0] out
);

	reg  [15:0] a_reg, b_reg;
	reg  c_reg;
	reg	 [15:0] old;
	wire [15:0] multa;
	
	assign multa = a_reg * b_reg;
	
	always @ (out, c_reg)
	begin
		if (c_reg)
			old <= 0;
		else
			old <= out;
	end
	
	always @ (posedge clk or posedge aclr)
	begin
		if (aclr)
		begin
			a_reg <= 0;
			b_reg <= 0;
			c_reg <= 0;
			out <= 0;
		end
		
		else if (clka)
		begin
			a_reg <= a;
			b_reg <= b;
			c_reg <= c;
			out <= old + multa;
		end
	end
endmodule
