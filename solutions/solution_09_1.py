################################################################################
# solution_09_1.py
################################################################################

import logging

log = logging.getLogger('solution')

#
#
#

class Filesystem:

    EMPTY = -1

    def __init__(self, disk_map_compressed: str):

        self._disk_map = self._decompress(disk_map_compressed)

    def _decompress(self, disk_map_compressed: str) -> list:

        disk_map = []

        file_number = -1
        processing_file = True
        for i in list(disk_map_compressed):

            entity_block_count = int(i)

            block = self.EMPTY
            if processing_file:
                file_number += 1
                block = file_number

            for _ in range(entity_block_count):
                disk_map.append(block)

            processing_file = not processing_file

        return disk_map

    def defragment(self):

        while self.is_fragmented():

            if self._disk_map[-1] == self.EMPTY:
                del self._disk_map[-1]    
            else:
                first_free = self._disk_map.index(self.EMPTY)
                self._disk_map[first_free] = self._disk_map[-1]
                del self._disk_map[-1]

    def get_checksum(self) -> int:

        checksum = 0
        for i in range(len(self._disk_map)):
            checksum += i * self._disk_map[i]

        return checksum

    def is_fragmented(self) -> bool:
        return (self.EMPTY in self._disk_map)


#
#
#

def solve(input_filename: str, input_data: list, use_debug: bool) -> str:

    #
    #
    #

    fs = Filesystem(input_data[0])
    fs.defragment()

    return fs.get_checksum()

################################################################################
# END
################################################################################
