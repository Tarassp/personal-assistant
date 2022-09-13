from address_book_app.address_book_client import AddressBookClient
from notebook_app.notebook_client import NotebookClient

welcome_message = """\nWelcome to your personal assistant!
Personal assistant menu:
    1. NoteBook 
    2. AddressBook
    3. FolderCleaner
    4. Exit from personal assistant
Enter the section number from the personal assistant menu: \n"""

def main():
    address_book_app = AddressBookClient()
    address_book_app.run()
    # notebook_app = NotebookClient()
    # while True:
    #     line = input(welcome_message)
    #     match line:
    #         case '1':
    #             notebook_app.run()
    #         case '2':
    #             address_book_app.run()
    #         case '3':
    #             print('RUN CLEANER')
    #         case '4':
    #             break
    #         case _:
    #             print('Wrong command')
                
main()