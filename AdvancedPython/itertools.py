import itertools

# some of the utility function part of itertools


def main():

    thougths = ["Great", "Day", "!"]
    # convert the list into iter, it will create a loop back to start
    iterator = itertools.cycle(thougths)
    i = 1
    while i < 10:
        # if condition is not set, this will be infinite loop
        print(next(iterator), end=" ")
        i += 1


main()
