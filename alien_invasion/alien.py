import argparse
import fileinput

def read_input(filename):
    dim = None
    inlines = []
    for line in fileinput.input(filename):
        if not dim:
            dim = int(line.strip())
        else:
            inlines.append(line.strip())
    return (dim, inlines)

def dropships(dim, field):
    rows = [0 for i in range(dim)]
    max_dim = 0
    for i in range(dim):
        cols = 0
        for j in range(dim):
            if field[i][j] == '-':
                rows[j] += 1
                if rows[j] > max_dim:
                    cols += 1
                    if cols > max_dim:
                        max_dim += 1
                        cols = 0
                else:
                    cols = 0
            else:
                rows[j] = 0
                cols = 0
    return max_dim ** 2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', default='-', help='input file')
    args = parser.parse_args()
    (dim, field) = read_input(args.infile)
    print('{} dropships!'.format(dropships(dim, field)))

if __name__ == '__main__':
    main()
