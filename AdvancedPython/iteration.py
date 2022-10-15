# Built in function like iter, enumerate, range, etc to help with functionality in python

# method declaration for a simple use case of iter, will be invoked from main functtion
def iterateList():
    # add names to list object
    names = ['Jack Sparrow', 'Hector Barbossa',
             'Davy Jones', 'Jack the Monkey']

    # convert list into iter, and loop by calling the next on iterNames
    # Loop does not run forever, it calls StopIteration without handling the while loop
    iterNames = iter(names)
    print("Simple flow : ")
    while True:
        try:
            print(next(iterNames))
        except:
            break

# one more Use Case for iter will be to use inside the class


class Pirates:
    names = []

    def __init__(self, pirateNames):
        self.names = pirateNames  # assign the list from the argument
        self.max = len(names)  # keep the count of the list

    def __iter__(self):
        self.num = 0
        return self  # return the object

    def __next__(self):
        if (self.num >= self.max):
            raise StopIteration
        # get the list for the index that is currently active and increment the number
        # for self.num
        val = names[self.num]
        self.num += 1
        return val

# adavance use case using a class which is declared above, will be invoked from main funciton


def iterateListAdv():
    # call the class and iterate the names in it
    names = ['Jack Sparrow', 'Hector Barbossa',
             'Davy Jones', 'Jack the Monkey']
    print_names = Pirates(names)
    print_name_iter = iter(print_names)
    print(next(print_name_iter))
    print(next(print_name_iter))
    print(next(print_name_iter))
    print(next(print_name_iter))
    print(next(print_name_iter))


# entry level method
def main():

    # iterateList()
    iterateListAdv()


# call main
if __name__ == "__main__":
    main()
