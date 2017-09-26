#-*- coding:utf-8 -*-

import sys
import numpy as np

from PIL import Image


def filter_pixels(path, watermark):
    f = Image.open(path)
    f2 = f.convert('L')
    im_array = np.array(f2)
    total_white_pixel = 0
    for x_arr in im_array:
        for i, pixel in enumerate(x_arr):
            if int(pixel) >= int(watermark):
                x_arr[i] = 255
                total_white_pixel += 1
            else:
                x_arr[i] = 0
    f3 = Image.fromarray(im_array)
    print "白色像素点个数: %s" % total_white_pixel
    f3.save('filterred.jpg')


def main():
    filter_pixels(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
