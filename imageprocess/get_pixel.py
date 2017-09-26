#-*- coding:utf-8 -*-

import numpy as np
import sys

from PIL import Image


def get_pixel(path):
    f = Image.open(path)
    f2 = f.convert('L')
    im_array = np.array(f2)
    np.savetxt("pixels.csv", im_array, delimiter=",", fmt='%s')


def main():
    get_pixel(sys.argv[1])


if __name__ == "__main__":
    main()
