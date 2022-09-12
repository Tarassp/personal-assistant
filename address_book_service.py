from address_book import AddressBook
from assistant_command import AssistantCommand
from error_decorator import *
from assistant_exceptions import *
from fields import Birthday, Phone, Name
from record import Record
from local_storage import StorageInterface


class AddressBookService:
    
    def __init__(self, storage: StorageInterface, address_book: AddressBook) -> None:
        self.address_book = address_book
        self._storage = storage
        self._handlers = {
            AssistantCommand.HELLO: self._handle_hello,
            AssistantCommand.ADD: self._handle_add,
            AssistantCommand.CHANGE: self._handle_change,
            AssistantCommand.PHONE: self._handle_phone,
            AssistantCommand.SHOW: self._handle_show,
            AssistantCommand.SEARCH: self._handle_search,
            AssistantCommand.SAVE: self._handle_save,
            AssistantCommand.LOAD: self._handle_open,
            AssistantCommand.EXIT: self._handle_exit,
            AssistantCommand.HELP: self._handle_help,
            AssistantCommand.UNKNOWN: self._handle_unknown
        }
    
    def handle(self, command: AssistantCommand, value: list[str]) -> str:
        handler = self.get_handler(command)
        return handler(value)
    
    @input_error
    def _handle_hello(self, value) -> str:
        return 'How can I help you?'
    
    @input_error   
    def _handle_add(self, value: list[str]) -> str:
        if len(value) != 2:
            raise UnknownAssistentValue('Give me name and phone please.')
        record = Record(Name(value[0]), Phone(value[1]))
        self.address_book.add_record(record)
        return 'Contact added successfully!'

    @input_error
    def _handle_change(self, value: list[str]) -> str:
        if len(value) != 2:
            raise UnknownAssistentValue('Give me name and phone please.')
        message = 'Contact updated successfully!'
        if value[0].lower() not in [x.lower() for x in self.address_book.keys()]:
            message = 'This contact does not exist for updating.\nSo a new contact was created!'
        self._handle_add(value)
        return message
    
    @input_error
    def _handle_phone(self, value: list[str]) -> str:
        if len(value) != 1:
            raise UnknownAssistentValue('Give me name.')
        record = self.address_book.find_by_name(Name(value[0])) or "The specified contact does not exist."
        return str(record) 
    
    @input_error
    def _handle_search(self, value: list[str]) -> str:
        if len(value) != 1:
            raise UnknownAssistentValue('Give me a text without spaces')
        records = self.address_book.search(value[0])
        
        if records:
            message = ""
            for i, v in enumerate(records):
                message += f'{i + 1}. {v}\n'
            message.strip('\n')
            return "----------------------\n" + message + "----------------------"
        return 'No Results'
    
    @input_error
    def _handle_show(self, value):
        message = ""
        for i, v in enumerate(self.address_book.values()):
            message += f'{i + 1}. {v}\n'
        
        message.strip('\n')
        if not message:
            message = 'Contact list is empty!\n'
        message = "----------------------\n" + message + "----------------------"
        
        return message
    
    def _handle_save(self, value: list[str]):
        if len(value) != 1:
            raise IncorrectFileName()
        self._storage.save(self.address_book, value[0])
        return 'Address Book saved successfully!'
    
    def _handle_open(self, value: list[str]):
        if len(value) != 1:
            raise IncorrectFileName()
        self.address_book = self._storage.load(value[0])
        return 'Address Book loaded successfully!'
    
    @input_error
    def _handle_exit(self, value) -> str:
        return 'Good bye!'

    @input_error
    def _handle_help(self, value) -> str:
        commands = ['HELLO', 'ADD <name> <phone>',
                    'CHANGE <name> <phone>', 'PHONE <name>',
                    'SEARCH <text>',
                    'LOAD <filename>', 'SAVE <filename>',
                    'SHOW ALL', 'GOOD BYE', 'CLOSE', 'EXIT']
        return '\n'.join(commands)
    
    @input_error
    def _handle_unknown(value) -> str:
        return 'Incorrect Command!!!'
    
    @input_error
    def get_handler(self, command: AssistantCommand):
        if command is AssistantCommand.UNKNOWN:
            raise UnknownAssistentCommand
        return self._handlers[command]