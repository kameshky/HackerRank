#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    bob = 0;
    marsha = 0;
    neutral = 0;
    array_bob = [a0,a1,a2]
    array_marsha = [b0,b1,b2]
    for i in range(3):
        if(array_bob[i]-array_marsha[i]>0):
            bob += 1
        elif array_bob[i]-array_marsha[i]==0:
            neutral +=1
    return [bob, 3-bob-neutral]
        

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


