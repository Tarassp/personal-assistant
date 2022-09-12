from enum import Enum, unique

@unique
class AssistantCommand(Enum):
        HELLO = ['hello']
        ADD = ['add']
        CHANGE = ['change']
        PHONE = ['phone']
        SHOW = ['show all']
        EXIT = ['exit', 'close', 'good bye']
        LOAD = ['load']
        SAVE = ['save']
        SEARCH = ['search']
        HELP = ['help']
        UNKNOWN = ['unknown']
        
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
        
        @property
        def max_value_words(self) -> int:
            match self:
                case AssistantCommand.HELLO | AssistantCommand.SHOW | AssistantCommand.EXIT | AssistantCommand.HELP:
                    return 0
                case AssistantCommand.PHONE | AssistantCommand.SEARCH | AssistantCommand.LOAD | AssistantCommand.SAVE:
                    return 1
                case _:
                    return 2

    