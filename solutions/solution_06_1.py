################################################################################
# solution_06_1.py
################################################################################

from enum import Enum
import logging
from .utils.grid import Grid

log = logging.getLogger('solution')

#
#
#

class ObjectTracker:
    '''
    '''

    class DIRECTION_OF_TRAVEL(Enum):
        '''
        '''

        UP = (0, 0, -1, '^')
        RIGHT = (1, 1, 0, '>')
        DOWN = (2, 0, 1, 'v')
        LEFT = (3, -1, 0, '<')

        def __init__(self, index: int, x_offset: int, y_offset: int, indicator: str):
            '''
            '''

            self.index = index
            self.x_offset = x_offset
            self.y_offset = y_offset
            self.indicator = indicator


    def __init__(self, grid: Grid):
        '''
        '''

        self._grid = grid
        self._current_d = None
        self._current_x = None
        self._current_y = None

        self._init_starting_position()

    def _init_starting_position(self) -> tuple:
        '''
        '''

        log.debug('determining starting position...')

        for row_id in range(len(self._grid.data)):
            log.debug('checking row %d: %s', row_id, self._grid.data[row_id])
            for dot in ObjectTracker.DIRECTION_OF_TRAVEL:
                log.debug('checking for indicator %s in row %s', dot.indicator, self._grid.data[row_id])
                if dot.indicator in self._grid.data[row_id]:
                    log.debug('found indicator in row!')
                    self._current_y = row_id
                    self._current_x = self._grid.data[row_id].index(dot.indicator)
                    self._current_d = dot

        if (self._current_x != None) and (self._current_y != None) and self._current_d:
            log.debug(
                'starting position identified: %d:%d facing %s',
                self._current_x, self._current_y, self._current_d.name)
        else:
            raise RuntimeError('unable to determine starting position!')


#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    # Build a grid to store the map.

    grid = Grid()
    for input_line in input_data:
        grid.add_row_str(input_line)

    #
    #
    #

    result = 0

    tracker = ObjectTracker(grid)






    return result

################################################################################
# END
################################################################################
