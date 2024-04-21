class Options:
    def help_letter(self):
        pass

    def see_wrong(self):
        pass

    def undo_letter(self):
        pass


class User:
    full_letter = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "z",
        "w",
        "x",
        "y",
        "z",
    ]

    @classmethod
    def __dellet(cls, let):
        st = cls.full_letter
        st.remove(let)
        return st

    age = 6

    def __init__(self, name) -> None:
        self.name = name

    def guese(self, word):
        if len(word) < 3:
            raise ValueError("word most be more that 3 letter")
        else:
            self.__word = word
            self.general_word = word
            print("yes got it")
        self.len = len(word)

    def limit(self, gues_limit):
        self.count = gues_limit

    @classmethod
    def __deldel(cls):

        cls.age = cls.age - 1
        if cls.age >= 1:
            print(cls.age, " from age left")
        else:
            print("game over go out please")

    def guse_letter(self, letter):
        self.letter = letter
        left_letter = User.__dellet(letter)
        print(f"select after guese between this {left_letter}")

        word_guss = list(self.__word)
        list(set(word_guss))
        if letter in list(word_guss):
            print("ok that is right")
            word_guss.remove(letter)
            len_left = len(word_guss)
            print(f"left{len_left}")
            if len_left == 0:
                print("ok you win")
        else:
            print("ریدی مهندسی یه بار دیگه امتحان کن ")
            User.__deldel()


class Game:

    nam1 = input("enter the name of the first gammer  should guess word: ")
    nam2 = input("enter the name of the second gammer should guess letter: ")

    obj = User(nam1)
    obj1 = User(nam2)

    word = input(f"user{nam1} please enter your word : ")
    obj.guese(word)
    opt = input(f"user {nam2} do you want use options : ")
    if opt == "yes":
        print("basheh ")
    lett = input(f"{nam2} please enter the first guess     ")

    obj1.guse_letter(lett)
