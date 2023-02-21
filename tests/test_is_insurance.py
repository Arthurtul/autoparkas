import unittest
from classes import Vehicle


class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.test_vehicle = Vehicle(
            odometer=10000,
            transported_weight=2000,
            vehicle_number="ABC123",
            gas_type="Regular",
            costs=100,
            drivers_license="A123456",
            l_km=10,
            tech_insp="2023-02-20",
            insurance_date="2023-01-01",
            gas_price=2.0
        )

    def test_is_insurance_required_next_month(self):
        # test 1: Insurance is required next month
        self.test_vehicle.insurance_date = "2023-03-01"
        self.assertTrue(self.test_vehicle.is_insurance_required_next_month())

        # test 2: Insurance is not required next month
        self.test_vehicle.insurance_date = "2023-04-01"
        self.assertFalse(self.test_vehicle.is_insurance_required_next_month())


if __name__ == '__main__':
    unittest.main()
