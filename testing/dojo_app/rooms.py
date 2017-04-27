class Room(object):
    def __init__(self, name):
        self.occupants = []
        self.name = name

    def __str__(self):
        return "<Room %s>" % (self.name)



class Office(Room):
    max_occupants = 6
    room_type = "Office"
    def __init__(self, name):
        super(Office, self).__init__(name)

    def __str__(self):
        return "<Office %s>" % (self.name)


class Living(Room):
    room_type = "Living"
    max_occupants = 4

    def __init__(self, name):
        super(Living, self).__init__(name)

    def __str__(self):
        return "<Living space %s>" % (self.name)