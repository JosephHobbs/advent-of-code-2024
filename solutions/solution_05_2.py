################################################################################
# solution_05_2.py
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
        self.pages = [int(x) for x in page_list]

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

        rule = tuple((int(page_before), int(page_after)))
        if rule not in self._rules:
            self._rules.append(rule)
        else:
            log.warning('skipping duplicate rule: %s', rule)

    def does_rule_apply(self, rule: tuple, pages: list) -> bool:
        '''
        '''

        if (rule[0] in pages) and (rule[1] in pages):
            log.debug('rule (%s) applies to (%s)', rule, pages)
            return True
        else:
            log.debug('rule (%s) does NOT apply to (%s)', rule, pages)
            return False

    def get_corrected_update(self, update: UpdateSet) -> UpdateSet:

        new_pages = list(update.pages)

        while True:

            changed = False
            for rule in self._rules:

                if self.does_rule_apply(rule, new_pages) and self.is_in_violation(rule, new_pages):
                    log.debug('updating (%s) based on rule (%s)', new_pages, rule)
                    new_pages = self.fix_violation(rule, new_pages)
                    log.debug('update is now (%s)', new_pages)
                    changed = True
                    break

            if not changed:
                break

        return UpdateSet(new_pages)

    def is_in_violation(self, rule: tuple, pages: list) -> bool:
        '''
        '''

        if rule[1] in pages[0:pages.index(rule[0])]:
            log.debug('violation detected, %d before %d : %s', rule[1], rule[0], pages)
            return True
        else:
            return False

    def is_update_valid(self, update_set: UpdateSet) -> bool:
        '''
        '''

        result = True

        for rule in self._rules:
            if (rule[0] in update_set.pages) and (rule[1] in update_set.pages):
                log.debug('rule (%s) applies to update set (%s)', rule, update_set.pages)
                if rule[1] in update_set.pages[0:update_set.pages.index(rule[0])]:
                    log.debug('violation detected, %d before %d : %s', rule[1], rule[0], update_set.pages)
                    result = False
                    break
            else:
                log.debug('rule (%s) does NOT apply to update set (%s)', rule, update_set.pages)

        return result

    def fix_violation(self, rule: tuple, pages: list) -> list:

        fixed_pages = list(pages)
        log.debug('removing %d from (%s)', rule[1], pages)
        fixed_pages.remove(rule[1])
        log.debug('inserting %d into (%s) at %d', rule[1], fixed_pages, (fixed_pages.index(rule[0]) + 1))
        fixed_pages.insert((fixed_pages.index(rule[0]) + 1), rule[1])
        return fixed_pages


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
        else:
            log.debug('found INVALID update set, correcting!')
            corrected_update = rules.get_corrected_update(update)
            middle_page = corrected_update.get_middle_page()
            log.debug('adding middle page %d to current result.', middle_page)
            result += middle_page

    return result

################################################################################
# END
################################################################################
