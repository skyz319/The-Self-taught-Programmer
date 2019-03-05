class Card:
    suits = ["黑桃",
             "红心",
             "方块",
             "梅花"]

    values = [None, None, "2", "3",
              "4", "5", "6", "7", "8",
              "9", "10", "J", "Q", "K", "A"]

    def __init__(self, v, s):
        """suit和value都为整型"""
        self.value = v
        self.suit = s

    # lt 小于运算
    def __lt__(self, c2):
        """当前牌是否小于传入的牌，若相等，比花色"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False

    def __gt__(self, c2):
        """当前牌是否大于传入的牌，若相等，比花色"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
        + self.suits[self.suit]

        return v