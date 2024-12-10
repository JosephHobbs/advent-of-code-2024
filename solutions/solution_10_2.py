################################################################################
# solution_06_1.py
################################################################################

import logging
from .utils.grid import Grid, Coordinate

log = logging.getLogger('solution')

#
#
#

class TrailChaser:

    OF_INTEREST = [
        Coordinate.Position.CENTER_UP,
        Coordinate.Position.RIGHT,
        Coordinate.Position.CENTER_DOWN,
        Coordinate.Position.LEFT
    ]

    POINT_LOW = 0
    POINT_HIGH = 9

    def __init__(self, grid: Grid):
        self.grid = grid
        self.trails = {}

    def _add_trail(self, start: Coordinate, end: Coordinate):

        key = str(f'{start.x}:{start.y}')
        value = str(f'{end.x}:{end.y}')
        if not key in self.trails.keys():
            self.trails[key] = []
        self.trails[key].append(value)

    def chase(self, coord: Coordinate, coord_start: Coordinate):

        current_value = coord.get_value_int(Coordinate.Position.CENTER)
        log.debug('[%d:%d] = %d', coord.x, coord.y, current_value)
        if current_value == self.POINT_HIGH:
            log.debug('[%d:%d] end of trail', coord.x, coord.y)
            self._add_trail(coord_start, coord)
            return

        for position in self.OF_INTEREST:
            neighbor_val = coord.get_value_int(position)
            if neighbor_val and (neighbor_val == (current_value + 1)):
                neighbor = self.grid.get_coordinate((coord.x + position.x_offset), (coord.y + position.y_offset))
                log.debug('elevated neighbor at %d:%d', neighbor.x, neighbor.y)
                self.chase(neighbor, coord_start)

    def count_trails(self) -> int:

        for y in range(0, len(self.grid.data)):
            for x in range(0, len(self.grid.data[y])):
                coord = self.grid.get_coordinate(x, y)
                if coord.get_value_int(Coordinate.Position.CENTER) == self.POINT_LOW:
                    log.debug('found trail head at %d:%d, chasing...', x, y)
                    self.chase(coord, coord)

        trails = 0
        for _, ends in self.trails.items():
            trails += len(ends)

        return trails

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

    trail_chaser = TrailChaser(grid)

    result = trail_chaser.count_trails()

    return result

################################################################################
# END
################################################################################
