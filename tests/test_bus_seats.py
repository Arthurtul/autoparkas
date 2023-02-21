import unittest
from classes import Bus


class TestBusSeats(unittest.TestCase):
    def setUp(self):
        self.test_vehicle = Bus(
            passenger_seats=50,
            odometer=10000,
            vehicle_number="ABC123",
            gas_type="Regular",
            costs=100,
            drivers_license="A123456",
            l_km=10,
            tech_insp="2023-02-20",
            insurance_date="2023-01-01",
            gas_price=2.0
        )

    def test_how_much_buses_needed(self):
        # test conditions by given number of passengers for example in given setup passenger seats = 50, so
        # to transfer 100 passengers you need 2 buses, for 50 passengers you need one bus
        self.assertEqual(self.test_vehicle.how_much_buses_needed(100), 2)
        self.assertEqual(self.test_vehicle.how_much_buses_needed(50), 1)
        self.assertEqual(self.test_vehicle.how_much_buses_needed(0), 0)
        self.assertEqual(self.test_vehicle.how_much_buses_needed(51), 2)
        self.assertEqual(self.test_vehicle.how_much_buses_needed(48), 1)


if __name__ == '__main__':
    unittest.main()
