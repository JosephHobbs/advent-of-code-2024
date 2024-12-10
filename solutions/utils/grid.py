################################################################################
# grid.py
################################################################################

from enum import Enum
import logging

log = logging.getLogger('solutions.utils.grid')

class Coordinate:
    '''
    '''

    class Position(Enum):
        '''
        '''

        CENTER =      (0,  0,  0)
        LEFT_UP =     (1, -1, -1)
        CENTER_UP =   (2,  0, -1)
        RIGHT_UP =    (3,  1, -1)
        LEFT =        (4, -1,  0)
        RIGHT =       (5,  1,  0)
        LEFT_DOWN =   (6, -1,  1)
        CENTER_DOWN = (7,  0,  1)
        RIGHT_DOWN =  (8,  1,  1)

        def __init__(self, index: int, x_offset: int, y_offset: int):
            '''
            '''
            self.index = index
            self.x_offset = x_offset
            self.y_offset = y_offset

    def __init__(self, x: int, y: int, values: list):
        '''
        Initialize coordinate with neighbor data.

            123
            405
            678
        '''
        self.x = x
        self.y = y
        self._values = values

    def get_value_int(self, position: Position) -> int:
        value = self._values[position.index]
        if value:
            return int(value)
        else:
            return None

    def get_value_str(self, position: Position) -> str:
        value = self._values[position.index]
        if value:
            return str(value)
        else:
            return None


class Grid:

    def __init__(self):
        self.data = []

    def add_row_str(self, row: str):

        if row:
            if (len(self.data) == 0) or (len(row) == len(self.data[0])):
                self.data.append([*row])
            else:
                raise ValueError(
                    f'too many characters: {len(row)} [expected {len(self.data[0])}]')

    def get_coordinate(self, x: int, y: int) -> Coordinate:
        return Coordinate(x, y, self._resolve_coordinate_data(x, y))
    
    def _resolve_coordinate_data(self, x: int, y: int) -> list:

        if (y >= len(self.data)) and (x >= len(self.data[0])):
            raise IndexError(
                f'coordinate out of range: {x}:{y} (max: {len(self.data[0] - 1)}:{len(self.data - 1)})')

        coord_data = [None] * len(Coordinate.Position)
        for position in Coordinate.Position:
            target_x = x + position.x_offset
            target_y = y + position.y_offset

            if (target_y < len(self.data)) \
                and (target_y >= 0) \
                and (target_x < len(self.data[target_y])) \
                and (target_x >= 0):
                
                coord_data[position.index] = self.data[target_y][target_x]
        
        return coord_data

################################################################################
# END
################################################################################
