class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print self.time


clock = Clock('5:30')
clock.print_time()


class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self, time):
        print time


clock = Clock('5:30')
clock.print_time('10:30')

'''
class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8

w1 = Weird(X, Y)
print w1.getX()
'''

'''
L11 PROBLEM 4
'''


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        if (self.x == other.x) & (self.y == other.y):
            return True
        else:
            return False

    def __repr__(self):
        return 'Coordinate(%d, %d)' % (self.x, self.y)


w1 = Coordinate(1, -8)
w2 = Coordinate(1, -8)

print w1
print w2
print w1 == w2
# print w1.__eq__()
print repr(w1)



class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ', '.join([str(e) for e in self.vals]) + '}'



s = intSet()
print s
s.insert(3)
s.insert(4)
s.insert(3)
print s
s.member(3)
s.member(5)
s.insert(6)
print s
# s.remove(3)
print s
s.remove(3)
s.vals