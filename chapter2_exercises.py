# Exercises for chapter 2:

# Name: Hunter Perry

# Exercise 2.1. 
# zipcode = 02492 generates a SyntaxError message because "9" is not within the octal number system. When an integer is lead with a zero in Python it generates the Octal representation for that number. >>> zipcode = 02132 only contains numbers between 0 and 7 therefore generating 1114 as the octal representation.

# Exercise 2.2.
# Below is the statement in the Python interpreter.
>>> 5
5
>>> x = 5
>>> x + 1
6
# Below is the statement modified into a print statement.
>>> print 5
5
>>> x = 5
>>> print x + 1
6

# Exercise 2.3.
width = 17
height = 12.0
delimiter = '.'
# 1. width/2 - Value = 8, Type = Integer
# 2. width/2.0 - Value = 8.5, Type = Variable
# 3. height/3 - Value = 4, Type = Integer
# 4. 1 + 2 * 5 - Value = 11, Type = Integer
# 5. delimiter * 5 - Value = '.....', Type = String

# Exercise 2. 4.
# 1.
>>> r = 'radius'
>>> v = 'volume'
>>> v = 1.333 * pi * 5 ** 3
>>> v
523.4678759043992
# 2. 
>>> p = 'cover price'
>>> d = 'discount'
>>> s1 = 'shipping cost'
>>> s2 = 'shipping cost for additional copy'
>>> n = 'number of copies'
>>> t = 'total'
>>> p =24.95
>>> p = 24.95
>>> d = .6
>>> s1 = 3.00
>>> s2 = .75
>>> n = 60
>>> t = ((n - 1) * (p * d + s2) + (p * d + s1))
>>> t = ((60 - 1) * (24.95 * .6 + .75) + (24.95 * .6 + 3.00))
>>> t
945.4499999999999
# 3.
>>> t = 'return time'
>>> t = (412.00 / 60.00) + (8.25 / 60.00 ) + (7.20 / 60.00) + (7.20 / 60.00) + (7.20 / 60.00)+ (8.25 / 60.00 )
>>> t
7.501666666666667
# t = 7 hours 30 minutes 10 seconds