start_py = '''from collections import deque

input_buffer = deque()
def cin():
    if input_buffer:
        return input_buffer.popleft()
    else:
        input_buffer.extend(input().split())
        return input_buffer.popleft()


def solve():
'''

end_py_single = '''

solve()

'''

end_py_t = '''

for tc in range(int(input())):
    solve()

'''


def input_var_py(encoding):
    c = encoding.datatype_py.count('[')
    inp = ''
    if c == 0:
        inp += "    " + encoding.name + " = " + encoding.datatype_py + "(cin())"
    else:
        ind = encoding.datatype_py.find('[')
        lims = [x for x in encoding.datatype_py[ind:][1:-1].split('][')]
        inp += "    " + encoding.name + " = "
        for i in range(c):
            inp += "["
        inp += "None "
        for i in range(c):
            inp += "for {it} in range({lim})] ".format(it=chr(ord('i') + c - i - 1), lim=lims[c - i - 1])
        inp += '\n'
        for i in range(c):
            line = "    " + "for {it} in range({lim}):\n".format(it=chr(ord('i') + i), lim=lims[i])
            for j in range(i):
                inp += "    "
            inp += line
        for i in range(c):
            inp += "    "
        indexing = ''
        for i in range(c):
            indexing += '[' + chr(ord('i') + i) + ']'
        inp += "    " + encoding.name + indexing + " = " + encoding.datatype_py[:ind] + "(cin())" + "\n"
    return inp


def full_code_py(all_data, t=True):
    code = start_py
    for var in all_data:
        code += input_var_py(var)
    if t:
        code += end_py_t
    else:
        code += end_py_single
    return code
