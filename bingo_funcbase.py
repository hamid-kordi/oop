from random import randint

random_integer = randint(0, 9)


def check_answer(answer):
    if answer > random_integer:
        return [True, "you shoukd choose smaller integer "]
    elif answer < random_integer:
        return [True, "you should select larger integer "]
    elif answer == random_integer:
        return [False, "bingo!"]


result = []
iterable = True
while iterable:
    client_guss = int(input("enter your integer"))
    result = check_answer(client_guss)
    print(result[1])
    iterable = result[0]
