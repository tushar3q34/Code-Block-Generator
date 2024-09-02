# This file contains all the functions to parse the input string

from scraper import *


class Variable:
    """Class for a variable (of type int, bool, array, double, string, etc.)

    Attributes
    ----------
    datatype : str
        String representation of the data type of the variable
        Eg: "string", "bool", "int[n]" (for array)
    name : str
        Name of the variable
    """

    def __init__(self, datatype, name):
        self.datatype = datatype
        self.name = name


class Wrapper:
    """Class for a loop including repetitive input

    Attributes
    ----------
    iterations : int
        Number of times the outer loop runs in the wrapper
    *enclosed : tuple of Wrapper and/or Variable objects
        Everything enclosed in the outer loop's body
    """

    def __init__(self, iterations, *enclosed):
        self.iterations = iterations
        self.enclosed = enclosed


# Useful where questions might use words instead of digits for small numbers
text_numbers = {"one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
                "ten": 10}


# Function to check a line of input for the presence of an array
def check_array(line):
    if re.search("_", line) is None:
        print(1)
        return

    match = re.search("[^ ] integers|numbers [^ ]", line)
    if match is None:
        print(2)
        return

    var_details = match.group().split()
    print(var_details)
    qty = var_details[0].strip('$')
    try:
        qty = int(qty)
    except ValueError:
        try:
            qty = text_numbers[qty]
        except KeyError:
            pass
    name = var_details[-1].strip(',$')

    name = re.search(".*_", name).group()[:-1]
    return Variable("int[{}]".format(qty), name)


s = [#'''The first line contains a single integer $t$ ($1$ $\\le$ $10^4$) - the number of test cases.''',
'''The only line of each test case contains $n$ integers $a_1$, $a_2$, $...$, $a_n$ ($1$ $\\le$ $l$ $\\le$ $r$ $\\le$ $10^9$).''']
for x in s:
    v = check_array(x)
    if v is not None:
        print(v.datatype, v.name)
