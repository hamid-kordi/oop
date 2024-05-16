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

    # @classmethod
    # def __dellet(self, let):
    #     self.letter = let
    #     st = User.full_letter
    #     st.remove(self.letter)
    #     return st

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

    # @classmethod
    def __deldel():

        User.age = User.age - 1
        if User.age >= 1:
            print(User.age, " from age left")
        else:
            print("game over go out please")

    def guse_letter(self, letter,word):
        self.letter = letter
        
        word_guss = word
        word_guss = list(word_guss)
        (set(word_guss))
        
        if letter in list(word_guss):
            print("ok that is right")

        else:
            print("ریدی مهندس یه بار دیگه امتحان کن ")
            User.__deldel()


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
u = 1
while(u == 1):
    obj1.guse_letter(lett,word=obj.general_word)
    u = int(input('do you want to resume : '))
    lett = input('enter on letter')
