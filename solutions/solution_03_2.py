################################################################################
# solution_03_2.py
################################################################################

import logging
import re

log = logging.getLogger('solution')

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Create one big string using the provided input data.

    input = ''
    for input_line in input_data:
        input += input_line

    log.debug('input data: %s', input)

    # Use regex to parse out operations do(), don't() and mul(#,#).

    operations = re.findall('do\(\)|don\'t\(\)|mul\(\d+\,\d+\)', input)

    # Process each operation in sequence, honoring the do/don't operations
    # to start/stop processing of mul operations.

    pattern_mul_data = re.compile('\d+')

    result = 0
    enabled = True
    for operation in operations:
        log.debug('processing operation: %s', operation)

        if operation == 'do()':
            log.debug('do operation detected')
            enabled = True
        elif operation == 'don\'t()':
            log.debug('don\'t operation detected')
            enabled = False
        else:
            if enabled:
                log.debug('enabled, processing mul operation')
                values = pattern_mul_data.findall(operation)
                value0 = int(values[0])
                value1 = int(values[1])
                log.debug('found operation data: %d : %d', value0, value1)
                result += (value0 * value1)
            else:
                log.debug('disabled, ignoring mul operation')

    return result

################################################################################
# END
################################################################################
