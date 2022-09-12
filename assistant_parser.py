from assistant_command import AssistantCommand
from assistant_exceptions import UnknownAssistentCommand, UnknownAssistentValue

class AssistantParser:
    def __init__(self, string: str):
        self._line_parameters = string.split()
        self.quantity_words_in_command = 0
    
    def get_command(self) -> AssistantCommand:        
        for i in range(AssistantCommand.max_command_words):
            raw_command = ' '.join(self._line_parameters[:i + 1])
            command = AssistantCommand(raw_command)
            if command is not AssistantCommand.UNKNOWN:
                self.quantity_words_in_command = len(raw_command.split())
                return command
        return AssistantCommand.UNKNOWN
    
    def get_value(self) -> list[str]:
        value = self._line_parameters[self.quantity_words_in_command:]
        return value