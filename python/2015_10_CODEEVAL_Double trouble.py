################################################################################
#
#  Double Trouble
#  According to the analysis, there can be only 2 letters in the code: A and B.
#  All messages are transmitted in a form of two equal parts (ABAB, AAAA, BABA,
#  and so on).
#  Some messages are so mutilated that scientists need to know how many correct
#  variants of the messages might exist to decide whether it would make sense to
#  decipher their meaning, and how long it would take. Therefore, you need to
#  calculate the number of possible correct variants for each message
#
#  Input: The first argument is a path to a file.  Each line includes a test case
#  containing one message that includes three symbols:
#  A,B or *
#
#  Output: Print the number of possible correct variants of each message.
#
################################################################################

import sys

# test_cases = open(sys.argv[1], 'r')
test_cases = open(r"C:\work\Academy\academy\test_for_scripts\test_2015_10_CODEEVAL_Double trouble.txt", 'r')

for test in test_cases:
    len_code = len(test)
    if len_code > 0:
        error_code = False
        variants = 0
        asterisk = 0
        for index_code in range(len_code / 2):
            letter_1 = test[index_code]
            letter_2 = test[index_code + len_code / 2]
            if letter_1 == letter_2 == "*":
                asterisk += 1
            elif letter_1 != letter_2:
                if ((letter_1 == "A" or letter_1 == "B") and letter_2 == "*")\
                        or ((letter_2 == "A" or letter_2 == "B") and letter_1 == "*"):
                    variants += 1
                else:
                    error_code = True
                    break
        if error_code:
            print 0
        else:
            if asterisk > 0:
                variants = 2 ** asterisk
            else:
                variants = 1
            print variants
test_cases.close()
