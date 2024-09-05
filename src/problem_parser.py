# This file contains all the functions to parse the input string

from scraper import *


class Variable:
    """Class for a variable (of type int, bool, array, double, string, etc.)

    Attributes
    ----------
    datatype_cpp : str
        String representation of the data type of the variable in C++
        Eg: "string", "bool", "int[n]" (for array)
    datatype_py : str
        String representation of the data type of the variable in Python
        Eg: "string", "bool", "int[n]" (for array)
    name : str
        Name of the variable
    """

    def __init__(self, datatype_cpp, datatype_py, name):
        self.datatype_cpp = datatype_cpp
        self.datatype_py = datatype_py
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


def ignore(line):
    if "number of test cases" in line:
        return True
    if "sum" in line and "across all test cases" in line:
        return True
    if "sum" in line and "over all test cases" in line:
        return True
    if "if" in line and "then" in line:
        return True
    return False


# Function to check a line of input for the presence of an array
def check_array(line):
    match = re.search("[^ ]+ (integers|numbers) [^ ]+ ", line)
    if match is None:
        return

    if re.search("_", match.group()) is None:
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
    return Variable("int[{}]".format(qty), "int[{}]".format(qty), name)


def check_str(line):
    is_str=re.search(".*string.*", line)
    is_strs=re.search(".*strings.*", line)
    if is_str and not is_strs :
        return Variable("string", "str", "s")
    elif is_strs :
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
            return Variable("string[{}]".format(result), "str[{}]".format(result), "s")
        else :
            return Variable("string[{}]".format(text_numbers[fix_num]), "str[{}]".format(text_numbers[fix_num]), "s")
    else :
        return


def check_matrix(line):
    is_matrix = re.search(".*lines.*(numbers|integers)",line)
    if is_matrix:
        result = line.split("lines")
        num1 = result[0].split()[-1][1:-1]
        return_val = check_array(result[1])
        num2 = return_val.datatype_cpp[4:-1]
        arr = return_val.name
        return Variable("int[{}][{}]".format(num1,num2), "int[{}][{}]".format(num1,num2), arr)
    else:
        return


# Function to check a line of input for the presence of an array
def check_integer(line):
    target_string = line
    res = re.search("[^ ]+ (integer|number) ", target_string)

    if res is not None:
        target_string = target_string[res.span()[1]:]
        if target_string[0:2] == "of" and res.group().split()[1] == "number":
            res = None
            target_string = line

    if res is not None:
        index = res.group().split()
        search_string = re.search("[^ ]*", target_string)
        var_detail = search_string.group().split()
        name = var_detail[0].strip('$.')

        return Variable("int", "int", name)

    else:
        res2 = re.search("[^ ]+ (integers|numbers) ", target_string)

        if res2 is None:
            return

        var = res2.group().split()
        num2 = var[0].strip('$')
        target_string = target_string[res2.span()[1]:]

        try:
            num2 = int(num2)
        except ValueError:
            try:
                num2 = text_numbers[num2]
            except KeyError:
                print("call check_array")  # call check_array
                return

        l = []
        x = 0
        while x < num2:
            flag = 0
            if x < num2 - 2:
                search_name = re.search("[^ ]*, ", target_string)
            elif x == num2 - 2:
                search_name = re.search("[^ ]* and ", target_string)
                flag = 1
            elif x == num2 - 1:
                search_name = re.search("[^ ]*", target_string)
                flag = 2

            if search_name is None:
                print("Error")
            else:
                var_detail = search_name.group().split()
                if flag == 0:
                    name = var_detail[0].strip("$,")
                elif flag == 1:
                    name = var_detail[0].strip("$")
                else:
                    name = var_detail[0].strip("$.")
                l.append(name)

            target_string = target_string[search_name.span()[1]:]
            x = x + 1

        obj = []

        for y in l:
            obj.append(Variable("int", "int", y))

        return obj


# IMPORTANT : Priority order is decided here
all_fxns = (check_matrix,
            check_array,
            check_str,
            check_integer,
            )


# Function to make all the necessary checks
def check_all(para):
    para = re.sub(r"\." + " |\n|\n\n", "\n", para)
    lines = para.split('\n')
    all_data = []
    for line in lines:
        if ignore(line):
            continue
        for check in all_fxns:
            op = check(line)
            if op is not None:
                try:
                    all_data.extend(op)
                except TypeError:
                    all_data.append(op)
                print(check)
                break
    return all_data
