class Room(object):
    offices = []
    living_spaces = []
    def __init__(self):
        pass


class Office(Room):
    maximum_occupants = 6
    def record_office(self,office_name):
        if office_name not in self.offices:
            self.offices.append(office_name)

class LivingSpace(Room):
    maximum_occupants = 4
    def record_livingspace(self,living_space):
        if living_space not in self.living_spaces:
            self.living_spaces.append(living_space)