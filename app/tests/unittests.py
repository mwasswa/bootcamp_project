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


    def test_print_room(self):
        self.assertIsInstance([],self.dojo.print_room('Dojo Room 1'),msg='Should return a list of names of occupants')


    def test_print_allocations(self):pass


    def test_raises_error_for_missing_room_name(self):pass


    def test_raises_error_for_missing_person_name(self):pass
