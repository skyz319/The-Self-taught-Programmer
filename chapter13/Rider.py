from chapter13.Horse import *

class Rider:
    def __init__(self, riderName):
        self.name = riderName
        self.horses = []

    def riderHorses(self):
        """
        骑车拥有的马匹数量
        :return:
        """
        if len(self.horses) == 0:
            print("Rider did not have horse!")
        else:
            print("Have %d horses, horese is:" %(len(self.horses)))
            for v in self.horses:
                # v.who_am_i
                print(v.name)