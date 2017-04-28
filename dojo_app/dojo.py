import random

from dojo_app.people import Staff, Fellow

from dojo_app.rooms import Office, Living


class Dojo(object):
    def __init__(self):
        self.people_in_dojo = []
        self.people_with_rooms = []
        self.people_without_rooms = []
        self.dojo_fellows = []
        self.fellows_with_rooms = []
        self.dojo_free_livingspaces = []
        self.dojo_staff = []
        self.staff_with_rooms = []
        self.dojo_rooms = []
        self.dojo_free_rooms = []
        self.dojo_office_rooms = []
        self.dojo_free_offices = []
        self.dojo_livingspaces = []

    def create_room(self, commandline_args):
        exists = added = ""
        rooms_list = commandline_args["<room_name>"]
        for room in rooms_list:
            if room.lower() in [room_bject.name.lower() for room_bject in self.dojo_rooms]:
                exists += "The room " + room + " already exists \n"
            else:
                if commandline_args["Office"]:
                    office = Office(room)
                    self.dojo_office_rooms.append(office)
                    added += "An Office called " + room + " has been successfully created!\n"
                    self.dojo_rooms.append(office)
                elif commandline_args["Living"]:
                    livingspace = Living(room)
                    self.dojo_livingspaces.append(livingspace)
                    added += "A Living Space called " + room + " has been successfully created!\n"
                    self.dojo_rooms.append(livingspace)

        self.reconcile_room_occupancy()
        print(exists + added)

    def reconcile_room_occupancy(self):
        for office in self.dojo_office_rooms:
            if len(office.occupants) < office.max_occupants:
                if office not in self.dojo_free_offices:
                    self.dojo_free_offices.append(office)
                    self.dojo_free_rooms.append(office)
            elif len(office.occupants) >= office.max_occupants:
                if office in self.dojo_free_offices:
                    self.dojo_free_offices.remove(office)
                    self.dojo_free_rooms.remove(office)
        for livingspace in self.dojo_livingspaces:
            if len(livingspace.occupants) < livingspace.max_occupants:
                if livingspace not in self.dojo_free_livingspaces:
                    self.dojo_free_livingspaces.append(livingspace)
                    self.dojo_free_rooms.append(livingspace)
            elif len(livingspace.occupants) >= livingspace.max_occupants:
                if livingspace in self.dojo_free_livingspaces:
                    self.dojo_free_livingspaces.remove(livingspace)
                    self.dojo_free_rooms.remove(livingspace)

    def add_person(self,commandline_args):
        person_name = commandline_args["<first_name>"] + " " + commandline_args["<last_name>"]
        wants_accomodation = commandline_args["<wants_space>"]
        self.reconcile_room_occupancy()
        if commandline_args["Staff"]:
            self.reconcile_room_occupancy()
            new_staff = Staff(person_name)
            self.dojo_staff.append(new_staff)
            self.people_in_dojo.append(new_staff)
            message = person_name + " has been successfully added!\n"
            random_office_choice = random.choice(self.dojo_free_offices)
            random_office_choice.occupants.append(new_staff)
            message += commandline_args["<first_name>"] + " has been allocated the office %s " % str(random_office_choice)\
            + "\n"
            self.staff_with_rooms.append(new_staff)
            self.people_with_rooms.append(new_staff)
        elif commandline_args["Fellow"]:
            self.reconcile_room_occupancy()
            new_fellow = Fellow(person_name)
            self.dojo_fellows.append(new_fellow)
            self.people_in_dojo.append(new_fellow)
            message = person_name + " has been successfully added!\n"
            random_choice = random.choice(self.dojo_free_offices)
            random_choice.occupants.append(new_fellow)
            message += commandline_args["<first_name>"] + " has been allocated the Office %s " % str(random_choice)\
            + "\n"
            self.fellows_with_rooms.append(new_fellow)
            self.people_with_rooms.append(new_fellow)
            if wants_accomodation == 'Y':
                livingspace_choice = random.choice(self.dojo_free_livingspaces)
                livingspace_choice.occupants.append(new_fellow)
                message += commandline_args["<first_name>"] + " has been allocated the Living Space %s "\
                                                              % str(livingspace_choice)
        print(message)

    def reallocate_person(self, args):
        person_name = args["<first_name>"] + " " + args["<last_name>"]
        new_person = None
        for person in self.people_in_dojo:
            if person.name == person_name:
                new_person = person

        if new_person is None:
            print("The Person " + person_name + "does not exist in the Dojo. \n" \
            "Use the add_person command to register them\n")
            return
        new_room_name = args["<new_room>"]

        for room in self.dojo_rooms:
            if room.name == new_room_name:
                new_room = room

        if new_room_name not in [r.name for r in self.dojo_free_rooms]:
            print("The room " + new_room_name + " is either vacant or does not exist")
            return

        if new_person.person_type == "Staff":
            if new_room.room_type == "Living":
                print(person_name + " is of type Staff and cannot be assigned a living space " + new_room)
                return

        for room in self.dojo_free_rooms:
            if new_person.name in [person.name for person in room.occupants]:
                if new_room == room:
                    print(new_person.name + " is already an occupant of room %s " % str(room))
                    return
                else:
                    room.occupants.remove(new_person)

        new_room.occupants.append(new_person)
        self.people_with_rooms.append(new_person)
        if new_person.person_type == "Fellow":
            self.fellows_with_rooms.append(new_person)
        elif new_person.person_type == "Fellow":
            self.staff_with_rooms.append(new_person)
        else:
            print("Invalid Person type")


        if new_person in self.people_without_rooms:
            self.people_without_rooms.remove(new_person)

        print("The person has been successfully re-allocated the room %s " % str(new_room))

    def load_people(self, args):
        filename = args["<filename>"]
        with open(filename, 'r') as input_people_file:
            people = input_people_file.readlines()
            for line in people:
                line = line.split()
                if line:
                    first_name = line[0]
                    last_name = line[1]
                    if line[2] == "FELLOW":
                        is_staff = False
                        is_fellow = True
                    else:
                        is_staff = True
                        is_fellow = False
                    if len(line) == 4:
                        wants_space = line[3]
                    else:
                        wants_space = None

                    self.add_person({
                        "<first_name>": first_name.title(),
                        "<last_name>": last_name.title(),
                        "<wants_space>": wants_space,
                        "Fellow": is_fellow,
                        "Staff": is_staff
                    })

    def print_allocations(self, args):
        message = ""
        for r in self.dojo_rooms:
            message += r.name + "\n"
            message += "-" * 50 + "\n"
            if r.occupants:
                message += ", ".join(p.name for p in r.occupants) + "\n"
                message +=  "\n"
            else:
                message += "This room has no occupants.\n"
                message += "\n"
        if not self.dojo_rooms:
            message += "There are no rooms in the system.\n"
            message += "Add a room using the create_room command" \
                      " and try again.\n"
        print(message)
        if args["--o"]:
            with open(args["--o"], 'wt') as f:
                f.write(message)
                print("The list of allocations has been saved " \
                      "to the following file: " + args["--o"])

    def print_unallocated(self, args):
        message = "People without rooms\n ----------------------------------------------------------------\n"
        for person in self.people_in_dojo:
            if person not in self.people_with_rooms:
                message += person.name + "\n"
                if person not in self.people_without_rooms:
                    self.people_without_rooms.append(person)
        if not self.people_in_dojo:
            message += "There are no people in the system.\n Add a person using the add_person command and try again.\n"
        elif not self.people_without_rooms:
            message += "There are no unallocated people in the system.\n"
        print(message)
        if args["--o"]:
            with open(args["--o"], 'wt') as f:
                f.write(message)
                print("The list of unallocated people has been saved to the following file: ")
                print(args["--o"])

    def print_room(self, args):
        room_name = args["<room_name>"]
        if room_name not in [room_object.name for room_object in self.dojo_rooms]:
            return "The room "+ room_name +" you have entered " + " doesn't exist"
        else:
            for room in self.dojo_rooms:
                if room.name == room_name:
                    room_object = room
                    print(room_object.name)
                    print("--------------------------------------------------------------------------\n")
                    if room_object.occupants:
                        for person in room_object.occupants:
                            print(person.name)
                    else:
                        print("This room has no occupants.")



