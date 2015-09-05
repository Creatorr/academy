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

#  import urllib2
#  test  = https://github.com/Creatorr/academy/blob/master/test_for_scripts/test_2015_08_CODEEVAL_Chardonnay%20or%20Cabernet.txt
#  test_cases = urllib2.urlopen("https://dl.dropboxusercontent.com/u/31749115/test.txt")

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if len(test) > 0:
        pos_sep = test.find('|')
        wine_str = test[:pos_sep - 1]
        wine_list = wine_str.split(" ")
        wine_out = list()
        letters = test[pos_sep + 2:].strip()
        for wine in wine_list:
            letters_temp = letters
            for letter_wine in wine:
                if letters_temp.find(letter_wine) > -1:
                    letters_temp = letters_temp.replace(letter_wine, "", 1)
            if len(letters_temp) == 0:
                wine_out.append(wine)
        if len(wine_out) > 0:
            print " ".join(wine_out)
        else:
            print False
test_cases.close()