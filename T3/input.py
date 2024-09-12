"""stores and parses the input string

"""
import time
from clock import Clock
from globals import TIMESTAMPS,NOTE_TYPES,MONTHS
class Input():
    def __init__(self) -> None:
        self.default_input = None
        self.string = ""
        self.list = []

    def update_list(self):
        self.list = self.string.split(" ")
 

    def  extract_note_time(self):
        """_summary_

        Args:
            input_list (list): _description_
        """
        time_stamp = None
        time_object = Clock.get_time_object() 
        for word in self.list:
            if len(word) >2:
                if word[0] == "@":
                    if word[1:] in TIMESTAMPS:
                        time_stamp =  Clock.generate_timestamp(word[1:])
                    elif word[1:] in MONTHS:
                        time_stamp =Clock.generate_timestamp(MONTHS[word[1:]])
                    else:
                        pass
                else:
                    pass
                if word[2] == ":" or word[2] == "/":

                    if word[:2].isdigit and word[3:].isdigit():
                        time_object = time.strptime(f"{int(word[:2])} {int(word[3:])} {time_object.tm_sec} {time_object.tm_mday} {time_object.tm_mon} {time_object.tm_year}", "%H %M %S %d %m %Y")
                        time_stamp = Clock.time_as_string(time_object=time_object)
                        

            return time_stamp
        
                
    def extract_note_type(self):
        """
        Returns:
            _word (str): type of note referenced in the string 
        """
        for _word in self.list:
            if _word in NOTE_TYPES:
                self.list.remove(_word)
                return _word
