# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:49:37 2020

@author: Administrator
"""

#!/home/sayandip199309/anaconda3/envs/tensorflow_gpu/bin/python

import sys
import os
import code
import itertools
import collections
import pdb
from contextlib import suppress



#keywords = [method for method in dir(REPL) if not method.startswith('__')]
#
#def readfunc(prompt):
#    inp = code.InteractiveConsole().raw_input(prompt)

repl_obj = REPL()
fallback = False
def readfunc(prompt):
	global fallback
	inp = code.InteractiveConsole().raw_input(prompt="\n>>> ")
	if inp == 'fallback':
		fallback = True
	args = inp.split()

	if fallback:
		code.InteractiveConsole().interact(banner="fallingback to native REPL", exitmsg="End")
	elif len(args) == 1:
		try:
			func = getattr(repl_obj, inp.strip())
			output = func()
			return output
		except (TypeError, AttributeError):
			return ascii(eval(inp))

	elif len(args) > 1:
#		try:
		method, *params = inp.split()
		func = getattr(repl_obj, method)
		output = func(*params)
		return f"{output}"
#		except AttributeError:
#			exec(inp)
#		finally:
#			return ""
	return args

class REPL:
    """Creates a REPL object, with some methods"""

    def __init__(self):
        self.output_data = []
        self.count = None
        self.index_counter = 0

    def Open(self, filename):
        """ Opens the provided file, appends the file object to
            self.output_data, increments the index_counter """
        with suppress(FileNotFoundError):
            fileobj = open(filename)
            data = fileobj.read()
            fileobj.close()
            self.output_data.append(data)
            self.index_counter += 1
            return ascii(f"#{self.index_counter - 1}: {fileobj!r}")

    def Filter(self, token, index_provided = None):
        """ Filters the specified token from the file object. """
        try:
            index_provided = int(index_provided)
        except (ValueError, TypeError):
            index_provided = -1
        data = self.output_data[index_provided]
        filtered = [line for line in data.split('\n') if token in line]
        self.output_data.append(filtered)
        self.index_counter += 1
        return ascii(f"#{self.index_counter - 1}: {filtered}")

    def Count(self, index_provided = None):
        """ Counts the number of occurences found for a token. """
        try:
            index_provided = int(index_provided)
        except (ValueError, TypeError):
            index_provided = -1
        data = self.output_data[index_provided]
        return ascii(f"{len(data)}")

    def __repr__(self):
        lst_obj = str(self.output_data[:10]).strip(']') + ' ...]'
        return ascii(f"<class REPL: REPL({lst_obj}), length: {self.index_counter}>")

#try:
code.interact(banner="Start:\nObject to interact with -> repl_obj",
		  readfunc = readfunc, local=locals(), exitmsg="End")