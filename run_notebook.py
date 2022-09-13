import math
from notes_command import NotesCommand
from notes_parser import NotesParser
from notebook_service import NotebookServide
from notebook import Notebook
from local_storage import LocalStorage

def run_notebook():
    storage = LocalStorage('Notebook')
    notes = Notebook()
    service = NotebookServide(storage, notes)
    hint = "Enter your command: "
    reserved_command = NotesCommand.NONE
    
    while True:
        line = input(hint)
        try:
            parser = NotesParser(line, reserved_command)
            command = parser.get_command()
            value = parser.get_value()
            
            status = service.handle(command, value)
            
            if status.response:
                print(status.response)
                
            if status.request:
                hint = status.request.message
                reserved_command = status.request.command
                continue
            
            match command:
                case NotesCommand.EXIT:
                    break
                case _:
                    reserved_command = NotesCommand.NONE
                    hint = "Enter your command: "
        except Exception as e:
            print(e)
        # except:
        #     print("Type 'help' to see the commands.")