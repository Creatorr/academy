################################################################################
#
#  Microsoft Excel uses a special convention to name its column headers. The 
#  first 26 columns use the letters 'A' to 'Z'. Then, Excel names its column 
#  headers using two letters. After 'ZZ', Excel uses three letters.
#  Write a function that takes as input the number of the column, and returns 
#  its header. The input will not ask for a column that would be greater 
#  than 'ZZZ'.  
#   
#  Input: the first argument is a path to a file. Each line of the input file 
#  contains one test case represented by one integer.  
#
#  Output: print one line containing the Excel column heading corresponding to 
#  the integer in the input.  
#  
################################################################################

import sys

test_cases = open(sys.argv[1], 'r')

#test_cases = list() 
#for i in range(18260, 18350): test_cases.append(str(i))

dictionary = ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for test in test_cases:
    if len(test) > 0:
        int_column = int(test)
        if int_column > 18278 or int_column < 1:
            continue
        if int_column <= 26:
            print dictionary[int_column]
        else:
            if int_column <= (27*26):
                print dictionary[(int_column - 1) / 26] + dictionary[int_column % 26]
            else:
                print dictionary[(int_column - 27) / (26 * 26)] + dictionary[((int_column - 1) / 26) % 26] + dictionary[int_column % 26]
test_cases.close()