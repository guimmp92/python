#!/usr/bin/python

"""
Implement the C library atoi function.
"123" --> 123
"""

def atoi(s):
    print "Processing {0}".format(s)
    res = 0
    for c in s:
        int_value = ord(c) - ord('0')
        if int_value < 0 or int_value > 9:
            #raise TypeError("Invalid input string")
            print "Invalid input string"
            return
        res = res*10 + int_value
    print res
    return res

atoi("123")
atoi("123c4")
