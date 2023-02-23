from classes import *
from datetime import datetime

trips_1 = Truck(odometer=1000, transported_weight=10, trailer_carry=8, vehicle_number="abc123",
                gas_type="petrol",
                costs="200", drivers_license="yes", l_km=100, tech_insp="2022-02-02", insurance_date="2023-01-01",
                gas_price=1.5, licence_category="D")

print(trips_1.check_if_licence_category())
print(trips_1.calculate_trips(109))

driver_tom = Vehicle(odometer=1000,
                     transported_weight=0,
                     vehicle_number="aaa111",
                     gas_type="petrol",
                     costs="150",
                     drivers_license="Yes",
                     l_km="8",
                     tech_insp=datetime(2023, 6, 2),
                     insurance_date="2022-02-02",
                     licence_category="D",
                     salary="1500",
                     scheduled_leave_start=datetime(2023, 7, 10),
                     scheduled_leave_end=datetime(2023, 7, 20)
                     )

print(driver_tom.is_driver_on_holiday(datetime(2023, 7, 10)))


my_bus = Bus(
            passenger_seats=20,
            odometer=10000,
            vehicle_number="ABC123",
            gas_type="Regular",
            costs=100,
            drivers_license="A123456",
            l_km=10,
            tech_insp="2023-02-20",
            insurance_date="2023-01-01",
            gas_price=2.0)

print(my_bus.how_much_buses_needed(40))
