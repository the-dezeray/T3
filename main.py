 from functions_and_key_bindings import key_function_array
#core function

def add_task():
	print("task added")
	return 0
def  remove_task():
	return 0



def search_array(array, value):
    for item in array:
        if 'other_words_used' in item and isinstance(item['other_words_used'], list):
            if value in item['other_words_used']:
                return item["function"]
    return False  # Value not found

def run_user_input(input):
	input = input.strip()

	input_array = input.split()
	funtion_from_array = search_array(key_to_function_array,input_array[0])
	funtion_from_array()

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