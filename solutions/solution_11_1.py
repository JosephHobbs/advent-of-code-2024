################################################################################
# solution_11_1.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

def blink(input: list) -> list:

    result = []

    for stone in input:
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            midpoint = len(stone_str) // 2
            result.append(int(stone_str[:midpoint]))
            result.append(int(stone_str[midpoint:]))
        else:
            result.append(stone * 2024)

    return result
        

#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    #
    #
    #

    stones = [int(x) for x in input_data[0].split()]

    for i in range(25):
        stones = blink(stones)

    return len(stones)

################################################################################
# END
################################################################################
