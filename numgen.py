#!/usr/bin/python

import random

def ind():
    oper='-+*/'
    num='1234567890'
    A=''
    for i in range(10):
        A += random.choice(num+oper)
    try: B = [A,eval(A)]
    except SyntaxError: B = "DEAD"
    return B


for i in range(10):
    indy = ind()
    print indy

