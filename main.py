
def get_user_input()->str:
    return input("Enter Command")

def main():
	user_input = get_user_input()
	from functions.user_input_parser import InputParser
	parsed_input = InputParser(string = user_input)
	from functions.handler import CommandHandler
	handler_instance = CommandHandler()
	handler_instance.handle(input_object= parsed_input)

 

if __name__ =="__main__":
	main()