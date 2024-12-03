################################################################################
# solution_02_1.py
################################################################################

import logging

log = logging.getLogger('solution.02_1')

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    result = 0
    for input_line in input_data:

        # Split input record into separate values for processing.
        values_string = input_line.split()
        values = [int(x) for x in values_string]

        log.debug('processing input: %s', values)

        # If the first and second values are the same, this is considered
        # an unsafe sample. So stop processing and move to the next one.

        if values[0] == values[1]:
            log.debug('first two values equal; dropping : %s', values)
            continue

        # Figure out if our samples are increasing. We'll assume decrease
        # to begin with.

        is_increasing = False
        if values[0] < values[1]:
            is_increasing = True

        # Process the samples by checking each one against. They should be
        # consistently increasing/decreasing by 1-3 values per sample.

        is_safe = True
        for i in range(1, len(values)):

            if is_increasing:
                limit_lower = values[i - 1] + 1
                limit_upper = values[i - 1] + 4
            else:
                limit_lower = values[i - 1] - 3
                limit_upper = values[i - 1]

            log.debug('verifying %d is between %d and %d...', values[i], limit_lower, limit_upper)
            if not values[i] in range(limit_lower, limit_upper):
                log.debug('  nope!')
                is_safe = False
                break

        if is_safe:
            log.debug('found safe set => %s', values)
            result += 1

    return result

################################################################################
# END
################################################################################
