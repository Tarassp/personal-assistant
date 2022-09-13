from address_book_app.address_book_command import AddressBookCommand

class AddressBookParser:
    def __init__(self, string: str):
        self._line_parameters = string.split()
        self.quantity_words_in_command = 0
    
    def get_command(self) -> AddressBookCommand:        
        for i in range(AddressBookCommand.max_command_words):
            raw_command = ' '.join(self._line_parameters[:i + 1])
            command = AddressBookCommand(raw_command)
            if command is not AddressBookCommand.UNKNOWN:
                self.quantity_words_in_command = len(raw_command.split())
                return command
        return AddressBookCommand.UNKNOWN
    
    def get_value(self) -> list[str]:
        value = self._line_parameters[self.quantity_words_in_command:]
        return value