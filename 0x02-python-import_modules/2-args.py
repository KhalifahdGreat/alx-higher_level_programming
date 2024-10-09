#!/usr/bin/python3
<<<<<<< HEAD
import sys

if __name__ == "__main__":
    # Get the list of arguments excluding the script name
    argv = sys.argv[1:]
    num_args = len(argv)

    # Determine the correct singular or plural form and punctuation
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Print each argument with its position
    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
=======
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
>>>>>>> master
