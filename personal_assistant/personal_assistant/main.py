from personal_assistant.address_book_app.address_book_client import AddressBookClient
from personal_assistant.notebook_app.notebook_client import NotebookClient
from personal_assistant.cleaner.cleaner_client import CleanerClient
import os


welcome_message = """Welcome to Personal Assistant Manager!
Menu:
    1. NoteBook 
    2. AddressBook
    3. FolderCleaner
    4. Exit from Personal Assistant Manager
Enter your option: """

def main():
    address_book_app = AddressBookClient()
    notebook_app = NotebookClient()
    cleaner_app = CleanerClient()
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
                cleaner_app.run()
            case '4' | 'exit':
                os.system('cls||clear')
                break
            case _:
                print('Wrong command')
                
if __name__ == '__main__':
  main()