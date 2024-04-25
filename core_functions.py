from main_database import shared_array
from main_database import modify_array
from file_reader_and_writer import update_csv , read_csv
def add_task(_user_input):
	a = {"timestamp":00,"type":"task","value":str(_user_input)}
	update_csv(a)
	return 0
def remove_task(_user_input):
	
	return 0

add_task(3)