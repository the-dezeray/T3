from core_functions import *


class  Function_map():
	def __init__(self):
		self.array = []
		self.secondary_flags =[]
	def find_function(self,value) :
	    for item in self.array:
	        if 'flags' in item and isinstance(item['flags'], list):
	            if value in item['flags']:
	                return item["function"]
	    return False  # Value not found



function_map = Function_map()

function_map.array =[
{"function":add,"flags":['-a',"add"]},
{"function":add_task,"flags":['-at',"addtask","task"]},
{"function":remove_task,"flags":['-r',"remove"]},
{"function":view_task,"flags":['view',"-v"]},
]
