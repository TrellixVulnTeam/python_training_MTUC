from sys import maxsize
class Contact:

    def __init__(self, firstname=None, secondname=None, surname=None, nickname=None,
                 title=None, company=None, address=None, home=None, mobile=None, work=None, email=None, id=None):
        self.firstname=firstname
        self.secondname=secondname
        self.surname=surname
        self.nickname=nickname
        self.title=title
        self.company=company
        self.address=address
        self.home=home
        self.mobile=mobile
        self.work=work
        self.email=email
        self.id=id

    def __repr__(self):
        return "%s: %s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
