#!/usr/bin/python3
from sys import argv
import math
""" this factors modual gets the first two factors of any number """


def isPrime(num):
    i = 3
    if num % 2 == 0:
        return False
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def factor(num):
    """
        This factor function
        gets the factors of
        a number and
        prints them out
    """
    if num % 2 == 0:
        i = 2
        print("{}={}*{}".format(num, int(num/i), i))
    else:
        sq = math.sqrt(num)
        if sq % 1 == 0:
            print("{}={}*{}".format(num, sq, int(num/sq)))
            return
        sq = int(sq) + 1
        for i in range(3, sq, +2):
            if num % i == 0:
                if isPrime(i):
                    print("{}={}*{}".format(num, int(num/i), i))
                    return


with open(argv[1]) as f:
    for line in f:
        factor(int(line))
