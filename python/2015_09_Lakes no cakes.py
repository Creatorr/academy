################################################################################
#
#  Lakes, not cakes
#  Write a program that will count how many lakes are in the forest. We count
#  all adjacent o symbols as one lake (by adjacent we mean symbols that are
#  located one cell up, down, left, right, or diagonally from the needed symbol).
#
#  Input: The first argument is a path to a file. Each line includes a test case,
#  which contains a map of the forest of different size. Forest areas are
#  separated by a vertical bar |.
#  # - forest
#  o - lake
#
#  Output: Print the number of lakes for each test case.
#
################################################################################

import sys


#  function recursive_check loops through neighboring cells using recursion
#  Input:
#       field_list(list): field
#       source_row(int): row index from field
#       source_col(int): column index from field
#       num_lakes_r: counter lakes
#  Output: mutable field_list(list)
def recursive_check(field_list, source_row, source_col, num_lakes_r):
    for neighbors_row in range(-1, 2):
        for neighbors_col in range(-1, 2):
            field_list[source_row][source_col] = num_lakes_r
            if field_list[source_row + neighbors_row][source_col + neighbors_col] == "o" \
                    and (neighbors_col == 0 and neighbors_row == 0) == False:
                field_list = recursive_check(field_list,
                                             source_row + neighbors_row,
                                             source_col + neighbors_col,
                                             num_lakes_r)
    return field_list


test_cases = open(sys.argv[1], 'r')
#  test_cases = open(r"C:\work\Academy\academy\test_for_scripts\test_2015_09_Lakes no cakes.txt", 'r')

for test in test_cases:
    num_lakes = 1
    field = list()
    field_rows = test.split("|")
    field_nrow = len(field_rows)
    field_ncols = len(field_rows[0].split())
    border_list = ["#" for dummy_border in range(field_ncols + 2)]
    field.append(border_list)
    for cols in range(field_nrow):
        field.append(list("#") + field_rows[cols].split() + list("#"))
    field.append(border_list)
    for rows in range(1, field_nrow + 1):
        for cols in range(1, field_ncols + 1):
                if field[rows][cols] == "o":
                    field = recursive_check(field, rows, cols, num_lakes)
                    num_lakes += 1
    print num_lakes - 1
test_cases.close()
