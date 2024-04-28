from functions.enums import Operation, Types

class InputObject:
    def __init__(self):
        self.type = Types.TASK
        self.operation = Operation.ADD

input_object = InputObject()

def set_type_task():
    input_object.type = Types.TASK


def set_operation_add():
    input_object.operation = Operation.ADD

def set_operation_remove():
    input_object.operation = Operation.REMOVE

array = [
    {"function": set_operation_add, "arguments": ["add", "-a"]},
    {"function": None, "arguments": ["set", "-s"]},
    {"function": set_operation_remove, "arguments": ["delete", "-d"]},
    {"function": None, "arguments": ["@", "at"]},
    {"function": None, "arguments": ["to"]},
    {"function": set_type_task, "arguments": ["task", "-t"]},
    {"function": None, "arguments": ["reminder"]},
    {"function": None, "arguments": ["event", "-e"]},
    {"function": None, "arguments": ["journal", "-j"]},
]


def get_function(element):
    return next((row["function"] for row in array if "add" in row["arguments"]), None)


def parse(text:str):
    text = text.strip()
    split_text = text.split()

    for i, element in enumerate(split_text):
        func = get_function(split_text)
        if func != None:
            func()

    match input_object.type:
        case Types.TASK:
            from functions.task_functions import user_input_handler
            user_input_handler(input_object)
        case Types.REMINDER:
            pass
        case Types.JOURNAL:
            pass
        case Types.FUNCTIONAL:
            pass
        case Types.NONE:
            pass
