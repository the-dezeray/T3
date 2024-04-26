from  key_to_function_map import function_map
#core function





def run_user_input(inputs):
	inputs = inputs.strip()

	split_input = inputs.split()

	funtion_from_array = function_map.find_function(split_input[0])
	if len(split_input) >0 :	
			funtion_from_array(split_input)

	return 0




# main function
def main():

	

	#storage array
	array = [] 

	#get user_input
	user_input  = input("type command: ")

	#run user input
	run_user_input(user_input)



#run program
main()