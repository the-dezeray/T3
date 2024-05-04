from dataclasses import dataclass
from functions.enums import Operation , Types
@dataclass
class CommandHandler:


    def add(self,input_object):
        from functions.file_reader_and_writer import update_csv

        _entry = {
            "timestamp": input_object.timestamp,
            "type": input_object.type,
            "value": input_object.value,
            "time": input_object.value,
        }
        update_csv(_entry)
    def update(self,input_object):
        return 0   
    
    def view(self,input_object):
        type = input_object.type
        from functions.file_reader_and_writer import read_csv

        data_file = read_csv()
        task_rows = []
        for data_dict in data_file:
            if eval(data_dict.get("type")) == type:
                task_rows.append(data_dict)

        for c in task_rows:
            print(str(c["value"]))
        return task_rows
    
    def remove(self,input_object):
        from functions.file_reader_and_writer import read_csv, new_csv

        data = read_csv()
        removed = data.pop()
        new_csv(data)
    def handle(self,input_object):

        match input_object.operation:
            case Operation.ADD  :

                self.add(input_object)
            case Operation.REMOVE:
                self.remove(input_object)
            case Operation.VIEW:
                from functions.view_functions import view
                array = view(Types.TASK)
            case Operation.NONE:
                self.add(input_object)

    