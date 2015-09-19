################################################################################
#
#  Time to eat
#  At codeeval.com, we have a cat called Kitty. She loves eating, and it seems
#  like she can eat anything any time. We want to keep Kitty fit, so we feed her
#  according to a schedule. Planning her daily meals, we need to see when Kitty
#  will eat starting with the latest meal in the evening to the earliest morning
#  snack. So, your task is to sort timestamps in the schedule in a reverse
#  chronological order.
#
#  Input: The first argument is a path to a file. Each line includes a test case:
#  a schedule containing unsorted timestamps in HH:MM:SS format.
#
#  Output: Sort timestamps in each schedule from the biggest to the smallest one.
#
################################################################################

import sys

test_cases = open(sys.argv[1], 'r')
#  test_cases = open(r"C:\work\Academy\academy\test_for_scripts\test_2015_09_CODEEVAL_Time to eat.txt", 'r')

for test in test_cases:
    if len(test) > 0:
        sec_list = list()
        time_list = test.replace("\n", "", 1).split(" ")
        for time_item in time_list:
            time_item_split = time_item.split(":")
            sec_list.append((int(time_item_split[0]) * 60 * 60 +
                             int(time_item_split[1]) * 60 +
                             int(time_item_split[2]),
                             time_item))
        print ' '.join(dummy_sec for (_, dummy_sec) in sorted(sec_list, reverse=True))
test_cases.close()
