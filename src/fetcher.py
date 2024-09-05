from scraper import *

path = "src/test_cases/"
def write_file(file_name,code_str):
    with open(file_name,"w") as f:
        f.write(code_str)
    f.close()


prob = input("Enter problem name, Eg: 1980G: ")
p = Problem(prob[:4],prob[4])
content = "".join(p.input) + "@"
for test in p.tests:
    content += test.input + "@"
write_file(path+prob+".txt",content)

def fetch(prob):
    try:
        p = Problem(prob[:4],prob[4])
        input_string = "".join(p.input)
        tests = [test.input for test in p.tests]
    except:
        with open(path + prob + ".txt",'r') as f:
            s = f.read().split("@")
            input_string = s[0]
            tests = s[1:]
        return input_string,tests
