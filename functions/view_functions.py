def view_task(stripped_input: list, index=0):
    from functions.file_reader_and_writer import read_csv

    data_file = read_csv()
    task_rows = []
    for data_dict in data_file:
        if data_dict.get("type") == "task":
            task_rows.append(data_dict)

    for c in task_rows:
        print(str(c["value"]))
from functions.enums import Types

def view(type =Types.NONE )->list:
    print("view function")
    from functions.file_reader_and_writer import read_csv

    data_file = read_csv()
    task_rows = []
    for data_dict in data_file:
        if eval(data_dict.get("type")) == type:
            task_rows.append(data_dict)

    for c in task_rows:
        print(str(c["value"]))
    return task_rows