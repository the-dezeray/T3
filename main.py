
def get_user_input()->str:
    return input("Enter Command")

def main():
	user_input = get_user_input()
	from functions.parser import parse
	parse(user_input)
 

if __name__ =="__main__":
	main()