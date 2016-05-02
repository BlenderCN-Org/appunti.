# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 23:36:46 2016

@author: maurizio
"""

def find_path():
    import sys
    s = sys.path
    path = "export PYTHONPATH="
    for elem in s:
        path += "{};".format(elem)
    return path 

print find_path()
