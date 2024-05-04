from enum import Enum

class Operation(Enum):
    """Enumeration of operations."""

    ADD = 1
    SET = 3
    NONE = 0
    VIEW = 4
    REMOVE = -1


class Types(Enum):
    """Enumeration of types."""

    TASK = 1
    REMINDER = 2
    FUNCTIONAL = 3
    NONE = 0
    JOURNAL = 4


class Arguments(Enum):
    NONE = -1
