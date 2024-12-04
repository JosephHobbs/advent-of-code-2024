################################################################################
# solution_04_2.py
################################################################################

import logging

log = logging.getLogger('solution')

def check_for_match(sample: str) -> int:

    if sample == 'MAS':
        log.debug('match found!')
        return 1
    else:
        return 0


def seek_x_mas(data: list, x: int, y: int) -> int:

    matches = 0

    # Check the 4 possible character strings. if 2/4 match, we're good!

    if (x >= 1) and (x <= (len(data[y]) - 2)) and (y >= 1) and (y <= (len(data) - 2)):
        # check down/right
        matches += check_for_match(''.join([data[y-1][x-1], data[y][x], data[y+1][x+1]]))
        # check down/left
        matches += check_for_match(''.join([data[y-1][x+1], data[y][x], data[y+1][x-1]]))
        # check up/left
        matches += check_for_match(''.join([data[y+1][x+1], data[y][x], data[y-1][x-1]]))
        # check up/right
        matches += check_for_match(''.join([data[y+1][x-1], data[y][x], data[y-1][x+1]]))

    return (matches == 2)


def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Build a list of lists to represent our word search grid.

    data = []
    for input_line in input_data:
        data.append(list(input_line))

    # Loop through and find all X's, as this is the start of the word we seek!

    result = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'A':
                log.debug('found an A at %d:%d', x, y)
                if seek_x_mas(data, x, y):
                    result += 1
    
    return result

################################################################################
# END
################################################################################
