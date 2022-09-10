import pickle

class NoteStorage:
    def save(self, object):
        NotImplementedError("You must define a save function")

    
    def restore(self):
        NotImplementedError("You must define a restore function")
    
    def set_file_name(self, name):
        NotImplementedError("You must define a set _file_name function")


class LocalStorage(NoteStorage):
    def __init__(self, file_name: str = 'data.bin') -> None:
        self.__file_name = file_name
        
    def set_file_name(self, name: str):
        self.__file_name = name
        
    def save(self, object):
        with open(self.__file_name, "wb") as fh:
            pickle.dump(object, fh)
            
    def restore(self):
        with open(self.__file_name, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked
