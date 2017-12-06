#!/bin/python3

import sys


N = int(input().strip())
if N%2!=0 or (N%2==0 and 6<=N<21):
    print ("Weird")
else:
    print("Not Weird")
