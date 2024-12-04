################################################################################
# solution_04_1.py
################################################################################

import logging

log = logging.getLogger('solution')

KEYWORD = 'XMAS'

def check_for_match(sample: str) -> int:

    if sample == KEYWORD:
        log.debug('match found!')
        return 1
    else:
        return 0


def seek_diagonal(data: list, x: int, y: int) -> int:

    matches = 0

    # Look DIAGONAL UP/LEFT

    if (x >= 3) and (y >= 3):
        sample = ''.join([data[y][x], data[y - 1][x - 1], data[y - 2][x - 2], data[y - 3][x - 3]])
        log.debug('diagonal up/left candidate %s', sample)
        matches += check_for_match(sample)

    # Look DIAGONAL UP/RIGHT

    if (x <= (len(data[y]) - 4)) and (y >= 3):
        sample = ''.join([data[y][x], data[y - 1][x + 1], data[y - 2][x + 2], data[y - 3][x + 3]])
        log.debug('diagonal up/right candidate %s', sample)
        matches += check_for_match(sample)

    # Look DIAGONAL DOWN/LEFT

    if (x >= 3) and (y <= (len(data) - 4)):
        sample = ''.join([data[y][x], data[y + 1][x - 1], data[y + 2][x - 2], data[y + 3][x - 3]])
        log.debug('diagonal down/left candidate %s', sample)
        matches += check_for_match(sample)

    # Look DIAGONAL DOWN/RIGHT

    if (x <= (len(data[y]) - 4)) and (y <= (len(data) - 4)):
        sample = ''.join([data[y][x], data[y + 1][x + 1], data[y + 2][x + 2], data[y + 3][x + 3]])
        log.debug('diagonal down/right candidate %s', sample)
        matches += check_for_match(sample)

    return matches


def seek_horizontal(data: list, x: int, y: int) -> int:

    matches = 0

    # Look LEFT -> RIGHT.

    if x <= (len(data[y]) - 4):
        sample = ''.join(data[y][x:(x + 4)])
        log.debug('horizontal forward candidate %s', sample)
        matches += check_for_match(sample)

    # Look RIGHT -> LEFT.

    if x >= 3:
        sample = ''.join(data[y][(x - 3):(x + 1)])[::-1]
        log.debug('horizontal reverse candidate %s', sample)
        matches += check_for_match(sample)

    return matches

def seek_vertical(data: list, x: int, y: int) -> int:

    matches = 0

    # Look DOWN.

    if y <= (len(data) - 4):
        sample = ''.join([data[y][x], data[y + 1][x], data[y + 2][x], data[y + 3][x]])
        log.debug('vertical down candidate %s', sample)
        matches += check_for_match(sample)
    
    # Look UP.

    if y >= 3:
        sample = ''.join([data[y][x], data[y - 1][x], data[y - 2][x], data[y - 3][x]])
        log.debug('vertical up candidate %s', sample)
        matches += check_for_match(sample)

    return matches


def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Build a list of lists to represent our word search grid.

    data = []
    for input_line in input_data:
        data.append(list(input_line))

    # Loop through and find all X's, as this is the start of the word we seek!

    result = 0

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 'X':
                log.debug('found an X at %d:%d', x, y)
                result += seek_horizontal(data, x, y)
                result += seek_vertical(data, x, y)
                result += seek_diagonal(data, x, y)
    
    return result

################################################################################
# END
################################################################################
