from typing import List
import re


class NoteBook():

    def __init__(self):
        self.data: List[Note] = []


    def __repr__(self) -> str:

        data = ""
        for number, note in enumerate(self.data):
            data += f"{number+1}) {note}\n" 
        return data

    
    def add_note(self, Note):

        if Note not in self.data:
            self.data.append(Note)
            return "Note was added successfully"

        else:
            return "Note is already exist!"


    def add_tag(self, part_of_note_text, new_tag):

        for note in self.data:

            if part_of_note_text in note.text:
                note.tags.append(new_tag)
                return f"Tag was added successfully!"
            else:
                return "Tag is already exist!"


    def delete_note(self, part_of_note_text):

        for note in self.data:

            if part_of_note_text in note.text:
                self.data.remove(note)
                return f"Note was deleted successfully!"

            else:
                return "Note is not exist!"    


    def delete_tag(self, tag):

        for note in self.data:
            if tag in note.tags:
                note.tags.remove(tag)
                return f"Tag {tag} was deleted successfully!"

            else:
                return "Tag is not exist!"


    def find_by_note_or_by_tag(self, part_of_text):

        result = []

        for note in self.data:
            if part_of_text in note.text or part_of_text in note.tags:
                result.append(note)

        if result == []:
            return "Nothing was found"

        else:
            return result


    def edit_note(self, old_text, new_text):

        for note in self.data:

            if old_text in note.text:
                sentences = note.text.split(old_text)
                note.text = new_text.join(sentences)
                print(f"{old_text} was switched with {new_text}")
                return ''
        return f"There's no {old_text} in notes"

    def sort_by_tags(self):   #???
        pass
