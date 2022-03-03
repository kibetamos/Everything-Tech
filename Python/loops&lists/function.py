# Notice that the first line of output is the line that is not part of the
# function. That is because the function does not run until it is called,
# and it is called after the print() function that outputs “Sad not to be
# part of the function. I’ve been outdented.”


def main():
    print("I am part of the function.")
    print("I am also part of the function.")
    print("Hey, me too!")
print("Sad not to be part of the function. I've been outdented.")
main()



def main():
    today = "Monday"
    print("Today is", today, ".")
main()

def main():
    today = input("What day is it? ")
    print("Wow! Today is ", today, "? Awesome!", sep="")
main()


def main():
    your_name = input("What is your name? ")
    print("Hello, ", your_name, "!", sep="")
main()