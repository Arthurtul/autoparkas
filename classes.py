import datetime
import math


class Driver:
    def __init__(self, scheduled_leave_start: datetime, scheduled_leave_end: datetime, licence_category, salary):
        self.scheduled_leave_start = scheduled_leave_start
        self.scheduled_leave_end = scheduled_leave_end
        self.licence_category = licence_category
        self.salary = salary


class Vehicle(Driver):

    def __init__(self, odometer, transported_weight, vehicle_number, gas_type, costs, drivers_license, l_km,
                 tech_insp: datetime, insurance_date, scheduled_leave_start: datetime, scheduled_leave_end: datetime,
                 licence_category, salary, gas_price=None):
        super().__init__(scheduled_leave_start, scheduled_leave_end, licence_category, salary)
        self.odometer = odometer
        self.transported_weight = transported_weight
        self.vehicle_number = vehicle_number
        self.gas_type = gas_type
        self.costs = costs
        self.drivers_license = drivers_license
        self.l_km = l_km
        self.tech_insp = tech_insp
        self.insurance_date = insurance_date
        self.gas_price = gas_price

    def is_insurance_required_next_month(self):
        insurance_date = datetime.datetime.strptime(str(self.insurance_date), "%Y-%m-%d").date()
        next_month = datetime.date.today() + datetime.timedelta(days=30)
        return insurance_date < next_month

    def is_tech_insp_required_next_month(self):
        tech_insp_date = (self.tech_insp + datetime.timedelta(730)).replace(day=1)
        next_month = datetime.date.today() + datetime.timedelta(days=30)
        return tech_insp_date < next_month

    def estimated_trip_costs(self, distance):
        fuel_cost = self.l_km * distance * self.gas_price
        cost_for_km = self.odometer / self.costs
        return round(fuel_cost + cost_for_km, 2)

    def is_driver_on_holiday(self, checked_time: datetime):
        if self.scheduled_leave_start <= checked_time <= self.scheduled_leave_end:
            return "Driver is unavailable, he is on holiday"
        else:
            return "Driver is  available, he is not on holiday"


class Bus(Vehicle):
    def __init__(self, passenger_seats, odometer, vehicle_number, gas_type, costs, drivers_license,
                 l_km, tech_insp, insurance_date, gas_price):
        super().__init__(odometer, None, vehicle_number, gas_type, costs, drivers_license, l_km,
                         tech_insp, insurance_date, gas_price, licence_category=None, salary=None,
                         scheduled_leave_end=None)
        self.passenger_seats = passenger_seats

    def how_much_buses_needed(self, num_of_passengers):
        num_buses = num_of_passengers // self.passenger_seats
        if num_of_passengers % self.passenger_seats > 0:
            num_buses += 1
        return num_buses


class Car(Vehicle):
    def __init__(self, odometer, vehicle_number, gas_type, costs, drivers_license,
                 l_km, tech_insp, insurance_date):
        super().__init__(odometer, None, vehicle_number, gas_type, costs, drivers_license, l_km,
                         tech_insp, insurance_date, licence_category=None, salary=None, scheduled_leave_end=None,
                         scheduled_leave_start=None)


# here transported_weight is weight that a vehicle, this case truck, can transport by itself
# trailer_carry is weight that trailer can transport by itself
# in the function calculate trips we take only one argument "load" is a weight that needs to be carried


class Truck(Vehicle, Driver):
    def __init__(self, odometer, transported_weight, trailer_carry, vehicle_number, gas_type, costs,
                 drivers_license, l_km, tech_insp, insurance_date, gas_price, licence_category):
        super().__init__(odometer, transported_weight, vehicle_number, gas_type, costs, drivers_license, l_km,
                         tech_insp, insurance_date, gas_price, scheduled_leave_end=None,
                         salary=None, licence_category=None)
        self.transported_weight = transported_weight
        self.trailer_carry = trailer_carry
        self.licence_category = licence_category

    def calculate_trips(self, load):
        if not self.transported_weight:
            return math.ceil(load / self.transported_weight)
        else:
            trips = math.ceil(load / (self.transported_weight + self.trailer_carry))
            trips_with_trailer = math.ceil((load - (trips * self.transported_weight)) / self.trailer_carry)
            trips_with_trailer = trips_with_trailer if trips_with_trailer > 0 else 0
            return trips, trips_with_trailer

    def check_if_licence_category(self):
        if self.licence_category == "D":
            return "Driver can drive a truck with trailer"
        else:
            return "Driver can not drive a truck with trailer"
