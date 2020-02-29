#!/bin/python3


import os


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # print("{} {} {}".format((x1 - x2), (v2 - v1), (x1 - x2) % (v2 - v1)))
    if x2 - x1 < 0 :
        return "NO"
    elif (x1 - x2) % (v2 - v1) == 0 : #and (x1 - x2) > 0:
        return "YES"
    else :
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
