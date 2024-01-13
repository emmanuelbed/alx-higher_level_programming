#!/usr/bin/python3
# Author - Tolulope Fakunle

for firstValue in range(0, 10):
    for secondValue in range(firstValue + 1, 10):
        if firstValue == 8 and secondValue == 9:
            print("{}{}".format(firstValue, secondValue))
        else:
            print("{}{}".format(firstValue, secondValue), end=", ")
