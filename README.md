# Command-Parser
A functional programming interface in Python, that closely resembles python REPL.

# Usage
After running the code, the program starts in interactive more:
```
$ python3 parser_2.py
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```
Program is written based on python Standard Library module `code`. This basically works somewhat like LISP. Where the idea is, a statement is `operator :-> operand`, meaning that `operator` is on the left, and `operand(s)` are on the right. Methods can be chained together, or nested (currently not supported). 
## Example:
Some sample commands for data analysis purposes would be
```
>>> Open "file.txt", Filter "some-token", Count
10
>>> Filter "some-other-text" 0
>>> print
['some-other-text,1', 'some-other-text2']
>>> Count 3
2
```
## Explanation:
```
>>> Open "file.txt", Filter "some-token", Count
     (0)    (0')      (1)      (1')        (2)
     
# Here three functions are called, 1. Open, 2. Filter, 3. Count (All user-definer), and each functions output are appended to a call variable implicitly, in the same order as they are executed. Each function receive the output of the previous function. Out of these, only Count prints an output on the console. 1', 2' are operands, and Count does not take any argument. 
>>> Filter "some-other-text" 0
      (3)        (3')       (3')
      
# Again the operator here is 3, and it took two arguments 3's. Second argument suggests, that instead of calculating on the last output stored in stack, access the output stored in provided index (0 in this case).
>>> print
     (4*)
['some-other-text,1', 'some-other-text2']

Here `print` is the default Python print, if no argument is provided, as is the case here, it takes the previous output as expression. Here output refers to the last value the last statement evaluated to. The user defined function `Filter` returns a `list` so, `print` printed the list.
>>> Count 3
     (5) (5')
2
Count does not need an argument, however, as there are argument passed, it will treat the argument as the index of the output list, and get that element, and operate on that. `3` suggests it asks Count to operate on the `3`rd index output, i.e. the list that was updated due to the last `Filter` command. Which gives 2.

