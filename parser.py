#!/home/sayandip199309/anaconda3/envs/tensorflow_gpu/bin/python

import sys
import os
import code
import itertools
import collections
from contextlib import suppress

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
            self.output_data.append(fileobj)
            self.index_counter += 1
            return (f"#{self.index_counter - 1}: {self.fileobj!r}")

    def Filter(self, token, index_provided = None):
        """ Filters the specified token from the file object. """
        try:
            index_provided = int(index_provided)
        except (ValueError, TypeError):
            index_provided = -1
        data = self.output_data[index_provided]
        filtered = [line.strip() for line in data if token in line]
        self.output_data.append(filtered)
        self.index_counter += 1
        return (f"#{self.index_counter - 1}: {filtered}")

    def Count(self, index_provided = None):
        """ Counts the number of occurences found for a token. """
        try:
            index_provided = int(index_provided)
        except (ValueError, TypeError):
            index_provided = -1
        data = self.output_data[index_provided]
        return len(data)

    def __repr__(self):
        lst_obj = str(self.output_data[:10]).strip(']') + ' ...]'
        return f"<class REPL: REPL({lst_obj}), length: {self.counter}>"

keywords = [method for method in dir(REPL) if not method.startswith('__')]

def readfunc(prompt):
    inp = code.InteractiveConsole().raw_input(prompt)



        



            

