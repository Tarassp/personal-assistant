class NoteComand:
    ADD = ["add", "додати"]
    EDIT = ["edit", "редрагувати"]
    DELETE = ["delete", "видалити"]
    ASSIGNTAGS = ["assign tags", "додайте теги"]
    SEARCHNOTES = ["searchnotes", "пошук нотаток"]
    SEARCHNOTESBYTAGS = ["search notes by tags", "пошук нотатки за тегом"]
    SORTNOTESBYTAGS = ["sort notes by tags", "сортувати нотатки за тегами"]
    UNKNOWN = ["unknown", "невідомо"]

    def __init__(self, command):
        self.command = command

    def __str__(self):
        return f"{self.command}"

class NoteComandParser:
    def __init__(self, comand: str):
        self.comand = comand
        self.comand = self.comand.lower()

    def parse(self) -> NoteComand:
        if self.comand in NoteComand.ADD:
            return NoteComand.ADD
        elif self.comand in NoteComand.EDIT:
            return NoteComand.EDIT
        elif self.comand in NoteComand.DELETE:
            return NoteComand.DELETE
        elif self.comand in NoteComand.ASSIGNTAGS:
            return NoteComand.ASSIGNTAGS
        elif self.comand in NoteComand.SEARCHNOTES:
            return NoteComand.SEARCHNOTES
        elif self.comand in NoteComand.SEARCHNOTESBYTAGS:
            return NoteComand.SEARCHNOTESBYTAGS
        elif self.comand in NoteComand.SORTNOTESBYTAGS:
            return NoteComand.SORTNOTESBYTAGS
        else:
            return NoteComand.UNKNOWN

    def __str__(self):
        return f"{self.comand}" 
        