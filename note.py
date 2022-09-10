
class Note:
    def __init__(self, note: str, tags: list[str] = []) -> None:
        self.note = note
        self.tags = tags

    def __repr__(self) -> str:
        return "\nTegs: " + ", ".join([teg for teg in self.tegs]) + f"\nNote text: {self.note}"
