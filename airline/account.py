# see : grokking-the-object-oriented-design-interview
"""
https://github.com/tssovi/grokking-the-object-oriented-design-interview/blob/master/example-codes/airline-management-system/constants.py

"""

from abc import ABC
from .constant import AccountState
class Account():
    def __init__(self,id,password,status=AccountState.ACTIVE):
        self.__id  = id
        self.__password = password
        self.__status = status
    def get_reset_password(self):
        None

class Person(ABC):
    def __init__(self,name,address,email,phone,account):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__account = account

class Customer(Person):
    def __init__(self,frequent_flyer_number): 
        self.__frequent_flyer_number = frequent_flyer_number
    def get_itineraries(self):
        None

class Passenger:
    def __init__(self,name,passport_num,date_of_brith):
        self.__name = name
        self.__passport_num = passport_num
        self.__date_of_brith = date_of_brith


class Address:
    def __init__(self,street,city,state,country,zip_code):
        self.__street = street
        self.__city = city
        self.__country = country
        self.__zip_code = zip_code
        self.__state = state