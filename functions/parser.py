from functions.enums import Operation, Types


class InputObject:
    def __init__(self):
        self.type = Types.NONE
        self.operation = Operation.NONE
        self.string = ""

    def set_type_task(self):
        self.type = Types.TASK
        print("set type to task")

    def set_operation_add(self):
        self.operation = Operation.ADD

    def set_type_reminder(self):
        self.type = Types.REMINDER

    def set_type_journal(self):
        self.type = Types.JOURNAL

    def set_operation_remove(self):
        self.operation = Operation.REMOVE

    def set_type_functional(self):
        self.type = Types.FUNCTIONAL

    def set_operation_view(self):
        self.operation = Operation.VIEW


input_object = InputObject()


array = [
    {"function": input_object.set_operation_add, "arguments": ["add", "-a"]},
    {"function": None, "arguments": ["set", "-s"]},
    {"function": input_object.set_operation_remove, "arguments": ["delete", "-d"]},
    {"function": None, "arguments": ["to"]},
    {"function": input_object.set_type_task, "arguments": ["task", "-t"]},
    {"function": input_object.set_type_reminder, "arguments": ["reminder"]},
    {"function": None, "arguments": ["event", "-e"]},
    {"function": input_object.set_operation_view, "arguments": ["view", "-v"]},
    {"function": input_object.set_type_journal, "arguments": ["journal", "-j"]},
]


def get_function(text):
    for item in array:
        arguments = item["arguments"]
        if text in arguments:
            print(text)
            return item["function"]
    return None


def parse(text: str):
    text = text.strip()
    split_text = text.split()
    input_object.string = text
    for i, element in enumerate(split_text):

        func = get_function(element)
        if func != None:
            print("run")
            func()

    match input_object.type:
        case Types.TASK:
            from functions.task_functions import user_input_handler

            user_input_handler(input_object)

        case Types.REMINDER:
            from functions.reminder_functions import user_input_handler

            user_input_handler(input_object)

        case Types.JOURNAL:
            from functions.journal_functions import user_input_handler

            user_input_handler(input_object)
        case Types.NONE:
            pass
