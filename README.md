
# Algorithm Generator

This basic code will let you change your python code into its basic Algorithm form.

#### For example:
##### Python code for Pascals Triangle:


```
# Print Pascal's Triangle in Python
from math import factorial
 
# input n
n = 5
for i in range(n):
    for j in range(n-i+1):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
 
    # for new line
    print()
```
##### The following Algorithm made by the AI will be:
```
STEP1: START
STEP2: from math Import a module named  factorial
STEP3: n is equal to 5
STEP4: Initiate a for loop with variable i in range of (n)
	    Initiate a for loop with variable j in range of (n-i+1)
	        
	        Display the following in the console (end=" ")
	    Initiate a for loop with variable j in range of (i+1)
	        
	        Display the following in the console (factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	    
	    Display the following in the console ()
STEP5: STOP
```
## Installation

To install this project on your computer, run this code in the terminal of your directory (make sure you have git installed on your computer)

```bash
    git clone https://github.com/harshj3915/AlgorithmGenerator.git

```
    
## How to Start

- Firstly make sure `Main.py` , `PythonCode.py` and `Algorithm.txt` are in the same directory
- Paste your python code in the `PythonCode.py`
- Make sure to format the python code in the `PythonCode.py` before running `Main.py`
    - **Its important to format the code with a proper python formatter as the AI only works on the formatted version of the code.**
    - FAQs about **formatting** are in the [FAQ section](#faq)
- Run `Main.py`
- Algorithm will be generated in `Algorithm.txt`
- If you find any bugs or issues please feel free to post in [Issue Thread](https://github.com/harshj3915/AlgorithmGenerator/issues) or [request to push](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) the improved/updated version of the code.

## FAQ

#### **I use Python IDLE how do i format my code?**

Use this [Online Formatter for Python](https://codebeautify.org/python-formatter-beautifier) to format your code online.

#### **How to format code in Spyder?**

Simply go to Tools > Preferences then choose Completion and linting > Code style and formatting . There, toggle on Enable code style linting and Autoformat files on save . Now when you save your file, Spyder will beautify your code, when it can infer what to do.

#### **How to format code in Visual Studio Code?**

VS Code has great support for source code formatting. The editor has two explicit format actions: Format Document (Ctrl+Shift+I) - Format the entire active file. Format Selection (Ctrl+K Ctrl+F) - Format the selected text.

#### **How to format code in Pycharm?**

Either open your file in the editor and press Ctrl+Alt+Shift+L or in the Project tool window, right-click the file and select Reformat Code.


## Authors

- [@Harsh Kothari](https://github.com/harshj3915)

