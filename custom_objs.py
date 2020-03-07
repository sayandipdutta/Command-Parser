from contextlib import suppress
from collections import namedtuple

class REPL:
    """Creates a REPL object, with some methods"""
    output_dict = {}
    func_dict = {}
    history = namedtuple('last', 'output command')
    last_output = history(None, None)
    index_counter = 0

    @classmethod
    def Open(cls, filename=None):
        """ Opens the provided file, appends the file object to
            cls.output_data, increments the index_counter """
        # breakpoint()
        if not filename:
            filename = cls.output_dict.get(-1, cls.last_output.output)

        with suppress(FileNotFoundError):
            fileobj = open(filename)
            data = fileobj.read()
            fileobj.close()
            return data

    @classmethod
    def Filter(cls, token, data_provided=None):
        """ Filters the specified token from the file object. """
        # breakpoint()
        if data_provided:
            data = data_provided
        else:
            data = cls.output_dict.get(-1, cls.last_output.output)
        
        filtered = [line for line in data.split('\n') if token in line]
        return filtered

    @classmethod
    def Count(cls, data_provided=None):
        """ Counts the number of occurences found for a token. """
        if not data_provided:
            data = REPL.output_dict.get(-1, REPL.last_output.output)
        else:
            data = data_provided
        print(len(data))
        return len(data)

    @classmethod
    def __repr__(cls):
        lst_obj = str(cls.output_dict).strip('}')[:10] + ' ...}'
        return ascii(f"<class REPL: REPL({lst_obj}), length: {cls.index_counter}>")

def lambda_def(statement, funcname):
    func = eval("lambda " + statement)
    setattr(REPL, funcname, func)
    
    
