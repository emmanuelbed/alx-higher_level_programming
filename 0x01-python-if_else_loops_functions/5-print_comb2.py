#!/usr/bin/python3
for nums in range (0, 100):
    if nums == 99:
        print("{}".format(nums))
    else:
        print("{:02}".format(nums), end=", ")
