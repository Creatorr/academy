################################################################################
#
#  Print wine names, containing all letters that Tom remembered
#   
#  Input: the first argument is a path to a file.
#  Each line includes a test case, which contains names of wines and letters
#  that Tom remembers. Names and letters are separated by a vertical bar '|'.
#
#  Output: print wine names, containing all letters that Tom remembered.
#  Letters can be anywhere in wine names. If there is no name with all letters,
#  print False. 
#  
################################################################################

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    # test = "Cabernet Merlot Noir | ot"
    # test = "Chardonnay Sauvignon | ann"
    # test = "Shiraz Grenache | o"
    pos_sep = test.find('|')
    wine = test[:pos_sep - 1]
    letters = test[pos_sep + 2:]
    for letter_wine in wine:
        if letters.find(letter_wine) > -1:
            letters = letters.replace(letter_wine, "")
    if len(letters) > 0:
        print "False"
    else:
        print wine
test_cases.close()
