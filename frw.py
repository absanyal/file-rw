# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 20:20:18 2016

@author: AB Sanyal

A cose to read from and write to files. Only for Experimental purposes.
"""

with open("ftor.txt", "r") as ftr:
    content = ftr.readlines()

ftr.close()

filename = "yololo.txt"

ftw = open(filename, "a")

for i in range(0, len(content)):
    ftw.write(content[i])

ftw.close()