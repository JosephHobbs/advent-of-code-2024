################################################################################
# solution_02_2.py
################################################################################

import logging

log = logging.getLogger('solution.02_2')

class ReactorReporter:

    def is_safe(samples: list, use_dampener: bool = False) -> bool:

        if ReactorReporter.calculate(samples, True):
            return True
        
        if ReactorReporter.calculate(samples, False):
            return True
        
        if use_dampener:
            for i in range(len(samples)):
                sublist = list(samples)
                del sublist[i]

                if ReactorReporter.calculate(sublist, True):
                    return True
                
                if ReactorReporter.calculate(sublist, False):
                    return True

        return False
    #
    #
    #

    def calculate(samples, is_growing: bool):
        
        value = samples[0]
        for i in range(1, len(samples)):
            next_value = samples[i]

            log.debug('checking next %d against current %d.', next_value, value)

            if value == next_value:
                log.debug('values are the same, NOT SAFE!')
                return False

            else:
                acceptable_range = range(
                    ReactorReporter.get_lower_limit(value, is_growing),
                    ReactorReporter.get_upper_limit(value, is_growing))

                log.debug('validating value %d is in %s.', next_value, acceptable_range)

                if not next_value in acceptable_range:
                    return False
            
            value = next_value
        
        return True
            
    #
    # Utility Methods
    #

    def get_lower_limit(value: int, increasing: bool) -> int:
        '''
        '''
        if increasing:
            return value + 1
        else:
            return value - 3

    def get_upper_limit(value: int, increasing: bool) -> int:
        '''
        '''
        if increasing:
            return value + 4
        else:
            return value

#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    result = 0
    for input_line in input_data:

        # Split input record into separate values for processing.
        values_string = input_line.split()
        values = [int(x) for x in values_string]

        log.debug('processing input: %s', values)

        if ReactorReporter.is_safe(values, True) == True:
            result += 1

    return result

################################################################################
# END
################################################################################
