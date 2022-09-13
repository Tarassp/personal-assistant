from typing import Optional
from address_book_app.address_book import AddressBook
from address_book_app.address_book_command import AddressBookCommand
from address_book_app.fields import Birthday, Phone, Name
from address_book_app.record import Record
from shared.error_decorator import *
from shared.assistant_exceptions import *
from shared.local_storage import StorageInterface
from shared.status import HandlerStatus


class AddressBookService:
    
    def __init__(self, storage: StorageInterface, address_book: AddressBook) -> None:
        self._address_book = address_book
        self._selected_record: Optional[Record] = None
        self._searched_records: list[Record] = []
        self._storage = storage
        self._handlers = {
            AddressBookCommand.HELLO: self._handle_hello,
            AddressBookCommand.ADD: self._handle_add,
            AddressBookCommand.ADDPHONE: self._handle_add_phone,
            AddressBookCommand.SETEMAIL: self._handle_set_email,
            AddressBookCommand.SETADDRESS: self._handle_set_address,
            AddressBookCommand.SETBIRTHDAY: self._handle_set_birthday,
            AddressBookCommand.SELECTREQUEST: self._handle_select_request,
            AddressBookCommand.SELECT: self._handle_select_record,
            AddressBookCommand.CHANGE: self._handle_change,
            AddressBookCommand.PHONE: self._handle_phone,
            AddressBookCommand.SHOW: self._handle_show,
            AddressBookCommand.SEARCH: self._handle_search,
            AddressBookCommand.SEARCHSELECTING: self._handle_search_selecting,
            AddressBookCommand.SAVE: self._handle_save,
            AddressBookCommand.LOAD: self._handle_open,
            AddressBookCommand.EXIT: self._handle_exit,
            AddressBookCommand.HELP: self._handle_help,
            AddressBookCommand.UNKNOWN: self._handle_unknown
        }
    
    def handle(self, command: AddressBookCommand, value: list[str]) -> HandlerStatus:
        handler = self.get_handler(command)
        return handler(value)
    
    @input_error
    def _handle_hello(self, value) -> str:
        return 'How can I help you?'
    
    def _handle_select_request(self, value: list[str]) -> HandlerStatus:
        if len(value) == 1:
            return self._handle_select_record(value)
        request = HandlerStatus.Request(
            'Enter some text to find records or just hit "Enter" to show all records: ', AddressBookCommand.SEARCHSELECTING)
        return HandlerStatus(request=request)
    
    def _handle_select_record(self, value: list[str]) -> HandlerStatus:
        record_number = int(value[0])
        if (record_number - 1) < len(self._searched_records):
            self._selected_record = self._searched_records[record_number - 1]
        elif len(self._address_book) > 0:
            self._selected_record = self._address_book[0]
        else:
            return HandlerStatus('Cannot select the record because Address Book is empty.')
        return HandlerStatus('The record is selected. Use <TAGS>, <CHANGE>, or <DELETE> command to work on it')
    
    def _handle_search_selecting(self, value: list[str]) -> HandlerStatus:
        search_status = self._handle_search(value)
        if search_status.response.lower() != 'no result':
            search_status.request = HandlerStatus.Request(
                'Enter the record number: ', AddressBookCommand.SELECT)
        return search_status
    
    @input_error   
    def _handle_add(self, value: list[str]) -> HandlerStatus:
        if len(value) < 2:
            raise UnknownAssistentValue('Give me a name and phone number(s) please.')
        self._address_book.add_record(value[0], value[1:])
        return HandlerStatus('Contact added successfully!')
    
    def _handle_add_phone(self, value: list[str]) -> HandlerStatus:
        if len(value) < 1:
            raise UnknownAssistentValue('Please, enter one or more phone numbers!')
        if self._selected_record:
            self._selected_record.add_phone(value)
        else:
            return HandlerStatus("You didn't select record yet. Please use SELECT command first.")
        self._selected_record = None
        
        if len(value) > 1:
            return HandlerStatus('Phones are added successfully!')
        return HandlerStatus('Phone is added successfully!')
    
    def _handle_set_email(self, value: list[str]) -> HandlerStatus:
        if len(value) != 1:
            raise UnknownAssistentValue('Should be only one email')
        if self._selected_record:
            self._selected_record.set_email(value[0])
        else:
            return HandlerStatus("You didn't select record yet. Please use SELECT command first.")
        self._selected_record = None
        
        return HandlerStatus('Email is set successfully!')
    
    def _handle_set_address(self, value: list[str]) -> HandlerStatus:
        if len(value) < 1:
            raise UnknownAssistentValue('Address cannot be empty!')
        if self._selected_record:
            self._selected_record.set_address(value)
        else:
            return HandlerStatus("You didn't select record yet. Please use SELECT command first.")
        self._selected_record = None
        return HandlerStatus('Address is set successfully!')
        
    def _handle_set_birthday(self, value: list[str]) -> HandlerStatus:
        if len(value) != 1:
            raise UnknownAssistentValue('Should be only one birthday')
        if self._selected_record:
            self._selected_record.set_birthday(value[0])
        else:
            return HandlerStatus("You didn't select record yet. Please use SELECT command first.")
        self._selected_record = None
        return HandlerStatus('Birthday is set successfully!')

    @input_error
    def _handle_change(self, value: list[str]) -> str:
        if len(value) != 2:
            raise UnknownAssistentValue('Give me name and phone please.')
        message = 'Contact updated successfully!'
        if value[0].lower() not in [x.lower() for x in self._address_book.keys()]:
            message = 'This contact does not exist for updating.\nSo a new contact was created!'
        self._handle_add(value)
        return message
    
    @input_error
    def _handle_phone(self, value: list[str]) -> str:
        if len(value) != 1:
            raise UnknownAssistentValue('Give me name.')
        record = self._address_book.find_by_name(Name(value[0])) or "The specified contact does not exist."
        return str(record) 
    
    @input_error
    def _handle_search(self, value: list[str]) -> HandlerStatus:
        searched_text = ' '.join(value)
        records = self._address_book.search(searched_text)
        
        if records:
            message = ""
            for i, v in enumerate(records):
                message += f'{i + 1}. {v}\n'
            message.strip('\n')
            message = "----------------------\n" + message + "----------------------"
            return HandlerStatus(message)
        return HandlerStatus('No Results')
    
    @input_error
    def _handle_show(self, value) -> HandlerStatus:
        message = ""
        for i, v in enumerate(self._address_book.values()):
            message += f'{i + 1}. {v}\n'
        
        message.strip('\n')
        if not message:
            message = 'Contact list is empty!\n'
        message = "----------------------\n" + message + "----------------------"
        
        return HandlerStatus(message)
    
    def _handle_save(self, value: list[str]):
        if len(value) != 1:
            raise IncorrectFileName()
        self._storage.save(self._address_book, value[0])
        return 'Address Book saved successfully!'
    
    def _handle_open(self, value: list[str]):
        if len(value) != 1:
            raise IncorrectFileName()
        self._address_book = self._storage.load(value[0])
        return 'Address Book loaded successfully!'
    
    @input_error
    def _handle_exit(self, value) -> str:
        return 'Good bye!'

    @input_error
    def _handle_help(self, value) -> str:
        commands = ['HELLO', 'ADD <name> <phone> <phone>...',
                    'CHANGE <name> <phone>', 'PHONE <name>',
                    'SEARCH <text>',
                    'LOAD <filename>', 'SAVE <filename>',
                    'SHOW ALL', 'GOOD BYE', 'CLOSE', 'EXIT']
        return '\n'.join(commands)
    
    @input_error
    def _handle_unknown(value) -> str:
        return 'Incorrect Command!!!'
    
    @input_error
    def get_handler(self, command: AddressBookCommand):
        if command is AddressBookCommand.UNKNOWN:
            raise UnknownAssistentCommand
        return self._handlers[command]