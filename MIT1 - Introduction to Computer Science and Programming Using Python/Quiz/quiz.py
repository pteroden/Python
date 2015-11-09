# coding=utf-8

# ZADANIE 1
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    power = 0
    while b**power < x:
        if b**(power + 1) > x:
            break
        else:
            power += 1
    return power

print myLog(15, 3)


# ZADANIE 2
def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    result = []
    for element in aList:
        if len(element) < 4:
            result.append(element)
    return result

print lessThan4(["apple", "cat", "dog", "banana"])


# ZADANIE 3
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        return N
    else:
        return N % 10 + sumDigits(N / 10)

print 'Test case %d:' %1
print sumDigits(103456)
print 1+0+3+4+5+6
print 'Test case %d:' %2
print sumDigits(7)
print 7
print 'Test case %d:' %3
print sumDigits(123)
print 1+2+3
print 'Test case %d:' %4
print sumDigits(0)
print 0
print 'Test case %d:' %5
print sumDigits(12345678912568743)
print 1+2+3+4+5+6+7+8+9+1+2+5+6+8+7+4+3

# ZADANIE 4
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    result = []
    for element in aDict:
        if aDict[element] == target:
            result.append(element)
    result.sort()
    return result

aDict = {'aaa':1, 'bbb':12, 'ccc':2, 'ddd':2, 'eee':2, 'fff':3, 'aab':2}
print keysWithValue(aDict, 2)

# ZADANIE 5
print 'ZADANIE 5'
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    listIter = L[:]
    for element in listIter:
        if not f(element):
            L.remove(element)
    return len(L)

# run_satisfiesF(L, satisfiesF)

def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L


# ZADANIE 3.1
print 'Odpowiedź %d' %1
stuff  = ["iBoy", "iGirl", "iQ", "iC","iPaid","iPad"]
for thing in stuff:
    if thing == 'iPad':
        print "Found it"

print 'Odpowiedź %d' %2
stuff  = ("iBoy", "iGirl", "iQ", "iC","iPaid","iPad")
for thing in stuff:
    if thing == 'iPad':
        print "Found it"

print 'Odpowiedź %d' %3
stuff  = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
for thing in stuff:
    if thing == 'iPad':
        print "Found it"

print 'Odpowiedź %d' %4
stuff  = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
for thing in stuff:
    if thing == 'iPad':
        print "Found it"

print 'Odpowiedź %d' %5
stuff  = "iPad"
for thing in stuff:
    if thing == 'iPad':
        print "Found it"

print 'Odpowiedź %d' %6
stuff  = 'iPad'
for thing in stuff:
    if thing == 'iPad':
        print "Found it"

# ZADANIE 3.2
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print Square(10)