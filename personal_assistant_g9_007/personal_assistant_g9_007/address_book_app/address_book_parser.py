from personal_assistant_g9_007.address_book_app.address_book_command import AddressBookCommand
class AddressBookParser:
    def __init__(self, string: str, reserved_command = AddressBookCommand.NONE):
        self._line_parameters = string.split()
        self.quantity_words_in_command = 0
        self.reserved_command = reserved_command
    
    def get_command(self) -> AddressBookCommand:
        if self.reserved_command is not AddressBookCommand.NONE:
            return self.reserved_command
                
        for i in reversed(range(AddressBookCommand.max_command_words)):
            raw_command = ' '.join(self._line_parameters[:i + 1])
            command = AddressBookCommand(raw_command)
            if command is not AddressBookCommand.UNKNOWN:
                self.quantity_words_in_command = len(raw_command.split())
                return command
        return AddressBookCommand.UNKNOWN
    
    def get_value(self) -> list[str]:
        value = self._line_parameters[self.quantity_words_in_command:]
        return value