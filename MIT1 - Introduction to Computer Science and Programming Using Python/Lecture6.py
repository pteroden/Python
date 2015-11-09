def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    result = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            result += (aTup[i],)
    return result

print oddTuples((16, 9, 18, 11, 10, 20, 20, 4, 2, 6))



def minus(a):
    return a - 1

print minus(4)



animals = { 'a': ['aardvark', 'dyuo', 'grsgh', 'hytg'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    for d in aDict:
        counter += len(aDict[d])
    return counter

print howMany(animals)

print "New entry!!"

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    counter = {}
    for d in aDict:
        counter[d] = len(aDict[d])
    if counter == {}: return None
    big = max(counter.values())
    for d in counter:
        if big == counter[d]:
            return d
    # return big, aDict.values()

print biggest(animals)
biggest({})



print 'Problem set - exercise 1'

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    area = 0
    while start < stop:
        area += f(start) * step
        start += step
    return area

print 'Test case 1: %s, 39.10318784326239' %radiationExposure(0, 5, 1)
print 'Test case 1: %s, 22.94241041057671' %radiationExposure(5, 11, 1)
print 'Test case 1: %s, 62.0455982538' %radiationExposure(0, 11, 1)
print 'Test case 1: %s, 0.434612356115' %radiationExposure(40, 100, 1.5)