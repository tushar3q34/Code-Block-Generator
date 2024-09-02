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
        return

    match = re.search("[^ ]+ (integers|numbers) [^ ]+ ", line)
    if match is None:
        return

    var_details = match.group().split()
    qty = var_details[0].strip('$')
    try:
        qty = int(qty)
    except ValueError:
        try:
            qty = text_numbers[qty]
        except KeyError:
            pass
    name = var_details[2].strip(',$')

    match = re.search(".*_", name)
    if match is not None:
        name = match.group()[:-1]
    return Variable("int[{}]".format(qty), name)


def check_str(line):
    is_str=re.search(".*string.*", line)
    is_strs=re.search(".*strings.*", line)
    if is_str and not is_strs :
        return Variable("string","str")
    elif is_strs :
        fix_num
        is_num = False
        for num in text_numbers :
            if re.search(".*"+num+".*", line) :
                is_num = True
                fix_num = num
                break
        if not is_num :
            pattern = r".*\s(?=lines)"
            match = re.search(pattern, line)
            result = match.group(1).split()[-1][1:-1]
            return Variable("string[{}]".format(result),"str")
        else :
            return Variable("string[{}]".format(text_numbers[fix_num]),"str")
    else :
        return


all_fxns = (check_array, check_str#, check_integer
            ,)


# Function to make all the necessary checks
def check_all(para):
    para = re.sub(r"\." + " |\n|\n\n", "\n", para)
    lines = para.split('\n')
    all_data = []
    for line in lines:
        for check in all_fxns:
            op = check(line)
            if op is not None:
                try:
                    all_data.append(*op)
                except TypeError:
                    all_data.append(op)
                break
    for v in all_data:
        print(v.datatype, v.name)