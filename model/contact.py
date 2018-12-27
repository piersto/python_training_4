class Contact:
    def __init__(self, firstname=None, lastname=None, middlename=None, birthday=None, birth_month=None, id=id):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.birthday = birthday
        self.birth_month = birth_month
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.id, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.firstname == other.firstname
