' a test module '

__author__ = 'Test'

PI = 3.14
_private = 'private_test'
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello,world")
    elif len(args) == 2:
        print("Hello, %s" %args[1])
    else:
        print("too many arguments!")

if __name__ == "__main__":
    test()