class Person(object):
    """
    Creates a Person object. Classes Fellow and Staff inherit from it.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "<Room %s>" % self.name


class Staff(Person):

    person_type = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)

    def __str__(self):
        return "<Staff %s>" % self.name


class Fellow(Person):

    person_type = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)

    def __str__(self):
        return "Fellow %s>" % self.name