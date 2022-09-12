import pickle
from abc import abstractmethod
from typing import Protocol

class StorageInterface(Protocol):
    @abstractmethod
    def save(self, object, filename):
        raise NotImplementedError
    
    @abstractmethod
    def load(self, filename):
        raise NotImplementedError


class LocalStorage(StorageInterface):
    def save(self, object, filename):
        with open(filename, "wb") as fh:
            pickle.dump(object, fh)
            
    def load(self, filename):
        with open(filename, "rb") as fh:
            unpacked = pickle.load(fh)
            return unpacked
