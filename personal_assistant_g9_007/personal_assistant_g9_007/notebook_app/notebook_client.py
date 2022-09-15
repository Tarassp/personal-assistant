from personal_assistant_g9_007.notebook_app.notes_command import NotesCommand
from personal_assistant_g9_007.notebook_app.notes_parser import NotesParser
from personal_assistant_g9_007.notebook_app.notebook_service import NotebookServide
from personal_assistant_g9_007.notebook_app.notebook import Notebook
from personal_assistant_g9_007.shared.local_storage import LocalStorage

class NotebookClient:
    def __init__(self) -> None:
        self.storage = LocalStorage('Notebook')
        self.notes = self.storage.load() or Notebook()
        self.service = NotebookServide(self.storage, self.notes)
        
    def run(self):
        welcome_message = "Welcome to NootBook App!\nEnter the command or type 'help' to see the list of commands: "
        hint = welcome_message
        reserved_command = NotesCommand.NONE
        
        while True:
            line = input(hint)
            try:
                parser = NotesParser(line, reserved_command)
                command = parser.get_command()
                value = parser.get_value()
                
                status = self.service.handle(command, value)
                
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
        