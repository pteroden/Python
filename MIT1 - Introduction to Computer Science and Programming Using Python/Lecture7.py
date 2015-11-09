def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print '1st excercise:'
print integerDivision(0, 1)



def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a)

print '2nd excercise:'
print rem(2, 5)
print rem(5, 5)
print rem(7, 5)



def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
       return 1
   else:
       return n * f(n-1)


print '3rd excercise:'
print f(3)
print f(2)
print f(1)
print f(0)