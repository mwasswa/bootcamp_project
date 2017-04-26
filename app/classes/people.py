class Person(object):
    staff_members = []
    fellows = []
    def __init__(self):
        pass


class Fellow(Person):
    def record_fellow(self,fellow_name):
        if fellow_name not in self.fellows:
            self.fellows.append(fellow_name)

class Staff(Person):
    def record_staff(self,staff_name):
        if staff_name not in self.staff_members:
            self.staff_members.append(staff_name)