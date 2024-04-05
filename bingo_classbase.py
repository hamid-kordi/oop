import random


class bingo:
    player_list = []

    def __init__(self):
        self.name = input("please enter your name: ")
        self.__rand_num = random.randint(0, 9)
        self.__guss_left = 3
        self.__win_state = False
        self.player_list.append(self)

    def check_answer(self):
        answer = int(input(f"{self.name} enter your guess : "))
        if answer > self.__rand_num:
            print(" __> you shoukd choose smaller integer")
        elif answer < self.__rand_num:
            print("--> you should select larger integer")
        elif answer == self.__rand_num:
            print(f"{self.name} bingo")
            self.__win_state = True
        self.__mine_guss_left()

    def __mine_guss_left(self):
        self.__guss_left -= 1

    def has_guss_left(self):
        if self.__guss_left > 0:
            return
        return False

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winer(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        return False


class GameController:
    def __init__(self) -> None:
        while True:
            for player in bingo.player_list:
                if not player.has_won():
                    player.check_answer()

            if bingo.game_has_winer():
                break

    


if __name__ == "__main__":
    while True:
        order = input("what do you want to do ?(add,start,exit)")
        if order == "add":
            bingo()
        elif order == "start":
            GameController()
        elif order == "exit":
            break
