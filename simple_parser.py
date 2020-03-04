from collections import namedtuple

def find_strings(line: str, strings: list = []) -> list:
    breakpoint()
    start = line.find('"')
    if start == -1:
        return strings
    else:
        rest = line[start + 1:]
        end = rest.find('"')
        string = f'"{line[start + 1:start + 1 + end]}"'
        strings.append(string)
        return find_strings(line=line[start + 1 + end + 1:],
                            strings=strings)

def arg_parse(line: str) -> list:
    allowed_punct = '\'",;.()[]{}#^'
    start_dict = {'"': ('"', 'str'), '^': (' ', 'index'),
                    '(': (')', 'tuple'), '[': (']', 'list'),
                    '{': ('}', 'collection'), '#': (' ', 'custom')}

    custom_object = False
    temp = ''
    for char in line:
        if char in start_dict:
            flag = start_dict[char][1]
            if flag == 'str':
                if char != start_dict[char][0]
                    temp += char
                else:
                    master_list.append(temp + '"')
                    temp = ''
                
            elif flag == index:
                
    open_literals = '([{#'
    master_list = []
    temp_ = ''
    
    for char in line:
        if char not in allowed_punct and not custom_object:
            if char != ' ':
                temp_ += char
            else:
                if char == 
                try:
                    arg = int(temp_)
                except ValueError:
                    arg = float(temp_)
                master_list.append(arg)
                temp_ = ''
        elif char in allowed_punct and custom_object:
            raise SyntaxError("int or float type objects can not ")
        else:
            custom_object = True
            if 

def arg_splitter(command: str) -> list:
    func, rest = command.split(" ", 1)
    args = []
    str_start = False
    arg = namedtuple('token', 'value type')
    first_str_strt = rest.find('"')
    # if first_str_strt == -1:
    #     pass
    # else:




    
    

# while 1:
#     line = input("\n>>> ")
#     commands = line.split(';')
    
