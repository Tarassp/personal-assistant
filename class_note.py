
class Note:
    def __init__(self, note: str, tegs: list[str] = None) -> None:
        self.note = note
        self.tegs = tegs if tegs != None else []

    def __repr__(self) -> str:
        return "\nTegs: " + ", ".join([teg for teg in self.tegs]) + f"\nNote text: {self.note}"


if __name__ == "__main__":
    note_1 = Note("Hello world!")
    print(note_1)
    note_1 = Note("Hello world!", ["hello"])
    print(note_1)
    note_1 = Note("Hello world!", ["hello", "world"])
    print(note_1)
