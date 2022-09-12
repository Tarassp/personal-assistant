from typing import Optional
from fields import Phone, Name, Birthday
from datetime import datetime
import re

class Record:
    def __init__(self, name: Name, *phones: Phone, birthday: Optional[Birthday] = None) -> None:
        self.name = name
        self.birthday = birthday
        self.phones = list(phones)
        
    def add_phone(self, phone: Phone):
        self.phones.insert(0, phone)
        
    def remove_phone(self, phone: Phone):
        self.phones.remove(phone)
        
    def update_phone(self, phone: Phone):
        pass
    
    def days_to_birthday(self) -> Optional[int]:
        if self.birthday:
            birthday_date = self.birthday.datetime
            now = datetime.now()
            delta1 = datetime(now.year, birthday_date.month, birthday_date.day)
            delta2 = datetime(now.year+1, birthday_date.month, birthday_date.day)
            return ((delta1 if delta1 > now else delta2) - now).days
        return None
    
    def __contains__(self, other):
        l = []
        if self.__has_valid_phone(other):
            l = list(filter(lambda x: other in x, self.phones))
        if not l:
            return other in self.name
        return bool(l)
    
    def __has_valid_phone(self, string: str) -> bool:
        return re.search('^\+?\d+$', string) != None
    
    def __str__(self) -> str:
        phone_list = 'Absent'
        if self.phones:
            phone_list = ', '.join(map(str, self.phones))
        
        if self.birthday:
            return '%s, %s, %s' % (self.name, phone_list, self.birthday)
        return '%s, %s' % (self.name, phone_list)