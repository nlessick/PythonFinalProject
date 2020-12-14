import unittest
from main_window import foreign_currency as fc


class TestCurrency(unittest.TestCase):
    def setUp(self):
        self.f_c = fc.determine_foreign_currency(self, "Australia")

    def tearDown(self):
        del self.f_c

    def test_inital_value_required_attributes(self):
        self.assertEqual(self.f_c.selection, "Australia")

    def test_object_not_created_error(self):
        with self.assertRaises(ValueError):
            c = fc.determine_foreign_currency(self, "Alaska")

    def test_return_value_true(self):
        c = fc.determine_foreign_currency(self, "India")
        self.assertEqual(fc.determine_foreign_currency(c), .014)

    def test_return_value_false(self):
        with self.assertRaises(ValueError):
            c = fc.determine_foreign_currency(self, "Europe")
            self.assertEqual(fc.determine_foreign_currency(c), 3.30)




if __name__ == '__main__':
    unittest.main()
