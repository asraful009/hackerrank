#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    k = max(list(h[ord(x)-ord('a')] for x in word))
    l = len(word)
    # print("{} {} {}".format(k, l, l*k))

    return k*l
if __name__ == '__main__':
    # fptr = open("./output/my.txt", 'w')

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
