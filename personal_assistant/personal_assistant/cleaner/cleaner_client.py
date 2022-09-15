from personal_assistant.cleaner.folder_cleaner import FolderCleaner
from personal_assistant.cleaner.logger import FileLogger
from personal_assistant.cleaner.normalizer import *
import sys

class CleanerClient:

    def run(self):
        hint = "Enter a full path to a directory or type 'exit': "
        while True:
            line = input(hint)
            
            if line.lower() == 'exit':
                break
            
            cleaner = FolderCleaner(line, NameNormalizer(), FileLogger())
            cleaner.clean()
            print('Done!')

    
