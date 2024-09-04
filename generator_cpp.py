start_cpp = '''#include <bits/stdc++.h>

using namespace std;

void solve(){
'''

end_cpp_single = '''
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    solve();
}'''

end_cpp_t = '''
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t;
    cin >> t;
    while (t--){
        solve();
    }
}'''


def input_var_cpp(encoding):
    c = encoding.datatype_cpp.count('[')
    inp = ''
    if c == 0:
        inp += "    " + encoding.datatype_cpp + ' ' + encoding.name + ";\n"
        inp += "    " + "cin >> " + encoding.name + ";\n"
    else:
        ind = encoding.datatype_cpp.find('[')
        inp += "    " + encoding.datatype_cpp[:ind] + ' ' + encoding.name + encoding.datatype_cpp[ind:] + ";\n"
        lims = [x for x in encoding.datatype_cpp[ind:][1:-1].split('][')]
        for i in range(c):
            line = "    " + "for (int {it} = 0; {it} < {lim}; {it}++){{\n".format(it=chr(ord('i') + i), lim=lims[i])
            for j in range(i):
                inp += "    "
            inp += line
        for i in range(c):
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


def full_code_cpp(all_data, t=True):
    code = start_cpp
    for var in all_data:
        code += input_var_cpp(var)
    if t:
        code += end_cpp_t
    else:
        code += end_cpp_single
    return code
