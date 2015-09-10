################################################################################
#
#  Help Robitta learn how many nuts Robo will bring this time to decide what 
#  jewelry she will be able to make. 
#   
#  Input: the first argument is a path to a file. Each line includes a test 
#  case, which contains the size of the field that Robo will go through, and 
#  X and Y coordinates of a place where Robitta waits for him. Field size and 
#  coordinates are separated by a vertical bar '|'. 
#
#  Output: print the number of nuts that Robo will bring to Robitta. 
#  
################################################################################

import sys

# import urllib2
# test_cases = urllib2.urlopen("https://dl.dropboxusercontent.com/u/31749115/test_for_academy/test_2015_09_CODEEVAL_Robo%20and%20Robitta.txt")

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if len(test) > 0:
        pos_sep = test.find('|')
        size_field = test[:pos_sep - 1].split("x")
        field_x = int(size_field[0])
        field_y = int(size_field[1])
        field = [[1] * field_x for dummy_y in range(field_y)]
        robitta_xy = test[pos_sep + 2:].split(" ")
        robitta_x = int(robitta_xy[0]) - 1
        robitta_y = field_y - int(robitta_xy[1])       
        robo_x = 0
        robo_y = 0
        direction = "right"
        nuts = 1
        for cell in range(0, field_x * field_y):
            field[robo_y][robo_x] = 0
            if robo_x == robitta_x and robo_y == robitta_y:
                break
            if direction == "right":
                if robo_x + 1 == field_x:
                    direction = "down"
                    robo_y += 1
                elif field[robo_y][robo_x + 1] == 0:
                    direction = "down"
                    robo_y += 1
                else:                    
                    robo_x += 1
            elif direction == "left":
                if robo_x == 0:
                    direction = "up"
                    robo_y -= 1
                elif field[robo_y][robo_x - 1] == 0:
                    direction = "up"
                    robo_y -= 1
                else:
                    robo_x -= 1
            elif direction == "up":
                if robo_y == 0:
                    direction = "right"
                    robo_x += 1
                elif field[robo_y - 1][robo_x] == 0:
                    direction = "right"
                    robo_x += 1
                else:
                    robo_y -= 1
            elif direction == "down":
                if robo_y + 1 == field_y:
                    direction = "left"
                    robo_x -= 1
                elif field[robo_y + 1][robo_x] == 0:
                    direction = "left"
                    robo_x -= 1
                else:
                    robo_y += 1
            nuts += 1
            if robo_x == robitta_x and robo_y == robitta_y:
                break
        print nuts
test_cases.close()