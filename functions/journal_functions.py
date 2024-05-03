from functions.enums import Operation, Types


def remove_text(text: str, text_to_remove: str) -> str:

    index = text.find(text_to_remove)
    if index!= -1:
        text = text[:index] + text[index + len(text_to_remove):]
        print(f"functions worked result: {text}")
    return text


def gen():
    return 0


def delete_task(a):
    return 0


def set_task(a):
    return 0


def add_task(input_object):
    from functions.file_reader_and_writer import update_csv

    timestamp = gen()
    b = "dadafs fadfa task a"
    print(f"the value of the input_object.string is {input_object.string}")
    value = remove_text(input_object.string,"task")
    value = remove_text(value, "add")
    value = value.strip()
    _type = input_object.type
    _dict = {"timestamp": timestamp, "type": _type, "value": value}
    update_csv(_dict)
    print("Hello World")

def remove_task(input_object):
    from functions.file_reader_and_writer import  read_csv,new_csv
    data = read_csv()
    removed = data.pop()
    new_csv(data)


    
def user_input_handler(input_object):
    print("input_object.type")
    match input_object.operation:
        case (  Operation.NONE, Operation.ADD ) :
            print("operation.add")
            add_task(input_object)
        case Operation.REMOVE:
            remove_task(input_object)

if __name__ == "__main__":
    print("Executing in main")
