from collections import namedtuple, defaultdict

import builtins
from contextlib import suppress
from pprint import pprint
from collections.abc import Iterable
import sys
import pdb
from simple_parser import *
import time
import traceback

def run_commands(line: str) -> list:
    commands = line.split(';')
    for command in commands:
        func, *rest = command.strip().split(" ", 1)
        func, args = func_getter(func), arg_parser(rest)
        if func is None: return

        if isinstance(args, tuple):
            op = func(*args)

        else:
            op = func(args)

        if not op is None:
            REPL.last_output = REPL.history(op, func.__name__)
            REPL.output_dict[REPL.index_counter] = REPL.last_output.output
            REPL.func_dict[REPL.index_counter] = REPL.last_output.command
            while len(REPL.output_dict) > 5:
                del REPL.output_dict[REPL.index_counter - 5]
            REPL.index_counter += 1



def main():
    prompt = """
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    """
    instructions = """
    1. Statements are of form: <func> <arguments>.
    2. When multiple statements need to be executed, each statement must be
    delimited with ';'.
    3. Functions passed as parameters must be prepended with '#'.
    4. To access indices of the stored output, indices must be prepended with '^'.
    """
    example = """
    Example:
    1.
    func_to_call arg1, arg2, ^index, #func_as_arg
    2.
    print #square ^2
    3.
    count 10; print ^-1
    """
    print(prompt, instructions, example, sep = '\n')

    # Start REPL
    while 1:
        try:
            inp = input(" >>> ")
            if inp in ['q', 'quit', 'quit()', '^D']:
                print("Exiting Interactive Console.")
                break
            run_commands(inp)
        
        except EOFError:
            print("Exiting Interactive Console.")
            break
        
        except Exception as error:
            print(f"{error.__class__.__name__}:",*error.args)
            print(traceback.format_exc())

if __name__ == '__main__':
    main()
