import builtins
import numpy as np
from pprint import pprint
from collections import namedtuple, defaultdict

from custom_objs import *

globals()['Self'] = REPL.output_dict

def method_getter(func):
    """Get method from an object/class"""
    objs = func.split('.')
    func = func_getter(objs[0])
    for method in objs[1:]:
        func = getattr(func, method)
    return func

def func_getter(func):
    """Retrieve function from globals namespace"""
    if '.' in func:
        return method_getter(func)
    if func in globals():
        return globals()[func]
    elif func in dir(builtins):
        return getattr(builtins, func)
    elif func in dir(REPL):
        return getattr(REPL, func)
    else:
        if not func:
            return None
        raise NameError(f"Name {func} is not defined.")


def arg_parser(line: str):
    """Parse argument provided, and evaluate the arguments,
    as python code. """
    # breakpoint()
    
    if not line:
        return ()
    else:
        line = line[0]
    line_list = list(line)
    arr = np.array([ord(char) for char in line])
    types_ = {(35, '#'): 'func', (94, '^'): 'index'}

    d = defaultdict(list)

    for strt, s1 in types_:
        if s1 == '#':
            opens = np.where(arr == strt)[0]
            for o in opens:
                for ix, char in enumerate(line[o+1:]):
                    if not char.isalpha() and char != '.' and not char.isnumeric() or (ix == len(line[o+1:]) - 1):
                        if (ix == len(line[o+1:]) - 1):
                            c = o + ix + 2
                            d['func'].append(((o, c), line[o:]))
                        else:
                            c = o + ix + 1
                            d['func'].append(((o, c), line[o:c]))
                            break

        elif s1 == '^':
            opens = np.where(arr == strt)[0]
            for o in opens:
                for ix, char in enumerate(line[o + 1:]):
                    # breakpoint()
                    if (not char.isnumeric() and char != '-') or (ix == len(line[o+1:])-1):
                        if (ix == len(line[o+1:])-1):
                            c = o + ix + 2
                            d['index'].append(((o, c), line[o:]))
                        else:
                            c = o + ix + 1
                            d['index'].append(((o, c), line[o:c]))
                            break

    for key, val in d.items():
        for match in val:
            (strt, stp), obj = match
            obj = obj[1:]
            l = len(obj)
            breakpoint()
            rest = ['']*l
            if key == 'func':
                if obj in globals():
                    line_list[strt: stp] = (
                        [f'globals()["{obj}"]'] + rest).copy()
                elif obj in dir(builtins):
                    line_list[strt: stp] = (
                        [f'getattr(builtins, "{obj}")'] + rest).copy()
                elif obj in dir(REPL):
                    line_list[strt: stp] = (
                        [f'getattr(REPL, "{obj}")'] + rest).copy()
                elif '.' in obj:
                    line_list[strt: stp] = (
                        [obj] + rest).copy()
            elif key == 'index':
                line_list[strt:stp] = (
                    [f'REPL.output_dict.get({obj}, REPL.last_output)'] + rest).copy()

    new_line = ''.join(line_list)
    return eval(new_line)
