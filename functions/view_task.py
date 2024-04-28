
def view_task(stripped_input : list,index =0):
	from functions.file_reader_and_writer import  read_csv
	data_file = read_csv()
	task_rows = []
	for data_dict in data_file :
		if data_dict.get("type") == "task":
			task_rows.append(data_dict)
			
	for c in task_rows:
		print(str(c["value"]))