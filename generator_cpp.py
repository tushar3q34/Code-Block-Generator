start_cpp = '''#include <bits/stdc++.h>

using namespace std;

void solve(){
'''

end_cpp = '''
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
}'''


def looper(string, i, c, inp_stmt):
    if c == 0:
        string += inp_stmt
        return string


def input_var_cpp(encoding):
    c = encoding.datatype.count('[')
    inp = ''
    if c == 0:
        inp += "    " + encoding.datatype + ' ' + encoding.name + ";\n"
        inp += "    " + "cin >> " + encoding.name + ";\n"
    else:
        ind = encoding.datatype.find('[')
        inp += "    " + encoding.datatype[:ind] + ' ' + encoding.name + encoding.datatype[ind:] + ";\n"
        lims = [x for x in encoding.datatype[ind:][1:-1].split('][')]
        for i in range(c):
            line = "    " + "for (int {it} = 0; {it} < {lim}; {it}++){{\n".format(it=chr(ord('i') + i), lim=lims[i])
            for j in range(i):
                inp += "    "
            inp += line
        for i in range(c + 1):
            inp += "    "
        indexing = ''
        for i in range(c):
            indexing += '[' + chr(ord('i') + i) + ']'
        inp += "    " + "cin >> " + encoding.name + indexing + ";\n"
        for i in range(c):
            for j in range(c - i - 1):
                inp += "    "
            inp += "    " + "}\n"
    return inp


def full_code_cpp(all_data):
    code = start_cpp
    for var in all_data:
        code += input_var_cpp(var)
    code += end_cpp
    return code
