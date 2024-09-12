"""handles and executes user inputs"""
from input import Input
import time
from rich.text import Text
from file_handler import append_yaml_file,get_yaml_data
from note import Note
from rich.panel import Panel
from globals import TIMESTAMPS,NOTE_TYPES,SUGGESTIONS
from rich.layout import Layout
from rich.padding import Padding
from rich.table import Table


       
class Core():
    """backend section"""
    def __init__(self,layout:Layout) -> None:
        self.cursor = ""
        """Initialization of the backend
            A layout instance must be provided to interact with
        Args:
            layout (Layout): a return variable of the make_layout function
        """
        self.cursor_visible = True
        self.last_blink_time = time.time()
        self.cursor_visible = False
        self.last_blink_time = 0
        self.input = Input()
        self.layout = layout
        self.formated_text  =" "
        self.suggestion = ""
        self.running = True
        self.table = None
        self.PRIMARY_KEY_WORD_MAPPING ={
        "show":self.show,
        "del":self.delete,
        "delete":self.delete,
        "add":self.create,
        "display":self.show,
        "+":self.create,
        "-":self.delete,
        
        }


    def save_key(self,key):
        """An argument for the keyboard Listerner
        Args:
            key (_type_): instance from the keyboard Listerner
        """
        
        _key :str= str(key)
        _key= _key.replace("'","")
        match _key:

            case "Key.space":
                _key = " "

            case "Key.backspace":
                _key = ""
                self.input.string =  self.input.string[:-1]

            case "Key.enter":
                self.input.update_list()

                self.process(user_input=self.input.string,layout=self.layout)
                self.input.string = ""
                self.formated_text = ""
                self.edit_suggestion()
            case _:
                pass

        if len(_key) <2:
            
            self.input.string += _key
            self.input.update_list()
            self.format_text()
            self.edit_suggestion()

    def contains_primary_key(self):
        
        for i in self.input.list:
            if i in self.PRIMARY_KEY_WORD_MAPPING:
                return True
        return False
    
    def edit_suggestion(self):
        """_summary_
        """
        if len(self.input.string )< 2:
            self.suggestion = ""
        if  not self.contains_primary_key():
    
            matching_words = [word for word in self.PRIMARY_KEY_WORD_MAPPING if word.startswith(self.input.list[-1])]
            if matching_words:
        
                if matching_words[0] in SUGGESTIONS:
                    self.suggestion = SUGGESTIONS[matching_words[0]]

    def format_text(self):
        """_summary_
        """
     
        for index ,i in enumerate(self.input.list):
            if i in self.PRIMARY_KEY_WORD_MAPPING:
                self.input.list[index] = "[orange_red1]"  + i.lower() + "[/orange_red1]"
                
            if i in NOTE_TYPES:
                self.input.list[index] = "[orange_red1] "  + i + " [/orange_red1]"
                
        self.formated_text = " ".join(self.input.list)


    def process(self,layout : Layout = None ,user_input:str= ""):

        if type(user_input) == str :
            self.input.list = user_input.split(" ")
            self.input.string = user_input
        for word in (self.input.list[:2]):
            if  word in self.PRIMARY_KEY_WORD_MAPPING:
                function : callable = self.PRIMARY_KEY_WORD_MAPPING[word]
                self.input.list.remove(word)

                function()

    def create(self ):
        """_summary_
        """
        note_type = self.input.extract_note_type()
        note_content = " ".join(self.input.list)
        note_deadline = self.input.extract_note_time()
        print(f"this is the dealine{note_deadline}")
   
        note_id =len(get_yaml_data()) 
        note = Note(type=note_type,content=note_content,deadline = note_deadline,id = note_id)

        
        append_yaml_file(note)

    def show(self):

        #time_scale = self.input.eextract_note_deadline()
        note_type = self.input.extract_note_type()   
        notes:list = get_yaml_data()
        notes  = [note for note in notes if note["type"] == note_type]
        self.table =  Table(expand=True,show_edge=False)
        self.table.add_column()
        self.layout["view"].update(Padding(self.table,pad =(0,40),expand=True))
        self.table.add_row(Text("@today",justify="left"))

        for i in  range(-8,-2):
            text =  notes[i]["content"]
            self.table.add_row(Panel(text))
        self.layout["view"].update(Padding(self.table,pad =(0,40),expand=True))

    def delete(self):
        """_summary_

        Args:
            user_input (list): _description_
        """
        pass
    
    def update_cursor(self):
        
        current_time = time.time()
        if current_time - self.last_blink_time >= 0.5:  # Blink every 0.5 seconds
            if self.cursor_visible:
                if self.formated_text == "":
                    pass 
                elif self.formated_text[-1] == "|":
                    self.formated_text = self.formated_text[:-1]
                self.cursor_visible = False
            else:
                self.formated_text += "|"
                self.cursor_visible = True
            self.last_blink_time = current_time


