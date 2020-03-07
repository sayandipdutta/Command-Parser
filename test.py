# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 11:31:19 2020

@author: Administrator
"""

import numpy as np
from pprint import pprint
from collections import defaultdict
import builtins

f0 = lambda:0
f1 = lambda:1
f2 = lambda:2
f3 = lambda:3
f4 = lambda:4


line = '{(1, 2): {3: [4, (5, {6, "7"}), #f1, 8], 9: ^10}}, [(#f2, ^2), #f3], #f4'
line_list = list(line)
arr = np.array([ord(char) for char in line])
types_ = {(123, 125, '{', '}'): 'dict/set', (91, 93, '[', ']'): 'list',
		  (40,41, '(', ')'): 'tuple', (34,None,'"', None): 'str',
		  (35,None,'#',None): 'func', (94,None,'^', None): 'index'}

types_ = {(35,None,'#',None): 'func', (94,None,'^', None): 'index'}

d = defaultdict(list)
new_dict = {}
for strt, end, s1, s2 in types_:
	if s1 == '#':
		opens = np.where(arr == strt)[0]
		for o in opens:
			for ix,char in enumerate(line[o+1:]):
				if not char.isalpha() and char != '.' and not char.isnumeric()  or (ix == len(line[o+1:]) -1):
					if (ix == len(line[o+1:]) -1):
						c = o + ix + 2
						d['func'].append(((o,c), line[o:]))
					else:
						c = o + ix + 1
						d['func'].append(((o,c), line[o:c]))
					break


	elif s1 == '^':
		opens = np.where(arr == strt)[0]
		for o in opens:
			for ix,char in enumerate(line[o+1:]):
				if not char.isnumeric()  or (ix == len(line[o+1:])-1):
					if (ix == len(line[o+1:])-1):
						c = o + ix + 2
						d['index'].append(((o,c), line[o:]))
					else:
						c = o + ix + 1
						d['index'].append(((o,c), line[o:c]))
						break



pprint(new_dict)



for key, val in d.items():
	for match in val:
		(strt, stp), obj = match
		obj = obj[1:]
		l = len(obj)
#		breakpoint()
		rest = ['']*l
		print(line[strt:stp], line_list[strt:stp])
		if key == 'func':
			if obj in globals():
				line_list[strt: stp] = ([f'globals()["{obj}"]'] + rest).copy()
			elif obj in dir(builtins):
				line_list[strt: stp] = ([f'getattr(builtins, "{obj}")'] + rest).copy()
		elif key == 'index':
			line_list[strt:stp] = ([f'line_list[{obj}]'] + rest).copy()



print(''.join(line_list))
print(eval(''.join(line_list)))




#def func_idx(line):
#	ix = 1
#	temp = ''
#	while line[ix] != ' ':
#		temp += line[ix]
#		ix += 1
#	if line[0] == '#':
#		if temp in globals():
#			return globals()[temp]
#		elif temp in dir(builtins):
#			return getattr(builtins,temp)
#	else:
#		return int(temp)
#
#def func(start, stop, type_):
#	if type_ == 'str':
#		return line[start+1 : stop]
#	else:
#		if type_ == 'dict':
#			d = {}
#			temp = ''
#			for char in line[start+1 : stop]:
#				if not char != '"' and char in

#for strt, end, s1, s2 in types_:
#	if not end is None:
#		found = []
#		opens = np.where(arr == strt)[0]
#		closes = np.where(arr == end)[0]
#		for o in opens:
#			for c in closes:
#				if line[o+1:c].count(s1) == line[o+1:c].count(s2) and c > o:
#					found.append((o, c))
#					break
#		for o, c in found:
#			if strt == 123:
#				if ':' in line[o:c]:
#					key = ['dict', line[o:c+1]]
#				else:
#					key = ['set', line[o:c+1]]
#			else:
#				key = [types_[(strt, end, s1, s2)], line[o:c+1]]
#			new_dict[(o,c)] = key
#	else:
#		if s1 == '"':
#			opn_clos = np.where(arr == strt)[0]
#			opens = opn_clos[::2]
#			closes = opn_clos[1::2]
#			for o, c in zip(opens, closes):
#				key = 'str'
#				new_dict[(o,c)] = [key, line[o:c+1]]
#		elif s1 == '#':
#			opens = np.where(arr == strt)[0]
#			for o in opens:
#				for ix,char in enumerate(line[o+1:]):
#					if not char.isalpha() and char != '.' and not char.isnumeric()  or (ix == len(line[o+1:]) -1):
#
#
#						if (ix == len(line[o+1:]) -1):
#							c = o + ix + 2
#							new_dict[(o,c)] = ['func', line[o:]]
#							d['func'].append(((o,c), line[o:]))
#						else:
#							c = o + ix + 1
#							new_dict[(o,c)] = ['func', line[o:c]]
#							d['func'].append(((o,c), line[o:c]))
#						break
#
#
#		elif s1 == '^':
#			opens = np.where(arr == strt)[0]
#			for o in opens:
#				for ix,char in enumerate(line[o+1:]):
#					if not char.isnumeric()  or (ix == len(line[o+1:])-1):
#
#						if (ix == len(line[o+1:])-1):
#							c = o + ix + 2
#							new_dict[(o,c)] = ['index', line[o:]]
#							d['index'].append(((o,c), line[o:]))
#						else:
#							c = o + ix + 1
#							new_dict[(o,c)] = ['index', line[o:c]]
#							d['index'].append(((o,c), line[o:c]))
#						break
