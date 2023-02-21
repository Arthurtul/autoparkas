import datetime


class Vehicle:

    def __init__(self, odometer, transported_weight, vehicle_number, gas_type, costs, drivers_license,
                 l_km, tech_insp, insurance_date, gas_price=None):
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
        tech_insp_date = datetime.datetime.strptime(self.tech_insp, "%Y-%m-%d").date()
        next_month = datetime.date.today() + datetime.timedelta(days=30)
        return tech_insp_date < next_month

    def estimated_costs(self, x):
        fuel_cost = self.l_km * x * self.gas_price
        total_cost = fuel_cost + self.costs
        return total_cost


class Bus(Vehicle):
    def __init__(self, passenger_seats, odometer, vehicle_number, gas_type, costs, drivers_license,
                 l_km, tech_insp, insurance_date, gas_price):
        super().__init__(odometer, None, vehicle_number, gas_type, costs, drivers_license, l_km,
                         tech_insp, insurance_date, gas_price)
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
                         tech_insp, insurance_date)

# here transported_weight is weight that a vehicle, this case truck, can transport by itself
# trailer_carry is weight that trailer can transport by itself
# in the function calculate trips we take only one argument "load" is a weight that needs to be carried
class Truck(Vehicle):
    def __init__(self, odometer, transported_weight, trailer_carry,  vehicle_number, gas_type, costs,
                 drivers_license, l_km, tech_insp, insurance_date, gas_price):
        super().__init__(odometer, transported_weight, vehicle_number, gas_type, costs, drivers_license, l_km,
                         tech_insp, insurance_date, gas_price)
        self.transported_weight = transported_weight
        self.trailer_carry = trailer_carry

    def calculate_trips(self, load):
        total_carry_capacity = self.transported_weight + self.trailer_carry  # truck and trailer carry together
        truck_trips = 0
        trailer_trips = 0
        total_trips = truck_trips + trailer_trips

        return truck_trips, trailer_trips, total_trips
