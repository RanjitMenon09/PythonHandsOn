import itertools
import operator
# some of the utility function part of itertools


def cycle_usage():
    thougths = ["Great", "Day", "!"]
    # convert the list into iter, it will create a loop back to start
    iterator = itertools.cycle(thougths)
    i = 1
    while i < 10:
        # if condition is not set, this will be infinite loop
        print(next(iterator), end=" ")
        i += 1


def accumalate_multiply():
    vals = [5, 2, 7, 3, 9, 6]
    # using operator import to use multiply function.
    acc = itertools.accumulate(vals, operator.mul)
    print('\n')
    print("accumaltor multiplication result : ", list(acc))


def accumlate_lambda():
    vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = itertools.accumulate(vals, lambda acc, val: acc+val)
    print('\n')
    print("accumalator lambda addition :", list(result))


def chain_usecase():
    val = "Today is a Great Day!"
    res = itertools.chain(val)
    print('\n')
    print("Chain usecase : ", list(res))


def mod_of_2(n):
    return n % 2 == 0


# not working as expected, why the result is not showing only the one which was retured as true
# here 2 was returning true and 5 was false, so it should return only true, but it returnes everything
# in list
def dropwhile_usecase():
    val = [2, 5, 3, 4, 7, 8, 9]
    print('\n')
    print("dropwhile mod :", list(itertools.dropwhile(mod_of_2, val)))


def main():
    cycle_usage()
    accumalate_multiply()
    accumlate_lambda()
    chain_usecase()
    dropwhile_usecase()


main()
