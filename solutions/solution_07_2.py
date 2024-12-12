################################################################################
# solution_07_1.py
################################################################################

from itertools import product
import logging
import re

log = logging.getLogger('solution')

#
#
#

class EquationTester:

    def __init__(self, operators: list, min_inputs: int, max_inputs: int):
        self._valid_ops = operators

        self._combos = {}
        for i in range(min_inputs - 1, max_inputs):
            log.debug('generating combos for %d', i)
            self._combos[i] = list(product(self._valid_ops, repeat=i-1))
            log.debug('combo %d contains %d entries', i, len(self._combos[i]))
        
    def check_validity(self, result: int, input_set: list) -> int:

        input_count = len(input_set)
        log.debug('running validation for %d; %s', input_count, input_set)
        for i in range(0, len(self._combos[input_count])):
            calc_combo = self._combos[input_count][i]
            total = input_set[0]
            for j in range(0, len(calc_combo)):
                operation = calc_combo[j]
                if operation == '+':
                    total += input_set[j + 1]
                elif operation == '*':
                    total = total * input_set[j + 1]
                else:
                    total = int(str(total) + str(input_set[j + 1]))

            if total == result:
                return result

        return 0
#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Prepare input data for processing.

    inputs = []
    for input_line in input_data:
        matches = re.findall('\d+', input_line)
        inputs.append([int(x) for x in matches])

    #
    #
    #

    min_width = 99
    max_width = 0
    for i in range(len(inputs)):
        this_width = len(inputs[i])
        if this_width < min_width:
            min_width = this_width
        if this_width > max_width:
            max_width = this_width

    calibration_tester = EquationTester(['+', '*', '|'], min_width, max_width)

    result = 0
    input_count = len(inputs)
    input_current = 0
    for input in inputs:
        input_current += 1
        log.debug('processing %d of %d', input_current, input_count)
        result += calibration_tester.check_validity(input[0], input[1:])

    return result

################################################################################
# END
################################################################################
