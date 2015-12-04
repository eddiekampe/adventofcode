import sys
import hashlib

secret = open("input.txt", "r").readline()


def positive_number_generator():  # Lazy evaluation
    for x in xrange(sys.maxint):
        yield x

for num in positive_number_generator():
    md5 = hashlib.md5(secret + str(num)).hexdigest()
    if md5.startswith("00000"):
        print num
        break
