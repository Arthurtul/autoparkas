import unittest
from classes import Truck


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_vehicle = Truck(
            odometer=1000,
            transported_weight=20,
            trailer_carry=1,
            vehicle_number="abc123",
            gas_type="diesel",
            costs=200,
            drivers_license="AZ2424",
            l_km=100,
            tech_insp="2022-01-01",
            insurance_date="2023-03-03",
            gas_price=1.5,
            licence_category="D"
        )

    def test_calculate_trips(self):
        self.assertEqual((2, 2), self.test_vehicle.calculate_trips(71))


if __name__ == '__main__':
    unittest.main()
