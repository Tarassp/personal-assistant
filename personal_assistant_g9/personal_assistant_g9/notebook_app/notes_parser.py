from personal_assistant_g9.notebook_app.notes_command import NotesCommand


class NotesParser:
    def __init__(self, string: str, reserved_command = NotesCommand.NONE):
        self._line_parameters = string.split()
        self.quantity_words_in_command = 0
        self.reserved_command = reserved_command

    def get_command(self) -> NotesCommand:
        if self.reserved_command is not NotesCommand.NONE:
            return self.reserved_command

        for i in reversed(range(NotesCommand.max_command_words)):
            raw_command = ' '.join(self._line_parameters[:i + 1])
            command = NotesCommand(raw_command)
            if command is not NotesCommand.UNKNOWN:
                self.quantity_words_in_command = len(raw_command.split())
                return command
        return NotesCommand.UNKNOWN

    def get_value(self) -> list[str]:
        value = self._line_parameters[self.quantity_words_in_command:]
        return value
