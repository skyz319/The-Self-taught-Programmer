# 牌堆
from random import shuffle
from Card import *

class Deck:
    def __init__(self):
        self.cards = []
        # 牌最小值为2，最大值为A(14)
        for i in range(2, 15):
            # 4种花色
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        """从牌堆返回一张牌并从牌堆删除此牌"""
        if len(self.cards) == 0:
            return
        return self.cards.pop()
