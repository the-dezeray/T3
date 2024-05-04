
def get_user_input()->str:
    return input("Enter Command")

def main():
	user_input = get_user_input()
	from functions.user_input import UserInput
	input_object = UserInput(string = user_input)
	from functions.handler import Handler
	handler = Handler()
	handler.handle(input_object= input_object)

 

if __name__ =="__main__":
	main()