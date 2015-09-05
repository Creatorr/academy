"""
Merge function for 2048 game.
Coding Style Guidelines by the use of Pylint.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """

    line_out = [0*dummy_zero for dummy_zero in line]
    num_out = 0
    num_in = 0
    while num_out <= len(line_out):
        for element in range(num_in,len(line)):
            #print num_out, num_in, element, line[element], line_out
            if line[element] <> 0:
                if line_out[num_out] == 0:
                    line_out[num_out] = line[element]
                    num_out -= 1
                else:
                    if line[element] == line_out[num_out]:
                        line_out[num_out] = line_out[num_out] * 2
                    else:
                        line_out[num_out + 1] = line[element]
                num_in = element + 1
                break
        num_out += 1
    return line_out

#  print merge([0, 0, 2, 2])
#  [2, 0, 2, 4] should return [4, 4, 0, 0]
#  [0, 0, 2, 2] should return [4, 0, 0, 0]
#  [2, 2, 0, 0] should return [4, 0, 0, 0]
#  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0]
#  [8, 16, 16, 8]