__author__ = 'piotr'

L = [13, 10, 5, 1, 7, 6, 2, 4, 3]
# L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def sort1(lst):
    print
    print "This is {0} iteration, this is list: {1}".format("#", lst)
    swapFlag = True
    iteration = 0
    while swapFlag:
        swapFlag = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = temp
                swapFlag = True

        L = lst[:]  # the next 3 questions assume this line just executed
        print "This is {0} iteration, this is list: {1}".format(iteration, L)
        iteration += 1
    return lst


# sort1(L)


def sort2(lst):
    print
    print "This is {0} iteration, this is list: {1}".format("#", lst)
    for iteration in range(len(lst)):
        minIndex = iteration
        minValue = lst[iteration]
        for j in range(iteration+1, len(lst)):
            if lst[j] < minValue:
                minIndex = j
                minValue = lst[j]
        temp = lst[iteration]
        lst[iteration] = minValue
        lst[minIndex] = temp

        L = lst[:]  # the next 3 questions assume this line just executed
        print "This is {0} iteration, this is list: {1}".format(iteration, lst)
    return lst


# sort2(L)


def sort3(lst):
    print
    print "This is {0} iteration, this is list: {1}".format("#", lst)
    out = []
    for iteration in range(0,len(lst)):
        new = lst[iteration]
        inserted = False
        for j in range(len(out)):
            if new < out[j]:
                out.insert(j, new)
                inserted = True
                break
        if not inserted:
            out.append(new)

        L = out[:]  # the next 3 questions assume this line just executed
        print "This is {0} iteration, this is list: {1}".format(iteration, lst)
    return out


# sort3(L)


recursive = 0
def sort4(lst):
    global recursive

    print
    print "This is {0} iteration, this is list: {1}".format("#", lst)
    def unite(l1, l2):
        if len(l1) == 0:
            return l2
        elif len(l2) == 0:
            return l1
        elif l1[0] < l2[0]:
            return [l1[0]] + unite(l1[1:], l2)
        else:
            return [l2[0]] + unite(l1, l2[1:])

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        front = sort4(lst[:len(lst)/2])
        back = sort4(lst[len(lst)/2:])

        L = lst[:]  # the next 3 questions assume this line just executed

        return unite(front, back)
    print "This is {0} recursive, this is list: {1}".format(recursive, lst)
    recursive += 1


# sort4(L)