import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('erick', 'adikah', 50000)
        emp_2 = Employee('sue', 'smith', 60000)

        self.assertEqual(emp_1.email, 'erick.adikah@email.com')
        self.assertEqual(emp_2.email, 'sue.smith@email.com')

        emp_1.first = 'john'
        emp_2.first = 'jane'

        self.assertEqual(emp_1.email, 'john.adikah@email.com')
        self.assertEqual(emp_2.email, 'jane.smith@email.com')

    def test_fullname(self):
        emp_1 = Employee('erick', 'adikah', 50000)
        emp_2 = Employee('sue', 'smith', 60000)

        self.assertEqual(emp_1.fullname, 'erick adikah')
        self.assertEqual(emp_2.fullname, 'sue smith')

        emp_1.first = 'john'
        emp_2.first = 'jane'

        self.assertEqual(emp_1.fullname, 'john adikah')
        self.assertEqual(emp_2.fullname, 'jane smith')

    def test_apply_raise(self):
        emp_1 = Employee('erick', 'adikah', 50000)
        emp_2 = Employee('sue', 'smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()
