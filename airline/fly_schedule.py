class WeeklySchedule:
    def __init__(self, time, day_week):
        self.__time = time
        self.__day_week = day_week


class CustomSchedule:
    def __init__(self, custom_date, time):
        self.__custom_date = custom_date
        self.__time = time


class Flight:
    def __init__(self, flight_number, departure, arrival, duration_in_minutes):
        self.__flight_number = flight_number
        self.__departure = departure
        self.__arrival = arrival
        self.__duration_in_minutes = duration_in_minutes

        self.__weekly_schedules = []
        self.__custom_schedules = []
        self.__flight_instances = []


class FlightImstance:
    def __init__(self, departure_time, gate, status, aircraft):
        self.__departure_time = departure_time
        self.__gate = gate
        self.__status = status
        self.__aircraft = aircraft

    def cancel(self):
        None

    def update_status(self, status):
        None


class flyReservation:
    def __init__(self, reservation_num, flight, aircraft, creation_date, status):
        self.__reservation_number = reservation_number
        self.__flight = flight
        self.__seat_map = {}
        self.__creation_date = creation_date
        self.__status = status

    def fetch_reservation_details(self, reservation_number):
        None

    def get_passengers(self):
        None


class Itinerary:
    def __init__(self, customer_id, starting_airport, final_airport, creation_date):
        self.__customer_id = customer_id
        self.__starting_airport = starting_airport
        self.__final_airport = final_airport
        self.__creation_date = creation_date
        self.__reservations = []

    def get_reservations(self):
        None

    def make_reservation(self):
        None

    def make_payment(self):
        None
