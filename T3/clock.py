"""Handles all time related functions and events in the code 
the global timeformat  : "%B %d %Y %h %H:%M:%S")

"""

from globals import TIMESTAMPS ,MONTHS
import time
class Clock:
    @classmethod
    def current_time(cls):
        time_object  = time.localtime()
        return cls.time_as_string(time_object=time_object)


    @staticmethod
    def get_time_object():
        return time.localtime()
    @classmethod
    def time_as_string(cls,time_object : time.struct_time):
        return  time.strftime("%H:%M:%S %d %B %Y",time_object)

    @staticmethod
    def is_in_weeks(day):
        weeks = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        return day in weeks
        
    @classmethod
    def generate_timestamp(cls,tag:str):
        """_summary_

        Args:
            tag (str): _description_

        Returns:
            _type_: _description_
        """

        time_object = time.localtime()
        timestamp :str =  None
        
        weeks = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
        if tag in weeks:
            day =None

            a = None
            mon = 0
            a = weeks.index(tag)
            if time_object.tm_wday > a:
               day = time_object.tm_mday +   abs( time_object.tm_wday -a)
            elif time_object.tm_wday < a:
               day =  time_object.tm_mday +   abs(time_object.tm_wday - a)
            elif time_object.tm_wday ==  a:
                day = time_object.tm_mday
        
            if day >30:

                if time_object.tm_mon in [4,6,9,11]:
                    mon =1
                    day -= 29
                elif day > 31:
                    mon = 1
                    day -= 30
                if time_object.tm_mon+mon >11:
                    mon = -11
            if day is not None:
                time_object = time.strptime(f"{time_object.tm_hour} {time_object.tm_min} {time_object.tm_sec} {day} {time_object.tm_mon+mon} {time_object.tm_year }", "%H %M %S %d %m %Y")
                timestamp = cls.time_as_string(time_object)

        else:
            match tag:
                case "now":
                    timestamp = cls.time_as_string(time_object)
                case "tommorrow":
                    
                    time_object = time.strptime(f"{time_object.tm_hour} {time_object.tm_min} {time_object.tm_sec} {time_object.tm_mday + 1} {time_object.tm_mon} {time_object.tm_year}", "%H %M %S %d %m %Y")
                    timestamp = cls.time_as_string(time_object)
                case "yesterday":
                    
                    time_object = time.strptime(f"{time_object.tm_hour} {time_object.tm_min} {time_object.tm_sec} {time_object.tm_mday - 1} {time_object.tm_mon} {time_object.tm_year}", "%H %M %S %d %m %Y")
                    timestamp =cls.time_as_string(time_object)
                case "today":
                    timestamp =cls.time_as_string(time_object)
                case _:
                    pass
        return timestamp  
        
   
    def extract_note_parent(cls):
        return 0
    def extract_note_deadline(cls):
        return 0
