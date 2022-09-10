
class Note:
    def __init__(self, text: str, tags: list[str] = []) -> None:
        self.text = text
        self.tags = tags

    def __repr__(self) -> str:
        return "\nTegs: " + ", ".join([tag for tag in self.tags]) + f"\nNote text: {self.note}"
