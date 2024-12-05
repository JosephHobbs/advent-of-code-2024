################################################################################
# solution_05_1.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

class UpdateSet:
    '''
    '''

    def __init__(self, page_list: list):
        '''
        '''
        self.pages = page_list

    def get_middle_page(self) -> int:
        '''
        '''
        
        index_of_middle_page = int((len(self.pages) + 1) / 2) - 1
        return int(self.pages[index_of_middle_page])


class RuleSet:
    '''
    '''

    def __init__(self):
        '''
        '''

        self._rules = []

    def add_rule(self, page_before: int, page_after: int):
        '''
        '''

        rule = tuple((page_before, page_after))
        if rule not in self._rules:
            self._rules.append((page_before, page_after))
        else:
            log.warning(
                'skipping duplicate rule: %d before %d',
                page_before,
                page_after)

    def is_update_valid(self, update_set: UpdateSet) -> bool:
        '''
        '''

        result = True

        for rule in self._rules:
            if (rule[0] in update_set.pages) and (rule[1] in update_set.pages):
                log.debug('rule (%s) applies to update set (%s)', rule, update_set.pages)
                if rule[1] in update_set.pages[0:update_set.pages.index(rule[0])]:
                    log.debug('violation detected, %s before %s : %s', rule[1], rule[0], update_set.pages)
                    result = False
                    break
            else:
                log.debug('rule (%s) does NOT apply to update set (%s)', rule, update_set.pages)

        return result




def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Build a list of lists to represent our word search grid.

    rules = RuleSet()
    updates = []
    for input_line in input_data:
        if '|' in input_line:
            log.debug('reading instruction: %s', input_line)
            instruction_details = input_line.split('|', 2)
            rules.add_rule(
                instruction_details[0], instruction_details[1])
        elif ',' in input_line:
            log.debug('reading update: %s', input_line)
            updates.append(UpdateSet(input_line.split(',')))

    #
    #
    #

    result = 0

    for update in updates:
        if rules.is_update_valid(update):
            log.debug('found valid update set!')
            middle_page = update.get_middle_page()
            log.debug('adding middle page %d to current result.', middle_page)
            result += middle_page
        else:
            log.debug('found INVALID update set!')

    return result

################################################################################
# END
################################################################################
