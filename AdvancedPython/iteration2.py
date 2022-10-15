# more iteration features like enumerate, range, zip, etc

def main():
    # range_example()
    # range_example2()
    # range_example3()
    # enumerate_example()
    zip_example()


def range_example():
    print("iterate over range :")
    for m in range(2**2):  # plain iteration of range
        print(m, end='\t')

    print('\n')


# convert range to a set
def range_example2():
    print("convert range into set, and using start and stop")
    set_number = set(range(1, 10, 2))  # start with 1 upto 10 and step by 2
    print(set_number)

# iterate a list using a range


def range_example3():
    print("Iterate the Season :")
    month = ["Spring", "Summer", "Autumn", "Winter"]
    for m in range(len(month)):
        print(m+1, month[m], end=" ")


# using enumerate to convert a dict to enumerate by seperating key,value
def enumerate_example():
    dictDaysOfWeek = {
        "Sunday": "रविवार",
        "Monday": "सोमवार",
        "Tuesday": "मंगलवार",
        "Wednesday": "वुधवार",
        "Thursday": "गुरुवार",
        "Friday": "शुक्रवार",
        "Saturday": "शनिवार"
    }

    # iterating only the dict, will return the index and key, but not the value
    # to get the value, need to use dict.items()
    for i, key in enumerate(dictDaysOfWeek):
        print("{0} = {1}".format(i, key))

    # use dictionary.items() to iterate the key value inside enumerate, only enumerting dict
    # will not return key/value pairs.
    for i, (english_days, hindi_days) in enumerate(dictDaysOfWeek.items()):
        print("{0}) {1} = {2}".format(i+1, english_days, hindi_days))

# zip to combine to list and return tuple


def zip_example():
    cardinal_direction = ['North', 'East', 'West', 'South']
    cardinal_direction_states = ['Himachal Pradesh',
                                 'West Bengal', 'Maharashtra', 'Kerala']

    # return a tuple of direction and state based on their index value.
    for m in zip(cardinal_direction, cardinal_direction_states):
        print(m)

    # use enumerate to iterate and make it more presentable
    for index, position in enumerate(zip(cardinal_direction, cardinal_direction_states), start=1):
        print(index, ") ", position[0], " = ", position[1])


main()
