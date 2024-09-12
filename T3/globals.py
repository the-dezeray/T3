from file_handler import get_config_data,load_json
NOTE_TYPES = ["task","entry","journal","project","sprint","bank","alarm"]
YAML_FILE_PATH  = "save.yaml"
TIMESTAMPS = ["today","tommorrow","yesterday","now","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

CONFIG = get_config_data()
json_file = load_json("config.json")
MONTHS = json_file['months']
SUGGESTIONS = json_file["suggestions"]
