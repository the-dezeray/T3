from dataclasses import dataclass

import re

from functions.mappings import OPERATION_MAPPINGS
from functions.enums import Operation ,Types,Arguments


def find_in_map(user_input: str, MAP):
    words = re.findall(r"\w+", user_input)
    for word in words:
        if word.lower() in MAP:
            
            return MAP[word.lower()]
    return None


@dataclass
class UserInput:
    

    operation: Operation = Operation.NONE
    type: Types = Types.NONE
    string: str = ""
    value: str = None
    arguments: Arguments = Arguments.NONE
    timestamp: float = 0.0

    def get_operation(self):

        return Operation.ADD

    def get_types(self):
        # Add your logic to get the type from the user
        return Types.TASKS

    def get_arguments(self):
        return Arguments.NONE

    def get_index(self):

        return 0

    def generate_timestamp(self):
        return 0

    def get_value(self):
        return self.string
    def __post_init__(self):
        self.operation = find_in_map(self.string, OPERATION_MAPPINGS)
        self.type = find_in_map(self.string, Types)
        self.arguments = self.get_arguments()
        self.index = self.get_index()
        self.timestamp = self.generate_timestamp()
        self.value = self.get_value()
