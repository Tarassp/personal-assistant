from run_address_book import run_address_book
from run_notebook import run_notebook

start_assistent = """\nWelcome to your personal assistant!
Personal assistant menu:
    1. NoteBook 
    2. AddressBook
    3. FolderCleaner
    4. Exit from personal assistant
Enter the section number from the personal assistant menu: \n"""


def main():
    while True:
        line = input(start_assistent)
        match line:
            case '1':
                run_notebook()
            case '2':
                run_address_book()
            case '3':
                print('RUN CLEANER')
            case '4':
                break
            case _:
                print('Wrong command')


main()
