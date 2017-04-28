class Person(object):
    """
    Creates a Person object. Classes Fellow and Staff inherit from it.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name #"<Person %s>" % self.name


class Staff(Person):

    person_type = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)

    def __str__(self):
        return self.name #"<Staff %s>" % self.name


class Fellow(Person):

    person_type = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)

    def __str__(self):
        return self.name #"Fellow %s>" % self.name