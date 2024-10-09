#!/usr/bin/python3
if __name__ == "__main__":
<<<<<<< HEAD
    """Print the result of the addition of all arguments"""
    import sys

    argv = sys.argv
    r_sum = 0

    for i in range(1, len(argv)):
        r_sum += int(argv[i])

    print("{}".format(r_sum))
=======
    from sys import argv
    sum = 0
    for count in range(1, len(argv)):
        sum += int(argv[count])
    print("{}".format(sum))
>>>>>>> master
