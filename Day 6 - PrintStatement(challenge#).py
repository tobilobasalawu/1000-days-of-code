'''
for i in range(0, 100):
    print(i, end = '')


import os
import time

print('\033[?25l', end="")

for i in range(1, 101):
    print(i)
    time.sleep(0.1)
    os.system('cls')

print('\033[?25h', end="")

'''

def program(color, text):
    print(color, end="")
    print(text)

program('\033[?25l', 'With my new program')