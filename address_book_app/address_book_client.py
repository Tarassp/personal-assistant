from address_book_app.address_book import AddressBook
from address_book_app.address_book_parser import AddressBookParser
from address_book_app.address_book_command import AddressBookCommand
from address_book_app.address_book_service import AddressBookService
from shared.local_storage import LocalStorage


class AddressBookClient:
    
    def __init__(self) -> None:
        self.storage = LocalStorage('AddressBook')
        self.adress_book = AddressBook()
        self.service = AddressBookService(self.storage, self.adress_book)
        
    def run(self):
        while True:
            line = input("Enter your command: ")
            try:
                parser = AddressBookParser(line)
                command = parser.get_command()
                value = parser.get_value()
                message = self.service.handle(command, value)
                
                if message:
                    print(message)

                if command is AddressBookCommand.EXIT:
                    break
            except:
                print("Type 'help' to see the commands.")