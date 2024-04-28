
def add_task(_user_input=[],index=0):
	from Functions.file_reader_and_writer import update_csv , read_csv
	a = {"timestamp":00,"type":"task","value":' '.join(_user_input[index:])}
	print(' '.join(_user_input[index:]))
	update_csv(a)
	return 0