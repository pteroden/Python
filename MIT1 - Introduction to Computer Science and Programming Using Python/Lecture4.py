def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result

print iterPower(2, 3)



def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

print recurPower(2, 10)



def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp/2)
    else:
        return base * recurPowerNew(base, exp - 1)

print recurPowerNew(2, 10)



def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    smaller = min(a, b)
    while a >= 1:
        if a % smaller == 0 and b % smaller == 0:
            return smaller
        else:
            smaller -= 1

print gcdIter(8, 12)



def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

print gcdRecur(8, 12)



def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    num = 0
    for i in aStr:
        num += 1
    return num

print lenIter('Piotr')



def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])

print lenRecur('Piotr')



def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    aStr = aStr.lower()
    char = char.lower()
    middle = len(aStr)/2

    if aStr == '':
        return False
    elif char == aStr[middle]:
        return True
    else:
        if char < aStr[middle]:
            return isIn(char, aStr[:middle])
        else:
            return isIn(char, aStr[middle+1:])

print isIn('a', 'hijklmnopr')



def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1) != len(str2):
        return False
    if str1 == '' or str2 == '':
        return True
    elif str1[0] != str2[-1]:
        return False
    else:
        return semordnilap(str1[1:], str2[:-1])


print semordnilap('nametag', 'hateman')




def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')

testFib(5)