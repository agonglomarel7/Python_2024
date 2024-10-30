
def hello():
    print("Hello, world!")


# to call a function
hello()


def user_age():
    age = int(input("How old are you? "))
    age_seconds = age *365*24*60*60

    print(age_seconds)


user_age()