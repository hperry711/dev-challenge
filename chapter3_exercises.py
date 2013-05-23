# Exercises for chapter 3:

# Name: Hunter Perry

# Exercise 3.1.
>>> repeat_lyrics()

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    repeat_lyrics()
NameError: name 'repeat_lyrics' is not defined

#Exercise 3.2.
>>> def print_lyrics():
	print "I'm a lumberjack, and I'm okay."
	print "I sleep all night and I work all day."

	
>>> def repeat_lyrics():
	print_lyrics()
	print_lyrics()

	
>>> repeat_lyrics()
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.
I'm a lumberjack, and I'm okay.
I sleep all night and I work all day.

#Exercise 3.3.
>>> def right_justify ():
>>> len ('allen')
5
>>> 70 / 5
14
>>> print ('allen' * 14)
allenallenallenallenallenallenallenallenallenallenallenallenallenallen

#Exercise 3.4.
>>> def do_twice(f):
	f()
	f()

	
>>> def print_spam():
	print 'spam'

	
>>> do_twice (print_spam)
spam
spam
>>> def print_twice(line1, line2):
	line1 = ' spam '
	line2 = ' spam '

	
>>> print ( line1 + line2 )
spamspam
>>> def do_twice(f, arg):
    f(arg)
    f(arg)

    
>>> def print_twice(arg):
    print arg
    print arg

    
>>> do_twice(print_twice, 'spam')
spam
spam
spam
spam