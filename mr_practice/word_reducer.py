#!/usr/bin/python
###word_reducer.py
#
#
###take split and ordered words from mapper and sort
### then make a dict of all terms and sum them up
#
import sys
#import coll

previous = None
s = 0

for line in sys.stdin:
	#get a list of the sorted words
	line = line.split('\t')
	if line[0] != previous:
		if previous is not None:
			print(str(s)+ '\t'+ previous)
		previous = line[0]
		s = 0
	s = s + 1

print(str(s)+ '\t'+ previous)


'''
previous = None
sum = 0

for key, value in map_sorted:

    if key != previous:
        if previous is not None:
            print(str( sum ), '\t' , previous)
        previous = key
        sum = 0
    
    sum = sum + value

print(str( sum ) , '\t' , previous)
'''

#./word_mapper.py < test1.txt | sort | ./word_reducer.py

