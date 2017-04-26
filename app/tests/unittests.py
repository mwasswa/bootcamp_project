import unittest
from app.classes.dojo import Dojo
class SpaceAllocationsTestCases(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_create_room_returns_proper_success_message(self):
        self.assertEqual("An office called Dojo Room 1 has been successfully created!", self.dojo.create_room('office','Dojo Room 1'),
                         msg='Should return the right success message if input arguments are proper')

    def test_add_person_returns_proper_success_message(self):
        self.assertEqual("Staff Neil Armstrong has been successfully added. Neil has been allocated the office Blue", self.dojo.add_person('Neil Armstrong', 'Staff'),
                     msg='Should return the right success message if input arguments are proper')


    def test_print_room(self):pass


    def test_print_allocations(self):pass


    def test_raises_error_for_missing_room_name(self):pass


    def test_raises_error_for_missing_person_name(self):pass

    def test_prime_numbers_in_range_returns_emptylist_if_arg_is_zero(self):
        self.assertEqual("argument must be an integer greater than 2", prime_numbers_in_range(0),
                         msg='should return error message if input is zero')

    def test_prime_numbers_in_range_returns_emptylist_if_arg_is_unity(self):
        self.assertEqual("argument must be an integer greater than 2", prime_numbers_in_range(1),
                         msg='should return error message if input value is 1')

    def test_prime_numbers_in_range_returns_list_if_arg_is_ten(self):
        self.assertEqual([2, 3, 5, 7], prime_numbers_in_range(10),
                         msg='Output must be list of prime numbers')

    def test_prime_numbers_in_range_returns_output_of_type_list_if_arg_isvalid(self):
        self.assertIsInstance(prime_numbers_in_range(10), list,
                              msg='Invalid output type. Should be a list')

    def test_prime_numbers_in_range_returns_emptylist_for_negative_arg(self):
        self.assertEqual("argument must be an integer greater than 2", prime_numbers_in_range(-10),
                         msg='Should return error message if argument is negative')

