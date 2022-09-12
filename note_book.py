from typing import List
from collections import deque
from note import Note


class NoteBook():


    def __init__(self):
        self.data: List[Note] = []


    def __repr__(self) -> str:

        data = ""
        for number, note in enumerate(self.data):
            data += f"{number+1}) {note.text} : {note.tags}\n" 
        return data
        
    
    def add_note(self, user_input_note, tags):              
        self.note = Note(user_input_note,tags)
        if self.note not in self.data:
            self.data.append(self.note)
            return self.data

        else:
            return "Note is already exist!"


    def add_tags(self, note_by_number, tags):    
        note_ind = self.data.index(note_by_number)
        note = self.data[note_ind]
        return note.tags.extend(tags)


    def search_notes(self, user_input_text):     

        result = []

        for note in self.data:
            if user_input_text in note.text:
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


    def delete_note(self, note_by_number):      
        return self.data.remove(note_by_number)


    def edit(self, note_by_number: Note, user_input_edittext:str):  
        note_ind = self.data.index(note_by_number)
        note = self.data[note_ind]
        note.text += " " + user_input_edittext
        return self.data


    def sort_notes_by_tags(self):  
        sorted_dict = {}
        for note in self.data:
            
            for tag in note.tags:

                if tag not in sorted_dict.keys():
                    sorted_dict[tag]=[note.text]
            
                else:
                    sorted_dict.get(tag).append(note.text)
        
        return sorted_dict 
