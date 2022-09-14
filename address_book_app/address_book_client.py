from address_book_app.address_book import AddressBook
from address_book_app.address_book_parser import AddressBookParser
from address_book_app.address_book_command import AddressBookCommand
from address_book_app.address_book_service import AddressBookService
from shared.local_storage import LocalStorage


class AddressBookClient:
    welcome_message = """\nWelcome to Address Book App!
Enter the command or type 'help' to see the list of commands: """
    
    def __init__(self) -> None:
        self.storage = LocalStorage('AddressBook')
        self.adress_book = AddressBook()
        self.service = AddressBookService(self.storage, self.adress_book)
        
    def run(self):
        hint = AddressBookClient.welcome_message
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