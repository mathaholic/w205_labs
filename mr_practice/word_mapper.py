#!/usr/bin/python
### wordmapper.py
### mapper that splits a document into its 
### constituent bits.

### testing on a project Gutenberg e-book.  Should
### probably remove the non-alpha numerics too just
### in case

import sys
import re

for line in sys.stdin:
	#if a line starts/ends with non- \w (alpha numeric), remove
	line = re.sub(r'^\W+|\W+$', '', line).strip()
	words = line.split(' ')
	#split the line into a list of words on the word

	if len(words) >1:
		for word in words:
		### if it ain't an alpnanumeral...
	 
		#w = re.search(r'[\W]', word)
			w = re.search(r'\W+|\W+$', word)
		### ... get rid of it
			if w:
				print(word[:w.start()].lower() + word[w.end():].lower() + '\t1')
			else:
				print(word.lower() + '\t1')
	else: continue
