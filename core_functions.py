
from file_reader_and_writer import update_csv , read_csv

def add_task(_user_input=[],index=0):

	a = {"timestamp":00,"type":"task","value":' '.join(_user_input[index:])}
	print(' '.join(_user_input[index:]))
	update_csv(a)
	return 0
def remove_task(_user_input=[],index =0):
	
	return 0
def add(stripped_input : list,index = 0):
	from  key_to_function_map import function_map
	print("run")
	_function = function_map.find_function(stripped_input[index])
	if len(stripped_input)>=index+1:
		print(stripped_input[index])
		_function(stripped_input,index+1)

def view_task(stripped_input : list,index =0):
	data_file = read_csv()
	task_rows = []
	for data_dict in data_file :
		if data_dict.get("type") == "task":
			task_rows.append(data_dict)
			
	for c in task_rows:
		print(str(c["value"]))