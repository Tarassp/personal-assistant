from execute_user_commands import CliNotes
from main import main

run_apps = {
    "1": "addressbook_run",
    "2": "notebook_run",
    "3": "foldcleaner_run",
}

start_assistent = """\nWelcome to your personal assistant!\n
Personal assistant menu:
    1. AddressBook
    2. NoteBook
    3. FoldCleaner\n
Enter the section number from the personal assistant menu:\n"""


class CLI:
    def __init__(self) -> None:
        self.notebook = CliNotes()

    def addressbook_run(self):
        print("Welcome to the AddressBook app!")
        main()

    def notebook_run(self):
        print("Welcome to the NoteBook app!")
        self.notebook.run()

    def foldcleaner_run(self):
        print("Welcome to the FoldCleaner app!")

    def run(self):
        while True:
            try:
                input_number_menu = input(start_assistent).strip()
                run_app_txt = run_apps.get(input_number_menu)
                getattr(self, run_app_txt)()
                break
            except TypeError:
                print("Wrong section number entered in personal assistant menu!")
