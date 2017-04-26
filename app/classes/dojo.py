import random
from app.classes.rooms import Office
from app.classes.rooms import LivingSpace

from app.classes.people import Staff
from app.classes.people import Fellow

class Dojo(object):
    def __init__(self):
        self.rooms = [{'offices': []}, {'living_spaces': []}]
        self.people = [{'fellows': []}, {'staff': []}]
        self.staff = Staff()
        self.fellow = Fellow()
        self.office = Office()
        self.living_space = LivingSpace()

    # self.room_allocations = {}

    def create_room(self, room_type, *room_name):
        message = ""
        dicts = {}
        for room in room_name:
            dicts[room] = []
            if room_type.lower() == 'office':
                self.rooms[0]['offices'].append(dicts)
                message += "An " + room_type + " called " + room + " has been successfully created!"
                self.office.record_office(room)
            elif room_type.lower() == 'livingspace':
                self.rooms[1]['living_spaces'].append(dicts)
                message += "A " + room_type + " called " + room + " has been successfully created!"
                self.living_space.record_livingspace(room)

            else:
                message += "The room " + room + " must be either an office or living"

        return message

    def add_person(self, person_name, person_type, wants_accomodation='N'):
        names = person_name.split()
        person_first_name = names[0]
        person_last_name = names[1]
        if person_type.lower() == 'fellow':
            if self.people[0]['fellows'].append(person_name):
                self.fellow.record_fellow(person_name)
                if wants_accomodation == 'Y':
                    room_allocated = self.allocate_person_room(person_name, 'Y')

                    if len(room_allocated['office']) and len(room_allocated['livingspace']):
                        return "{} {} has been successfully added.".format(person_type,person_name) + "\n" + person_first_name + " has been allocated the office "+ room_allocated['office'] + "\n" + person_first_name + " has been allocated the livingspace " +  room_allocated['livingspace']
                    else:
                        return "{} {} has been successfully added.".format(person_type, person_name) + "\n" + person_first_name + " has been allocated the office "+ room_allocated['office']
        elif person_type.lower() == 'staff':
            if self.people[1]['staff'].append(person_name):
                self.staff.record_staff(person_name)
                room_allocated = self.allocate_person_room(person_name)
                return "{} {} has been successfully added.".format(person_type,
                                                                   person_name) + "\n" + person_first_name + " has been allocated the office " + \
                       room_allocated['office']
        else:
            return person_name + " must be either a type fellow or staff"

    def allocate_person_room(self, person_name, wants_accomodation='N'):
        maximum_occupants = self.office.maximum_occupants
        possible_offices = []
        for offices in self.rooms[0]['offices']:
            for office, occupants in offices.items():
                if len(occupants) < maximum_occupants:
                    possible_offices.append(office)
        assigned_office = random.choice(possible_offices)


        if wants_accomodation == 'Y':
            maximum_occupants = self.living_space.maximum_occupants
            possible_living_spaces = []
            for living_space in self.rooms[1]['living_spaces']:
                for room, occupants in living_space.items():
                    if len(occupants) < maximum_occupants:
                        possible_living_spaces.append(room)
            assigned_livingspace = random.choice(possible_living_spaces)


            return {'office': assigned_office, 'livingspace': assigned_livingspace}

        else:
            return {'office': assigned_office}

    def print_room(self,room_name):
        for dicts in self.rooms[0]['offices']:  #[{'room':[occ1,occ2,occ3]},{},{}]
            if room_name in dicts:
                return (dicts[room_name])

        for dicts in self.rooms[1]['living_spaces']:
            if room_name in dicts:
                return (dicts[room_name])

    def print_allocations(self):
        for dicts in self.rooms[0]['offices']:  #[{'room':[occ1,occ2,occ3]},{},{}]
            for room_name, occupants_list in dicts.items():
                occupants = ""
                if len(occupants_list) > 0:
                    for occupant in occupants_list:
                        occupants += occupant.upper() + ", "
        print(room_name.upper() + "\n --------------------------------------\n" + occupants + "\n\n")

        for dicts in self.rooms[1]['living_spaces']:  #[{'room':[occ1,occ2,occ3]},{},{}]
            for room_name, occupants_list in dicts.items():
                occupants = ""
                if len(occupants_list) > 0:
                    for occupant in occupants_list:
                        occupants += occupant.upper() + ", "
        print(room_name.upper() + "\n --------------------------------------\n" + occupants + "\n\n")


    def print_unallocations(self):
        print("Unallocated Offices: \n\n")
        for dicts in self.rooms[0]['offices']:  #[{'room':[occ1,occ2,occ3]},{},{}]
            for room_name, occupants_list in dicts.items():
                if len(occupants_list) == 0:
                    return room_name.upper() + "\n"

        print("Unallocated Living Spaces: \n\n")
        for dicts in self.rooms[1]['living_spaces']:  #[{'room':[occ1,occ2,occ3]},{},{}]
            for room_name, occupants_list in dicts.items():
                if len(occupants_list) == 0:
                    return room_name.upper() + "\n"

    def reallocate_person(self,person_name,new_room):
        for rooms in self.rooms:
            offices = rooms['offices']
            spaces = rooms['living_spaces']

        for office in offices:
            for room, occupants in office.items():
                if person_name in occupants:
                    if occupants.remove(person_name) and new_room in office and person_name not in office[new_room]:
                        office[new_room].append(person_name)


        for space in spaces:
            for room, occupants in space.items():
                if person_name in occupants:
                    if occupants.remove(person_name) and new_room in space and person_name not in space[new_room]:
                        space[new_room].append(person_name)



    def load_people(self):pass

    def save_state(self):pass

    def load_state(self):pass

dojo = Dojo()

print(dojo.create_room('office','Dojo Room 1'))
print(dojo.create_room('livingspace','Dojo Room 2'))
