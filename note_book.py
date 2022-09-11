from typing import List
from collections import deque


# functions: add_note, find_by_note, find_by_tag, add_tag, 
#            remove_tag, remove_note, edit_note, sort_by_tags

class NoteBook():

    def __init__(self):
        self.data: List[Note] = []


    def __repr__(self) -> str:

        data = ""
        for number, note in enumerate(self.data):
            data += f"{number+1}) {note}\n" 
        return data

    def choose_num_of_note(self, notes_with_text: List[Note]) -> str:
        notes_for_choose = ""
        count = 1
        for note in notes_with_text:
            one_note = f"{count}) {note}\n"
            notes_for_choose += one_note 
            count+=1

        return notes_for_choose
        
    
    def add(self, Note):

        if Note not in self.data:
            self.data.append(Note)
            return "Note was added successfully"

        else:
            return "Note is already exist!"


    def add_tag(self, new_tag):

        a = self.__repr__()
        print(a)
        num_of_note = int(input("Enter number of note you want add a tag to:"))
        note = self.data[num_of_note-1]
        if new_tag not in note.tags:
            note.tags.append(new_tag)
            return f'Tag {new_tag} was added successfully!'
        else:
            return "Tag is already exist!"


    def search_notes(self, text_of_note):

        result = []

        for note in self.data:
            if text_of_note in note.text:
                result.append(note)

        if result == []:
            return "No notes were found"

        else:
            return result


    def search_notes_by_tags(self, tag):
        result = []
        for note in self.data:
            if tag in note.tags:
                result.append(note)

        if result == []:
            return "No tags were found"

        else:
            return result


    def delete_tag(self, removing_tag):
        notes_with_tag = self.find_by_tag(removing_tag)

        if notes_with_tag=='No tags were found':
            return 'No tags were found'
        
        if len(notes_with_tag)==1:
            notes_with_tag[0].tags.remove(removing_tag)
            return f"Tag {removing_tag} was removed successfully"

        a = self.choose_num_of_note(notes_with_tag)
        print(a)

        num_of_note = int(input("Enter number of note you want remove a tag from:"))
        note = self.data[num_of_note-1]
        note.tags.remove(removing_tag)
        return f"Tag {removing_tag} was removed successfully"


    def delete_note(self, text_of_note):
        notes_with_text = self.find_by_note(text_of_note)

        if notes_with_text == "No notes were found":
            return f'No notes with {text_of_note} were found'

        if len(notes_with_text)==1:
            self.data.remove(notes_with_text[0])
            return f"Note was removed successfully!"

        a = self.choose_num_of_note(notes_with_text)
        print(a)

        num_of_note = int(input("Enter number of note you want remove:"))
        note = self.data[num_of_note-1]
        self.data.remove(note)
        return f"Note was removed successfully"
        

    def edit(self, old_text, new_text):
        notes_with_text = self.find_by_note(old_text)

        if notes_with_text == "No notes were found":
            return f'No notes with {old_text} were found'

        if len(notes_with_text)==1:
            sentences = notes_with_text[0].text.split(old_text)
            notes_with_text[0].text = new_text.join(sentences)
            print(f"{old_text} was switched with {new_text}")
            return ''

        a = self.choose_num_of_note(notes_with_text)
        print(a)
        
        num_of_note = int(input("Enter number of note you want change:"))
        note = self.data[num_of_note-1]
        sentences = note.text.split(old_text)
        note.text = new_text.join(sentences)
        print(f"{old_text} was switched with {new_text}")
        return ''


    def sort_notes_by_tags(self, tag):  
        new_self_data = deque()
        for note in self.data:
            if tag in note.tags:
                new_self_data.appendleft(note)
            else:
                new_self_data.append(note)
        self.data = list(new_self_data)
        return self.data