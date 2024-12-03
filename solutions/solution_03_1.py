################################################################################
# solution_03_1.py
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

    # Use regex to parse out the mul() operations. Only those that match the
    # patterm mul(#,#) are valid.

    mul_operations = re.findall('mul\(\d+\,\d+\)', input)

    # Process each operation by parsing out the two numeric values. Convert to
    # int (from str), multiply together and add to the running result.

    pattern_mul_data = re.compile('\d+')

    result = 0
    for operation in mul_operations:
        log.debug('processing operation: %s', operation)
        values = pattern_mul_data.findall(operation)
        value0 = int(values[0])
        value1 = int(values[1])
        log.debug('found operation data: %d : %d', value0, value1)
        result += (value0 * value1)

    return result

################################################################################
# END
################################################################################
