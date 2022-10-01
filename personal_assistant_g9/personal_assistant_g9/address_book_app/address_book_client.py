from address_book_app.address_book import AddressBook
from shared.parser import CLIParser
from shared.cli_command import CLICommand
from address_book_app.address_book_service import AddressBookService
from shared.local_storage import LocalStorage
from shared.client import Client


class AddressBookClient(Client):
    def __init__(self) -> None:
        self.storage = LocalStorage("address_book.bin")
        self.adress_book = self.storage.load() or AddressBook()
        self.service = AddressBookService(self.storage, self.adress_book)

    def run(self):
        welcome_message = "Welcome to Address Book App!\nEnter the command or type 'help' to see the list of commands: "
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

                if command == CLICommand.EXIT:
                    break
            except Exception as e:
                print(e)

            reserved_command = CLICommand.NONE
            hint = "Enter your command: "
