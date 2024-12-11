################################################################################
# solution_11_2.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

def blink(input: dict):

    result = {}
    for key in input.keys():
        
        if key == 0:
            if not 1 in result:
                result[1] = 0
            result[1] += input[key]
        
        elif len(str(key)) % 2 == 0:
            key_str = str(key)
            key_midpoint = len(key_str) // 2
            new_key_1 = int(key_str[:key_midpoint])
            new_key_2 = int(key_str[key_midpoint:])

            if not new_key_1 in result:
                result[new_key_1] = 0
            result[new_key_1] += input[key]

            if not new_key_2 in result:
                result[new_key_2] = 0
            result[new_key_2] += input[key]

        else:

            new_key = key * 2024
            if not new_key in result:
                result[new_key] = 0
            result[new_key] += input[key]
    
    return result

#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    #
    #
    #

    inputs = [int(x) for x in input_data[0].split()]

    stones = {}
    for input in inputs:
        stones[input] = 1

    for i in range(75):
        log.debug('Here goes %d', (i + 1))
        log.debug(stones)
        stones = blink(stones)

    total_stones = 0
    for _, count in stones.items():
        total_stones += count
    
    return total_stones

################################################################################
# END
################################################################################
