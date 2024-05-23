# see : grokking-the-object-oriented-design-interview
"""
https://github.com/tssovi/grokking-the-object-oriented-design-interview/blob/master/example-codes/airline-management-system/constants.py

"""


class AirPort:
    def __init__(self, name, address, code):
        self.__name = name
        self.__address = address
        self.__code = code

    def get_flights(self):
        None


class AirCraft:
    def __init__(self, name, model, manufacturing_year):
        self.__name = name
        self.__model = model
        self.__manufacturing_year = manufacturing_year

    def get_flights(self):
        None


class Seat:
    def __init__(self, seat_num, type_seat, seat_class):
        self.__ = seat_num
        self.__type_seat = type_seat
        self.__seat_class = seat_class

    pass


class FlightSeat(Seat):
    def __init__(self, fare):
        self.__fare = fare

    def get_fare(self):
        return self.__fare
