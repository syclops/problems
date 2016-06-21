import argparse
import fileinput
import string
import sys

class Direction(object):

    NORTH = (-1, 0)
    SOUTH = (1, 0)
    EAST = (0, 1)
    WEST = (0, -1)

    @classmethod
    def reflect(cls, direction, mirror):
        """
        """
        if mirror == '/':
            return [-x for x in direction[::-1]]
        elif mirror == '\\':
            return direction[::-1]
        else:
            return (None, None)


class MirrorField(object):
    """
    Mirror field used for encryption and decryption of ASCII text.
    """

    DEFAULT_WIDTH = 13

    def __init__(self, keystr, width=DEFAULT_WIDTH, precompute=False):
        keylines = keystr.split('\n')
        assert len(keylines) == width
        for line in keylines:
            assert len(line) == width
        self.key = keylines
        self.width = width
        self.table = {}
        if precompute:
            self.compute_table()

    def compute_table(self):
        for char in (string.ascii_lowercase[:2*self.width] +
                     string.ascii_uppercase[:2*self.width]):
            self.table[char] = self.translate(char)

    def get_start(self, char):
        if char not in string.ascii_letters:
            return (None, None)
        index = ord(char)
        if char in string.ascii_uppercase:
            index -= ord('A')
        elif char in string.ascii_lowercase:
            index -= ord('a')
        if index >= 2 * self.width:
            return (None, None)
        if index < self.width:
            start = (index, 0)
            direction = Direction.EAST
        elif index < 2 * self.width:
            start = (self.width - 1, index - self.width)
            direction = Direction.NORTH
        if char in string.ascii_lowercase:
            start = Direction.reflect(start, '\\')
            direction = Direction.reflect(direction, '\\')
        return (start, direction)

    def update(self, coord, direction):
        [row, col] = coord
        if self.key[row][col] in '/\\':
            new_direction = Direction.reflect(direction, self.key[row][col])
        else:
            new_direction = direction
        new_coord = (row + new_direction[0], col + new_direction[1])
        return (new_coord, new_direction)

    def get_end(self, coord, direction):
        [row, col] = coord
        if row < 0:
            return chr(ord('a') + col)
        elif row == self.width:
            return chr(ord('A') + self.width + col)
        elif col < 0:
            return chr(ord('A') + row)
        elif col == self.width:
            return chr(ord('a') + self.width + row)
        return None

    def translate(self, char):
        (coord, direction) = self.get_start(char)
        while self.get_end(coord, direction) is None:
            (coord, direction) = self.update(coord, direction)
        return self.get_end(coord, direction)

    def convert(self, text):
        outstr = ''
        for char in text:
            if self.table:
                outstr += self.table[char]
            else:
                outstr += self.translate(char)
        return outstr


def read_input(infile):
    inlines = []
    for line in fileinput.input(infile):
        if (len(line[:-1]) != MirrorField.DEFAULT_WIDTH and
                len(inlines) < MirrorField.DEFAULT_WIDTH):
            return [None, None]
        inlines.append(line[:-1])
    return ['\n'.join(inlines[:-1]), inlines[-1]]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', default='-',
                        help='input file')
    parser.add_argument('--precompute', action='store_true',
                        help='use a precomputed table to translate characters')
    args = parser.parse_args()
    [keystr, text] = read_input(args.infile)
    field = MirrorField(keystr, precompute=args.precompute)
    print(field.convert(text))

if __name__ == '__main__':
    main()
