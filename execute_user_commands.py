from note import Note


handlers = {
    "add": "add_handler",
    "edit": "edit_handler",
    "delet": "delet_handler",
    "search_text": "search_text_handler",
    "add_tags": "add_tags_hndler",
    "search_by_tags": "search_by_tag_handler",
    "sort": "sort_handler",
    "back": "back_handler",
}


class CliNotes:
    def __init__(self) -> None:
        self.notesbook = NoteBook()
        self.parser = Pars_Notes()

    def add_handler(self):
        while True:
            user_input_note = input("Enter note text: ")
            if not user_input_note.split():
                continue
            user_input_tags = input(
                "Enter tags for your note separated by commas: ")
            tags = [item.strip() for item in user_input_tags.split(",")]
            tags = None if tags == [""] else tags
            self.notesbook.add_note(user_input_note, tags)
            return "Note saved!", ""

    def edit_handler(self):
        search_notes_with_number = self.search_text_handler()
        print(search_notes_with_number[0])
        note_by_number = self.define_note_by_number(
            search_notes_with_number[1])
        while True:
            user_input_edittext = input(
                "Enter the text you want to add to the note:: ")
            if not user_input_edittext.split():
                continue
            break
        self.notesbook.edit(note_by_number, user_input_edittext)
        return "New text added to note!", ""

    def define_note_by_number(self, search_notes_with_number: list[tuple[int, Note]]) -> Note:
        while True:
            try:
                user_input_number = int(input(
                    "Enter the note number you want to edit: "))
                note_by_number = None
                for item in search_notes_with_number:
                    if item[0] == user_input_number:
                        note_by_number: Note = item[1]
                if note_by_number == None:
                    raise ValueError
            except ValueError:
                print("You have entered an invalid note number!")
            return note_by_number

    def delet_handler(self):
        search_notes_with_number = self.search_text_handler()
        print(search_notes_with_number[0])
        note_by_number = self.define_note_by_number(
            search_notes_with_number[1])
        self.notesbook.delete_note(note_by_number.text)
        return "Note removed!", ""

    def search_text_handler(self):
        while True:
            user_input_text = input(
                "Enter a piece of text to search for a note: ")
            if not user_input_text.split():
                continue
            search_notes: list[Note] = self.notesbook.search_notes(
                user_input_text)
            search_notes_with_number: list[tuple[int, Note]] = [
                (number, note) for number, note in enumerate(search_notes)]
            return ("\n".join(
                [f"Number: {item[0]}, Tags: {item[1].tags} \nNote: {item[1].text}\n" for item in search_notes_with_number])), search_notes_with_number

    def add_tags_hndler(self):
        search_notes_with_number = self.search_text_handler()
        print(search_notes_with_number[0])
        note_by_number = self.define_note_by_number(
            search_notes_with_number[1])
        while True:
            user_input_tags = input(
                "Enter tags for your note separated by commas: ")
            tags = [item.strip() for item in user_input_tags.split(",")]
            if tags == [""]:
                continue
            break
        self.notesbook.add_tags(note_by_number, tags)
        return "Added tags to the note!", ""

    def search_by_tag_handler(self):
        while True:
            user_input_tag = input(
                "Enter a tag to search for notes: ")
            if not user_input_tag.strip():
                continue
            tag = user_input_tag.strip()
            search_notes_by_tag: list[Note] = self.notesbook. search_notes_by_tags(
                tag)
            search_notes_with_number: list[tuple[int, Note]] = [
                (number, note) for number, note in enumerate(search_notes_by_tag)]
            return ("\n".join(
                [f"Number: {item[0]}, Tags: {item[1].tags} \nNote: {item[1].text}\n" for item in search_notes_with_number])), ""

    def sort_handler(self):
        sort_notes_tags: dict[str:[list[str]]
                              ] = self.notesbook.sort_notes_by_tags()
        result_sort = ""
        for tag, texts_notes in sort_notes_tags.items():
            result_sort += f"\nList of notes by tag '{tag}':\n" + "\n".join(
                texts_notes)
        return result_sort, ""

    def back_handler(self):
        return "Exit Notebook app!", ""

    def run_notes(self):
        while True:
            try:
                user_input_command = input(
                    """Enter the command for working with notes
                        (add/edit/delet/search_text/add_tags/search_by_tags/sort,
                        if you want to return to "personal-assistant" enter 'back',): """)
                command = self.parser.parser_comand(user_input_command)
                command_handler = handlers.get(command)
                command_response = getattr(self, command_handler)()
                print(command_response[0])
                if command_response[0] == "Exit Notebook app!":
                    break
            except ValueError:
                print("Сommand entered incorrectly!")
