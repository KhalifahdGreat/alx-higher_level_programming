#!/usr/bin/python3
'''
   3-say_my_name
   Contains a function that prints names
'''
def say_my_name(first_name, last_name=""):
    '''
        a Python function that takes two strings and prints them
    '''
    errmsg = 'first_name must be a string'
    errmsg1 = 'last_name must be a string'

    if not isinstance(first_name, str):
        raise TypeError(errmsg)
    if not isinstance(last_name, str):
        raise TypeError(errmsg1)
    else:
        print('My name is {} {}'.format(first_name, last_name))
