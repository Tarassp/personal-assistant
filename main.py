from address_book import AddressBook
from assistant_parser import AssistantParser
from assistant_command import AssistantCommand
from address_book_service import AddressBookService
from local_storage import LocalStorage

def main():
    message = ''
    storage = LocalStorage()
    adress_book = AddressBook()
    assistant = AddressBookService(storage, adress_book)
    while True:
        line = input("Enter your command: ")
        try:
            parser = AssistantParser(line)
            command = parser.get_command()
            value = parser.get_value()
            message = assistant.handle(command, value)
            
            if message:
                print(message)

            if command is AssistantCommand.EXIT:
                break
        except:
            print("Type 'help' to see the commands.")
main()