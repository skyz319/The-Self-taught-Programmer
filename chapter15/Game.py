from Deck import *
from Player import *

class Game:
    def __init__(self):
        name1 = input("P1 name:")
        name2 = input("P2 name:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} 赢得了这一局".format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} {} drew {}".format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("开始游戏！")
        while len(cards) >= 2:
            m = "q: 退出。 任一" + "键进行游戏:"
            response = input(m)

            if response == "q":
                break

            p1n = self.p1.name
            p2n = self.p2.name
            p1c = self.deck.rm_card()
            print("{} card: {}".format(p1n, p1c))
            p2c = self.deck.rm_card()
            print("{} card: {}".format(p2n, p2c))

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print("Game is over，{} Wins！".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "All have no"


game = Game()
game.play_game()


