import time
import re
from collections import OrderedDict


def read_File():
    code = []
    f = open("PythonCode.py", "r")
    raw_Code = f.readlines()
    for i in raw_Code:
        if i != '\n' and i != '':
            code.append(i[0:-1])
    return code

try:
    complex_Alterations = OrderedDict()
    complex_Alterations = {
        'False': 'False', 'None': 'None', 'True': 'True', ' and ': '(and)', 'as': 'as', 'assert': 'assert', 'async': 'async', 'await': 'await', 'break': 'Break the flow of code', 'class': 'Define a class', 'continue': 'Break this iteration of code', 'def': 'Define a funtion', 'del': 'del', 'elif': 'Otherwise if', 'else:': 'Otherwise', 'except': 'except', 'finally': 'finally', 'for': 'Initiate a for loop with variable', 'from': 'from', 'global': 'Define a global variable', 'if': 'Check whether ', 'import': 'Import a module named ', 'in': 'in', ' is ': ' is ', 'lambda': 'lamda', 'nonlocal': 'nonlocal', ' not ': 'not', ' or ': '(or)', 'pass': 'pass', 'raise': 'raise', 'return': 'Return ', 'try': 'Try', 'while': 'Initiate a while loop with condition', 'with': 'with'
    }
    arithmetic_Alterations = OrderedDict()
    arithmetic_Alterations = {
        '==': 'is equal to',
        '>=': 'greater than or equal to',
        '<=': 'lesser than or equal to',
        '++': 'increment by 1',
        '--': 'decrement by 1',
        ' > ': ' greater than ',
        ' < ': ' lesser than ',
        ' = ': ' is equal to ',


    }
    higher_Order_Alterations = OrderedDict()
    higher_Order_Alterations = {
        'print(': 'Display the following in the console (',
        'len(': 'Length of (',
        'range(': 'range of (',
        'round(': 'Round it to ('
    }
    ignore_Elements = ['']


    Code = read_File()

    Algorithm = ['START']
    for code_Line in Code:
        
        if '#' in code_Line:
            code_Line = code_Line[0:code_Line.index('#')]


        if 'input(' in code_Line and 'print(' not in code_Line:
            code_Line = 'Accept a variable ' + \
                code_Line[code_Line.index(re.search('\w', code_Line).group()):code_Line.index(' = ')]+' from user'

        else:
            for key in higher_Order_Alterations:
                if key in code_Line:

                    code_Line = code_Line.replace(
                        key, higher_Order_Alterations[key])
            for key in complex_Alterations:
                if key in code_Line:

                    code_Line = code_Line.replace(key, complex_Alterations[key])
            for key in arithmetic_Alterations:
                if key in code_Line:

                    code_Line = code_Line.replace(key, arithmetic_Alterations[key])
        if len(code_Line)==0:
            continue
        if code_Line[-1] == ':':
            code_Line = code_Line[0:-1]
        if code_Line[0] == ' ':
            Algorithm[-1] = Algorithm[-1]+'\n\t'+code_Line
        else:
            Algorithm.append(code_Line)


    with open('Algorithm.txt', 'w') as f:
        for i in range(1, len(Algorithm)+1):
            f.write("STEP"+str(i)+": "+str(Algorithm[i-1]))
            f.write('\n')
        f.write("STEP"+str(len(Algorithm)+1)+": STOP")
except Exception as e:
    print(e)
    with open('Algorithm.txt', 'w') as f:
        f.write(str(e))

