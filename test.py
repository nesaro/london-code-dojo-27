import unittest
from pub import Glass, Customer

class MyTest(unittest.TestCase):
    def test_glass(self):
        glass = Glass()
        self.assertEqual(glass.content, 20)

    def test_drink(self):
        customer = Customer()
        customer.buy_beer()
        customer.drink()
        self.assertEqual(customer.glass.content, 19)

    def test_quaff(self):
        customer = Customer()
        customer.buy_beer()
        customer.quaff()
        self.assertEqual(customer.glass.content, 16)

    def test_one_off(self):
        customer = Customer()
        customer.buy_beer()
        customer.down_in_one()
        self.assertEqual(customer.glass.content, 0)

    def test_too_much(self):
        customer = Customer()
        customer.buy_beer()
        customer.down_in_one()
        self.assertEqual(customer.glass.content, 0)
        self.assertRaises(Exception, customer.quaff)

    def test_half_drink(self):
        customer = Customer()
        customer.buy_beer("half")
        customer.drink()
        self.assertEqual(customer.glass.content, 9)

    def test_half_quaff(self):
        customer = Customer()
        customer.buy_beer("half")
        customer.quaff()
        self.assertEqual(customer.glass.content, 6)

    def test_half_one_off(self):
        customer = Customer()
        customer.buy_beer("half")
        customer.down_in_one()
        self.assertEqual(customer.glass.content, 0)

    def test_triple_drink(self):
        customer = Customer()
        customer.buy_beer("triple")
        customer.drink()
        self.assertEqual(customer.glass.content, 59)

    def test_triple_quaff(self):
        customer = Customer()
        customer.buy_beer("triple")
        customer.quaff()
        self.assertEqual(customer.glass.content, 56)

    def test_triple_one_off(self):
        customer = Customer()
        customer.buy_beer("triple")
        customer.down_in_one()
        self.assertEqual(customer.glass.content, 0)

