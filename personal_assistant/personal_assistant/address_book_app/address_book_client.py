from personal_assistant.address_book_app.address_book import AddressBook
from personal_assistant.address_book_app.address_book_parser import AddressBookParser
from personal_assistant.address_book_app.address_book_command import AddressBookCommand
from personal_assistant.address_book_app.address_book_service import AddressBookService
from personal_assistant.shared.local_storage import LocalStorage


class AddressBookClient:
    
    def __init__(self) -> None:
        self.storage = LocalStorage('address_book.bin')
        self.adress_book = self.storage.load() or AddressBook()
        self.service = AddressBookService(self.storage, self.adress_book)
        
    def run(self):
        welcome_message = "\nWelcome to Address Book App!\nEnter the command or type 'help' to see the list of commands: "
        hint = welcome_message
        reserved_command = AddressBookCommand.NONE
        
        while True:
            line = input(hint)
            try:
                parser = AddressBookParser(line, reserved_command)
                command = parser.get_command()
                value = parser.get_value()
                
                status = self.service.handle(command, value)
                
                if status.response:
                    print(status.response)
                    
                if status.request:
                    hint = status.request.message
                    reserved_command = status.request.command
                    continue
                
                if command == AddressBookCommand.EXIT:
                    break
            except Exception as e:
                print(e)
            
            reserved_command = AddressBookCommand.NONE
            hint = "Enter your command: "