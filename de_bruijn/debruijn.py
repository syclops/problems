import argparse
import fileinput

def lyndon(alph, length, prev):
    if prev == alph[-1]:
        return None
    word = ((length // len(prev) + 1) * prev)[:length]
    while word[-1] == alph[-1]:
        word = word[:-1]
    word = word[:-1] + word[-1].translate(str.maketrans(alph,
                                                        alph[1:] + alph[0]))
    return word

def de_bruijn(alph, length):
    seq = ''
    word = alph[0]
    while word:
        if length % len(word) == 0:
            seq += word
        word = lyndon(alph, length, word)
    return seq

def process(infile):
    for line in fileinput.input(infile):
        [alph_str, len_str] = line.strip().split()
        length = int(len_str)
        try:
            alph = ''.join(map(str, range(int(alph_str))))
        except:
            alph = alph_str
        print(de_bruijn(alph, length))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', default='-', help='input file')
    args = parser.parse_args()
    process(args.infile)

if __name__ == '__main__':
    main()
