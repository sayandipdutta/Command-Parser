# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:21:17 2020

@author: Administrator
"""
from itertools import accumulate
import operator
import code
from functools import lru_cache
import pdb
import sys

def recur(*args):
	return ((not len(funcs)) and args) or recur(funcs.pop(0)(args))


class REPLfunc:
	def __init__(self):
		self.output = []
		self.count = None

	def Open(self,filename):
		if filename:
			self.output.append(('Open', open(filename)))
			return ascii(f"File opened: {filename}")
		else:
			raise TypeError("Filter expects exactly 1 argument.")


	def Filter(self,token):
		prev_out = self.output[-1][1]
		if token:
			filtered = [line.strip() for line in prev_out
					   if token in line]
			prev_out.close()
			self.output.append(('Filter', filtered))
			self.count = len(filtered)
			return ascii(f"{type(filtered)}")
		else:
			prev_out.close()
			raise TypeError("Filter expects exactly 1 argument.")

	def Count(self, index = None):
		if index:
			output = len(self.output[int(index)][1])
		else:
			output = len(self.output[-1][1])
		self.output.append(('Count', output))
		return ascii(f"{output}")



repl_obj = REPLfunc()
fallback = False
def readfunc(prompt):
	global fallback
	inp = code.InteractiveConsole().raw_input(prompt=">>> ")
	if inp == 'fallback':
		fallback = True
	args = inp.split()
	if fallback:
		code.InteractiveConsole().interact(banner="fallingback to native REPL", exitmsg="End")
	elif len(args) == 1:
		try:
			func = getattr(repl_obj, inp.strip())
			exec('func()')
		except (TypeError, AttributeError):
			return ascii(eval(inp))

	elif len(args) > 1:
		method, params = inp.split()
		func = getattr(repl_obj, method)
		output = func(params)
		return output


	return args

#try:
code.interact(banner="Start:\nObject to interact with -> repl_obj",
		  readfunc = readfunc, local=locals(), exitmsg="End")
#except TypeError:
#	code.interact(banner="",local=locals(), exitmsg="End")

#def Sum(args):
#	*_, elems = args
#	return sum(elems)
#
#def Subtract(args):
#	return list(accumulate(list(args), operator.sub))
#
#def AreaOfCircle(arg):
#	*_, r = arg
#	return 2*3.14*r**2
#
#funcs = [Subtract, Sum, AreaOfCircle]
#func_iter = iter(funcs)
#
#
##def recur(*args, func=func_iter):
##	try:
##		return recur(next(func_iter)(args))
##	except StopIteration:
##		return args
##
##print(recur(1,4,2,4,5,func=func_iter))
#
##@lru_cache(maxsize = 1000)
#
#code.interact(banner="Start", local=locals(), exitmsg="End")



