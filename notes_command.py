from enum import Enum, unique

@unique
class NotesCommand(Enum):
        ADD = ['add']
        TAGS = ['tags']
        SELECTREQUEST = ['select']
        SELECT = ['choose']
        CHANGE = ['change']
        DELETE = ['delete']
        SHOW = ['show all']
        SEARCH = ['search']
        SEARCHBYTAG = ['search tag']
        SEARCHSELECTING = ['search selecting']
        SORTBYTAG = ['sort tag']
        HELP = ['help']
        UNKNOWN = ['unknown']
        EXIT = ['exit', 'close', 'good bye']
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