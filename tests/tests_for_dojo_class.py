import unittest
import os
from dojo_app.dojo import Dojo


class TestDojoApplication(unittest.TestCase):

    def setUp(self):
        self.sample_dojo = Dojo()

        #Create sample Living Room in Test Dojo
        self.sample_dojo.create_room({"<room_name>": ["SRoomA"],"Living": True,"Office": False})
        self.srooma = self.sample_dojo.dojo_livingspaces[0]

        #Create Sample Office in This Test Dojo
        self.sample_dojo.create_room({"<room_name>": ["RoomA"],"Living": False,"Office": True})
        self.rooma = self.sample_dojo.dojo_office_rooms[0]

        #Add Sample Person To Sample Dojo
        self.sample_dojo.add_person({"<first_name>": "Test","<last_name>": "Fellow","<wants_space>": "Y","Fellow": True, "Staff": False})
        self.test_add_fellow = self.sample_dojo.people_in_dojo[0]

        self.sample_dojo.add_person({"<first_name>": "Test","<last_name>": "Staff","<wants_space>": "Y","Fellow": False,"Staff": True})
        self.test_add_staff = self.sample_dojo.people_in_dojo[0]

    def test_create_room(self):
        self.assertEqual(2, len(self.sample_dojo.dojo_rooms))
        self.assertEqual(1, len(self.sample_dojo.dojo_livingspaces))
        self.assertEqual(1, len(self.sample_dojo.dojo_office_rooms))

        self.sample_dojo.create_room({"<room_name>": ["SRoomB", "SRoomC"],"Living": True,"Office": False})

        self.assertEqual(4, len(self.sample_dojo.dojo_rooms))
        self.assertEqual(3, len(self.sample_dojo.dojo_livingspaces))

        self.sample_dojo.create_room({"<room_name>": ["RoomB", "RoomC"],"Living": False,"Office": True})

        self.assertEqual(6, len(self.sample_dojo.dojo_rooms))
        self.assertEqual(3, len(self.sample_dojo.dojo_office_rooms))


        self.sample_dojo.create_room({"<room_name>": ["RoomA", "RoomB"],"Living": False,"Office": True})

        self.assertEqual(6, len(self.sample_dojo.dojo_rooms))
        self.assertEqual(3, len(self.sample_dojo.dojo_office_rooms))

    def test_add_person(self):
        self.assertEqual(2, len(self.sample_dojo.people_in_dojo))
        self.assertEqual(1, len(self.sample_dojo.dojo_fellows))
        self.assertEqual(1, len(self.sample_dojo.dojo_staff))

        self.assertEqual(2, len(self.rooma.occupants))

    def test_free_offices(self):
        self.sample_dojo.create_room({"<room_name>": ["RoomB"],"Living": False,"Office": True})

        self.sample_dojo.reconcile_room_occupancy()

        self.assertEqual(2, len(self.sample_dojo.dojo_free_offices))
        self.assertEqual(3, len(self.sample_dojo.dojo_free_rooms))



    def test_print_allocations(self):
        self.sample_dojo.print_allocations({"--o": "test_print_allocated.txt"})

        self.assertTrue(os.path.exists("test_print_allocated.txt"))

        with open("test_print_allocated.txt") as myfile:
            lines = myfile.readlines()
            self.assertTrue("SRoomA\n" in lines)
            self.assertTrue("RoomA\n" in lines)
            self.assertTrue("Test Fellow, Test Staff\n" in lines)
        os.remove("test_print_allocated.txt")

    def test_print_unallocated(self):
        self.sample_dojo.add_person({"<first_name>": "Test","<last_name>": "Fellow2","<wants_space>": "N","Fellow": True,"Staff": False})
        self.sample_dojo.print_unallocated({"--o": "test_print_unallocated.txt"})

        self.assertTrue(os.path.exists("test_print_unallocated.txt"))

        with open("test_print_unallocated.txt") as myfile:
            lines = myfile.readlines()
            self.assertTrue("People without rooms\n" in lines)
            self.assertTrue("There are no unallocated people in the system.\n" in lines)
        os.remove("test_print_unallocated.txt")