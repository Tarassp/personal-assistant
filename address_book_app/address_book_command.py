from enum import Enum, unique

@unique
class AddressBookCommand(Enum):
        HELLO = ['hello']
        SELECT = ['choose']
        SELECTREQUEST = ['select']
        ADD = ['add']
        ADDPHONE = ['add phone']
        SETEMAIL = ['set email']
        SETADDRESS = ['set address']
        SETBIRTHDAY = ['set birthday']
        CHANGE = ['change']
        PHONE = ['phone']
        SHOW = ['show all']
        EXIT = ['exit', 'close', 'good bye']
        LOAD = ['load']
        SAVE = ['save']
        SEARCH = ['search']
        SEARCHSELECTING = ['search selecting']
        HELP = ['help']
        UNKNOWN = ['unknown']
        NONE = ['none']
        
        @classmethod
        def _missing_(cls, value: str):
            for item in cls.__members__.values():
                if value.lower() in item.value:
                    return item
            else:
                return cls.UNKNOWN
        
        @classmethod
        @property
        def max_command_words(cls) -> int:
            return 2

    