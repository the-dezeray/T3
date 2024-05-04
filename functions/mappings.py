from functions.enums import Operation

OPERATION_MAPPINGS = {
    "add": Operation.ADD,
    "-a": Operation.ADD,
    "delete": Operation.REMOVE,
    "-d": Operation.REMOVE,
    "-v": Operation.VIEW,
    "view": Operation.VIEW,
}
