"""
  One zero, two zero...

    Deciphering code includes many stages, and you are taking part in one of them. Therefore, your task is the
    following: you have two numbers - the first one is the number of zeros in a binary code and the second one
    shows the range from 1 to this number, where you have to find these zeros.

    Input sample:
        The first argument is a path to a file. Each line includes a test case with two numbers: the first one is the
        number of zeros in a binary code that we need to find and the second one is the range from 1 to this number
        where you have to find these zeros.
    Output sample:
        Print the total number of numerals that contain the needed amount of zeros in a binary system.
"""

import sys

try:
    test_cases = open(sys.argv[1], 'r')
except IndexError:
    test_cases = open(r"C:\work\Academy\academy\test_for_scripts\test_2015_10_CODEEVAL_One zero two zero.txt", 'r')

for test in test_cases:
    target_zero, target_num = test.replace("\n", "", 1).split(" ")
    count_target = 0
    for dummy_num in range(1, int(target_num) + 1):
        if int(str(bin(dummy_num))[2:].count("0")) == int(target_zero):
            count_target += 1
    print count_target
test_cases.close()
