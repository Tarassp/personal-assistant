
class Pars_Notes:
    def __init__(self, text):
        self.text = text
        self.parse()

    def parse(self):
        self.command = self.text.split()[0]
        self.text = self.text[len(self.command):]

    def add(self):
        print(self.text)

    def edit(self): 
        print(self.text)

    def delete_note(self):
        print(self.text)

    def add_tags(self):
        print(self.text)

    def search_notes(self):
        print(self.text)

    def search_notes_by_tags(self):
        print(self.text)

    def sort_notes_by_tags(self):
        print(self.text)

    def run(self):
        if self.command == 'add':
            self.add()
        elif self.command == 'edit':
            self.edit()
        elif self.command == 'delete':
            self.delete_note()
        elif self.command == 'add_tags':
            self.add_tags()
        elif self.command == 'search_notes':
            self.search_notes()
        elif self.command == 'search_notes_by_tags':
            self.search_notes_by_tags()
        elif self.command == 'sort_notes_by_tags':
            self.sort_notes_by_tags()
        else:
            print('Unknown command')
