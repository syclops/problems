import argparse
import fileinput
from PIL import Image
import statistics
import tqdm

def process(image, outfile):
    width, height = image.size
    pixels = image.load()
    for y in range(height):
        for x in range(width):
            if pixels[x, y] < 128:
                diff_val = pixels[x, y]
                pixels[x, y] = 0
            else:
                diff_val = pixels[x, y] - 255
                pixels[x, y] = 255
            if x + 1 < width:
                pixels[x+1, y] += round(diff_val * 7/16)
            if y + 1 < height:
                if x > 0:
                    pixels[x-1, y+1] += round(diff_val * 3/16)
                pixels[x, y+1] += round(diff_val * 5/16)
                if x + 1 < width:
                    pixels[x+1, y+1] += round(diff_val/16)
    if outfile == '':
        image.show()
    else:
        image.save(outfile)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?', default='-', help='input file')
    parser.add_argument('outfile', nargs='?', default='', help='output file')
    args = parser.parse_args()
    image = Image.open(args.infile).convert('L')
    process(image, args.outfile)
    # out_image = Image.frombytes(mode='L', size=image.size, data=data)
    # out_image.save('output.png')

if __name__ == '__main__':
    main()
