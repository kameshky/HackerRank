#!/bin/python3

import sys


n = int(input().strip())
n = str(format(n,'b'))
string_find='1'
for i in range(0,len(n)):
    if string_find in n:
        string_find+='1'
    else:
        break
print(len(string_find)-1)
