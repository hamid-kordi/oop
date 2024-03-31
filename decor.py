def decor(func):
    def wrapper():
        print("start")
        func()
        print("end")

    return wrapper


@decor
def greeeting():
    print("this is main function")


# x = decor(greeeting)
# x()

greeeting()
