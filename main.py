from address_book_app.address_book_client import AddressBookClient
from notebook_app.notebook_client import NotebookClient
import os


welcome_message = """\nWelcome to Personal Assistant Manager!
Menu:
    1. NoteBook 
    2. AddressBook
    3. FolderCleaner
    4. Exit from Personal Assistant Manager
Enter your option: """

def main():
    address_book_app = AddressBookClient()
    notebook_app = NotebookClient()
    os.system('cls||clear')
    while True:
        line = input(welcome_message)
        match line:
            case '1':
                os.system('cls||clear')
                notebook_app.run()
            case '2':
                os.system('cls||clear')
                address_book_app.run()
            case '3':
                os.system('cls||clear')
                print('RUN CLEANER')
            case '4':
                break
            case _:
                print('Wrong command')
                
main()