"""
This code snippet is part of story published on Medium.com at
https://medium.com/cspackets/and-then-i-understood-recursion-c0775125049f

Name of the program :- call_stack_demo.py
Sample code to demonstrate call stack.
"""

import traceback

def function_a():
  return function_b()

def function_b():
  return function_c()

def function_c():
  # Prints a stack trace from its invocation point.
  traceback.print_stack()
  return "Hi"

if __name__ == "__main__":
  # Execution starts here.
  print function_a()
