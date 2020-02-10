#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CALCULADORA SIMPLE CON PYTHON
"""

import sys


def f_sum(num1, num2):
    print("your sum is: ", float(num1)+float(num2))


def f_res(num1, num2):
    print("your res is: ", float(num1)-float(num2))


def f_div(num1, num2):
    try:
        print("your sum is: ", float(num1) / float(num2))
    except ZeroDivisionError:
        print("you try to divided by zero")


try:

    if sys.argv[2] == '+':
        f_sum(sys.argv[1], sys.argv[3])
    elif sys.argv[2] == '-':
        f_res(sys.argv[1], sys.argv[3])
    elif sys.argv[2] == '/':
        f_div(sys.argv[1], sys.argv[3])


except ValueError:
    print("could not convert string to float:", sys.argv[1], sys.argv[2], sys.argv[3])
except TypeError:
    print("Upss something is broken", sys.argv[1], sys.argv[2], sys.argv[3])
except SyntaxError:
    print("Are tou sure:", sys.argv[1], sys.argv[2], sys.argv[3])





