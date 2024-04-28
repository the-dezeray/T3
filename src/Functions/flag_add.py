def adds(stripped_input : list,index = 0):
	from  Functions import flag_register
	print("run")
	_function = flag_register.find_function(stripped_input[index])
	if len(stripped_input)>=index+1:
		print(stripped_input[index])
		_function(stripped_input,index+1)
