import argparse
import fileinput

def process(infile):
    symbols = set()
    for line in fileinput.input(infile):
        name = line.strip()
        for i in range(len(name)):
            for j in range(i+1, len(name)):
                abbrev = name[i].upper() + name[j]
                if abbrev not in symbols:
                    symbols.add(abbrev)
                    print(abbrev)
                    break
            else:
                continue
            break
        else:
            print(name)
            return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', default='-', help='input file')
    args = parser.parse_args()
    process(args.infile)

if __name__ == '__main__':
    main()
