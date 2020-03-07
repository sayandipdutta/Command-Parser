# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:33:37 2020

@author: Administrator
"""
import pandas as pd

INFILE = 'data.txt'

strikes = []
call_pos, put_pos = [], []

with open(INFILE) as f:
	for line in f:
		if not line.startswith('#') and line.strip():
						 contents = line.strip().split(',')
flag = False
for ix, field in enumerate(contents):
	if 'PE' in field:
		strikes.append(field[-7:-2])
		call_pos.append(contents[ix + 2])
		put_pos.append(contents[ix + 3])

#print(strikes,call_pos, put_pos, sep = '\n')
df = pd.DataFrame({'strikes':strikes, 'call_pos': call_pos, 'put_pos':put_pos})
print(df)
df.sort_values('strikes', inplace=True)
df.to_csv('positions.csv', index=False)
