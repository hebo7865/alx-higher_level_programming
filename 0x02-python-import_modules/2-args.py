#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = len(argv) - 1
    if arguments == 0:
        print("{} arguments.".format(arguments))
    elif arguments == 1:
        print("{} argument:\n{}: {}".format(arguments, argv.index(argv[-1]), argv[-1]))
    else:
        print("{} arguments:".format(arguments))
        for i in range(arguments):
            print("{}: {}".format(argv.index(argv[i + 1]), argv[i + 1]))
