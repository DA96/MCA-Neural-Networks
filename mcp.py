
'''

Aim: IMPLEMENT LOGIC GATES USING MCP MODEL IN NEURAL NETWORKS


Approach:

Weights are same for each input in MCP model and belong to set {1,0,-1}.
Weights and Threshold value for each logic gate is determined analytically.

Output value is determind by function:

        y = 1, if Sum(weight[i] * x[i]) >= t , for each i
          = 0, if Sum(weight[i] * x[i]) < t , for each i

        where,
        i is the number of inputs
        x[i] is the input value of ith input
        weight[i] is weight of ith input
        t is the threshold value of that gate

All input values x[i] belong to set {0,1}.
Output value y belong to set {0,1}.
t is an integer



Implementation:

Gates implemented: AND, OR, NOT, NAND, NOR
Number of inputs taken here are 2. (except for NOT GATE, which works on 1 input)


'''


'''
Author: DIVYA AGARWAL

Python version: 3.6.2

'''


input_values = [[0,0], [0,1], [1,0], [1,1]]

#values arranged in order of AND, OR, NOT, NAND, NOR
#weights = [[1,1], [1,1], -1, [-1,-1], [-1,-1]]
#threshold = [2, 1, 0, -1, 0]


def mcp_function(w, t, x, input_count):
	y = 0
	for i in range(input_count):
		y += w[i]*x[i]

	if y >= t:
		return 1
	else:
		return 0


def main():

	print("-------- MCP MODEL --------")

	print("\n---- AND GATE ----\n")
	print("  weights: 1,1	\n  threshold: 2  \n")
	print("			x1		x2		Output")
	for i in range(4):
		print("			",input_values[i][0],"		",input_values[i][1],"		",mcp_function([1,1], 2, input_values[i], 2))
	


	print("\n---- OR GATE ----\n")
	print("  weights: 1,1	\n  threshold: 1  \n")
	print("			x1		x2		Output")
	for i in range(4):
		print("			",input_values[i][0],"		",input_values[i][1],"		",mcp_function([1,1], 1, input_values[i], 2))



	print("\n---- NOT GATE ----\n")
	print("  weights: -1	\n  threshold: 0  \n")
	print("			x1		Output")
	inp = [0,1]
	for i in range(2):
		print("			",inp[i],"		",mcp_function([-1,], 0, [inp[i]], 1))



	print("\n---- NAND GATE ----\n")
	print("  weights: -1,-1	\n  threshold: -1  \n")
	print("			x1		x2		Output")
	for i in range(4):
		print("			",input_values[i][0],"		",input_values[i][1],"		",mcp_function([-1,-1], -1, input_values[i], 2))



	print("\n---- NOR GATE ----\n")
	print("  weights: -1,-1	\n  threshold: 0  \n")
	print("			x1		x2		Output")
	for i in range(4):
		print("			",input_values[i][0],"		",input_values[i][1],"		",mcp_function([-1,-1], 0, input_values[i], 2))



if __name__ == '__main__':
	main()


