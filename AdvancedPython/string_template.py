from datetime import date
from string import Template


def main():

    # String formating using format method
    niceWords = "Today {0} that is {1} will be a wonderfull day".format(
        date.today().strftime("%d-%b-%Y"), date.today().strftime("%A"))
    print(niceWords)

    # build string interpolation using Template class
    # require import
    tempStr = Template("The ${fox} jumps over the lazy ${dog}")

    # use substitute with directly passing as key value pairs
    printData = tempStr.substitute(fox="quick brown fox", dog="Rapid Rabbit")
    print("option 1 : ", printData)

    # use a dict to store the value for the placholder text used in the template
    data = {
        "fox": "quick brown fox",
        "dog": "Rapid Rabbit"
    }
    printData2 = tempStr.substitute(data)
    print("option 2 : ", printData)


main()
