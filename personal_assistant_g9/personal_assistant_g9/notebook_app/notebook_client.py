from shared.cli_command import CLICommand
from shared.parser import CLIParser
from notebook_app.notebook_service import NotebookServide
from notebook_app.notebook import Notebook
from shared.local_storage import LocalStorage
from shared.client import Client


class NotebookClient(Client):
    def __init__(self) -> None:
        self.storage = LocalStorage("Notebook")
        self.notes = self.storage.load() or Notebook()
        self.service = NotebookServide(self.storage, self.notes)

    def run(self):
        welcome_message = "Welcome to NootBook App!\nEnter the command or type 'help' to see the list of commands: "
        hint = welcome_message
        reserved_command = CLICommand.NONE

        while True:
            line = input(hint)
            try:
                parser = CLIParser(line, reserved_command)
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
                    case CLICommand.EXIT:
                        break
                    case _:
                        reserved_command = CLICommand.NONE
                        hint = "Enter your command: "
            except Exception as e:
                print(e)
            # except:
            #     print("Type 'help' to see the commands.")
