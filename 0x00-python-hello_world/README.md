# 0x00. Python - Hello, World

## Zen 

### The Zen of Python, by *Tim Peters*

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


## Task 0. Run Python file
 
 Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE
```shell
 guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```
 
## Task 1. Run inline
 Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE
 
```shell
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$  
```
 
## Task 2. Hello, print
 Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
 
```shell
 guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```
 
## Task 3. Print integer
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings tips 
 
```shell
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$  
```
 
  ## Task 
 
 
 ```shell
 
 ```
 
  ## Task 
 
 
 ```shell
 
 ```
 
## Task 6. Play with strings 
 Complete this source code to print Welcome to Holberton School!

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long

 
 ```shell
 guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
 ```
 
## Task 7. Copy - Cut - Paste
Complete this source code

You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters 
 
```shell
guillaume@ubuntu:~/py/0x00$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/0x00$  
```
 
  ## Task 
 
 
 ```shell
 
 ```
 
  ## Task 
 
 
 ```shell
 
 ```
 
  ## Task 
 
 
 ```shell
 
 ```
