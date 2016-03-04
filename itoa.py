#!/usr/bin/python

"""
Convert an integer number in any base into a string, e.g. 123 in base 10 --> "123"
"""


def convert_to_string(num, base=10):
    if num // base == 0:
        return chr(num + ord('0'))
    return convert_to_string(num // base, base) + chr(num % base + ord('0'))


print "Enter integer to convert:"
integer = int(raw_input())
print convert_to_string(integer)
