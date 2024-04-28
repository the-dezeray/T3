import sys
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)

from Functions import flag_add,add_task,remove_task,view_task
# Now that all modules are imported, you can use them as needed


array =[

{"function":flag_add.adds,"flags":['-a',"23"]},
{"function":add_task.add_task,"flags":['-at',"task","add"]},
{"function":remove_task,"flags":['-r',"remove"]},
{"function":view_task,"flags":['view',"-v"]},
]

def find_function(value,) :
    global array
    
    for item in array:
        if 'flags' in item and isinstance(item['flags'], list):
            if value in item['flags']:
                return item["function"]
    print("noething was found")
    return False  # Value not found
