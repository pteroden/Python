__author__ = 'piotr'

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''

    keys = []
    values = []
    duplicated = []

    for key in aDict.keys():
        if not aDict[key] in values:
            if aDict[key] not in duplicated:
                keys.append(key)
                values.append(aDict[key])
            else:
                duplicated.append(aDict[key])
        else:
            duplicated.append(aDict[keys.pop(values.index(aDict[key]))])
            values.remove(aDict[key])
        print "Keys: {0}, values: {1}, duplicated: {2}".format(keys, values, duplicated)
    return sorted(keys)


aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}

print uniqueValues(aDict)