#!/usr/bin/python

from numpy.random import *

print 'Rolling the dice...'

die1 = randint(1,7)
die2 = randint(1,7)

print 'Die 1:',die1
print 'Die 2:',die2

print 'Total value:',die1 + die2

if die1 + die2 > 7:
	print 'You won'
else:
	print 'You lost'