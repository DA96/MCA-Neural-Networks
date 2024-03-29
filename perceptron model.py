
'''

Aim: IMPLEMENT LOGIC GATES USING PERCEPTRON MODEL IN NEURAL NETWORKS


Approach: Used Perceptron Learning Algorithm to learn weights for inputs to logic gates

Let w be weight vector, x be input vector
	such that 1st item in w is bias, therefore, 1st item in x is always 1

Output value is determind by function:

        y' = 1, if Sum(w[i] * x[i]) >= 0 , for each i
           = 0, if Sum(w[i] * x[i]) < 0 , for each i

        where,
        y' is the output calculated by the function in learning stage
        x[i] is the input value of ith input
        w[i] is weight of ith input
        
Let y be the actual output for a particular set of input values x

If y and y' are not same then we need to update weights
such that
	w[i] = w[i] + learning_rate * (y - y')*x[i]     ---- eq1

Here we have assumed learning_rate = 1.

Now, when weights are updated, we need to check whether the updated weights give the correct output for our input values
If yes, then check for next input values
If no, then update the weights again and then check for all input values

So we learn weights which satisfy all input combinations and give desired target output.

Note: It is already proved mathematically that eq1 will converge and will eventually give weights that will satisfy the condition for these logic gates



Implementation:

Gates implemented: AND, OR, NOT, NAND, NOR
Number of inputs taken here are 2 + 1(bias). (except for NOT GATE, which works on 1 input + bias)

Input values x[i] belong to set {0,1}.
Output value y and y' belong to set {0,1}.
weight w[i] is real number.


'''


'''
Author: DIVYA AGARWAL

Python version: 3.6.2

'''


input_values = [[0,0], [0,1], [1,0], [1,1]]
input_values_notgate = [0,1]

#corresponding target values 
target_values_AND = [0,0,0,1]
target_values_OR = [0,1,1,1]
target_values_NOT = [1,0]
target_values_XOR = [0,1,1,0]
target_values_NAND = [1,1,1,0]
target_values_NOR = [1,0,0,0]

learning_rate = 1


#perceptron learning algorithm
def learn(gate):

	if gate == "AND":
		target_gate = target_values_AND
	elif gate == "OR":
		target_gate = target_values_OR
	elif gate == "NOT":
		target_gate = target_values_NOT
	elif gate == "NAND":
		target_gate = target_values_NAND
	elif gate == "NOR":
		target_gate = target_values_NOR


	if gate != "NOT":
		input_num = 2
	else:
		input_num = 1

	weights = []
	#initializing weights, where 1st item is bias
	for j in range(input_num + 1):
		weights.append(1)

	#weights = [1, 1, 1]

	i = 0
	while i < 2**(input_num):

		#since 1st item is bias, input value for this is fixed as 1
		if gate != "NOT":
			x = [1, input_values[i][0], input_values[i][1]]
		else:
			x = [1, input_values_notgate[i]]
		
		
		sum = 0
		for j in range(input_num + 1):
			sum += weights[j] * x[j]

		if sum >= 0:
			output_calculated = 1
		else:
			output_calculated = 0


		if target_gate[i] != output_calculated:

			for j in range(input_num + 1):
				#updating weight of each input
				weights[j] += learning_rate*((target_gate[i] - output_calculated)*x[j])

			#testing updated weights for all input value combinations
			i = 0

		else:
			#if weights are good and give correct output then check for next input value combination, so increment i
			i += 1

	return weights



def calculate_output(w, x):
	#w is weght vector
	#x is input vector
	y = 0
	for j in range(len(w)):
		y += w[j]*x[j]

	if y >= 0:
		return 1
	else:
		return 0



def print_output(w, flag_notgate):

	if flag_notgate == 0:
		print("  bias: ",w[0], "\n  weight 1: ",w[1], "\n  weight 2: ",w[2], "\n")
		print("			x1		x2		Output")
		for i in range(4):
			x = [1, input_values[i][0], input_values[i][1]]
			print("			",input_values[i][0],"		",input_values[i][1],"		",calculate_output(w,x))
	
	else:
		print("  bias: ",w[0], "\n  weight 1: ",w[1], "\n")
		print("			x1		Output")
		for i in range(2):
			x = [1, input_values_notgate[i]]
			print("			",input_values_notgate[i],"		",calculate_output(w,x))




def main():

	print("------ PERCEPTRON MODEL ------")

	#w is weight vector received after learning weights for that logic gate

	print("\n---- AND GATE ----\n")
	w = learn("AND")
	print_output(w,0)

	print("\n---- OR GATE ----\n")
	w = learn("OR")
	print_output(w,0)

	print("\n---- NOT GATE ----\n")
	w = learn("NOT")
	print_output(w,1)

	print("\n---- NAND GATE ----\n")
	w = learn("NAND")
	print_output(w,0)

	print("\n---- NOR GATE ----\n")
	w = learn("NOR")
	print_output(w,0)



if __name__ == '__main__':
	main()

