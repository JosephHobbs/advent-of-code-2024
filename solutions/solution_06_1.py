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

    class ACTION(Enum):
        '''
        '''
        MOVE_FWD = 0
        TURN_RIGHT = 1

    class DIRECTION_OF_TRAVEL(Enum):
        '''
        '''

        UP = (0, 0, -1, '^', 2)
        RIGHT = (1, 1, 0, '>', 5)
        DOWN = (2, 0, 1, 'v', 7)
        LEFT = (3, -1, 0, '<', 4)

        def __init__(self, index: int, x_offset: int, y_offset: int, indicator: str, neighbor_index: int):
            '''
            '''

            self.index = index
            self.x_offset = x_offset
            self.y_offset = y_offset
            self.indicator = indicator
            self.neighbor_index = neighbor_index


    #
    #
    #

    def __init__(self, grid: Grid):
        '''
        '''

        self._grid = grid

        self._current_d = None
        self._current_x = None
        self._current_y = None
        self.has_left = False
        self.visited = []

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

    def _move(self):
        self._current_x += self._current_d.x_offset
        self._current_y += self._current_d.y_offset

    def _turn_right(self):
        if self._current_d == ObjectTracker.DIRECTION_OF_TRAVEL.UP:
            self._current_d = ObjectTracker.DIRECTION_OF_TRAVEL.RIGHT
        elif self._current_d == ObjectTracker.DIRECTION_OF_TRAVEL.RIGHT:
            self._current_d = ObjectTracker.DIRECTION_OF_TRAVEL.DOWN
        elif self._current_d == ObjectTracker.DIRECTION_OF_TRAVEL.DOWN:
            self._current_d = ObjectTracker.DIRECTION_OF_TRAVEL.LEFT
        else:
            self._current_d = ObjectTracker.DIRECTION_OF_TRAVEL.UP

    def run(self):

        self.visited.append((self._current_x, self._current_y))

        while True:

            log.debug('grabbing current coordinate: %d:%d', self._current_x, self._current_y)
            coord = self._grid.get_coordinate(self._current_x, self._current_y)
            next_coord_value = coord.get_value_str(self._current_d.neighbor_index)
            log.debug('neighbor coordinate is %s', next_coord_value)

            if next_coord_value == '.' or next_coord_value == '^':
                log.debug('moving %s', self._current_d)
                self._move()
                visited_coord = (self._current_x, self._current_y)
                if visited_coord not in self.visited:
                    self.visited.append(visited_coord)
            elif next_coord_value == '#':
                log.debug('turning right')
                self._turn_right()
            else:
                log.debug('exited map')
                break

    def get_visited_count(self):
        return len(self.visited)

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

    tracker = ObjectTracker(grid)
    tracker.run()

    return tracker.get_visited_count()

################################################################################
# END
################################################################################
