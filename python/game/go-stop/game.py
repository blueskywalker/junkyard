import hwatoo
import random


class CardScoringBoard:

    def __init__(self):
        self.score = 0
        self.cards = { 20: {}, 10 : {}, 5 : {}, 1 : {}}
        self.numOfGo = 0

    def add(self, card):
        self.cards[card.month].add(card)
        self.calcScore()

    def calc_score(self):
        self.score = self.numOfGo
        self.score += self.pee_score() 
        self.score += self.ribon_score() 
        self.score += self.ten_score() 
        self.score += self.gwang_score()

    def pee_score(self):
        peelist = self.cards[1]
        double = peelist & hwatoo.double_pee
        n = len(peelist) + len(double)

        if n < 10:
            return 0

        return n - 9

    def is_dan(self,danlist):
        data=set(map(lambda x:x[0],self.cards[5]))
        hongdan = data & danlist
        if len(hongdan) == 3:
            return True
        else:
            return False

    def is_hongdan(self):
        return self.is_dan(hwatoo.hong_dan)

    def is_chungdan(self):
        return self.is_dan(hwatoo.chung_dan)

    def is_chodan(self):
        return self.is_dan(hwatoo.cho_dan)

    def ribon_score(self):
        n = 0
        if is_hongdan():
            n += 3
        if is_chungdan():
            n += 3
        if is_chodan():
            n += 3
        size = len(self.cards[5])
        if size > 4:
            n += size-4
        return n

    def is_godori(self):
        data = map(lambda x:x[0],self.cards[10])
        godori = data & hwatoo.godori
        if len(godori) == 3:
            return True
        return False

    def ten_score(self):
        n = 0
        if is_godori():
            n += 5

        size = len(self.cards[10])
        if size > 4:
            n += size-4
        return n

    def gwang_score(self):

        data = map(lambda x:x[0],self.cards[20])
        size = len(data)
        n = 0
        if size > 2:
            n = size

        if n == 3 and 45 in data:
            n = 2

        return n


    def __str__(self):
        out=[]
        out.append("SCORE : %d with GO (%d) " % (self.score,self.numOfGo))
        out.append("GWANG : " + str(map(str, self.cards[20])))
        out.append("TEN : " + str(map(str, self.cards[10])))
        out.append("RIBON : " + str(map(str, self.cards[5])))
        out.append("PEE : " + str(map(str, self.cards[1])))
        return "\n".join(out)


class Player:

    def __init__(self):
        self.holding = []
        self.scoring = CardScoringBoard()

    def assign(self, cards):
        self.holding.extend(cards)

    def str_holding(self):
        return ",".join(["(%s[%d])" % (x.desc,x.id) for x in self.holding])

    def __str__(self):
        return '\n'.join([str(self.scoring),self.str_holding()])

    def play(self):
        pass


class ComputerPlayer(Player):

    def __str__(self):
        return str(self.scoring)

    def paly(self):
        pass


class TwoPlayerGoStopGame:

    def __init__(self):
        self.cards = hwatoo.hwa_too[:]
        random.shuffle(self.cards)
        self.floor = []

        self.player1 = Player()
        self.player2 = ComputerPlayer()

        for _ in range(2):
            self.player1.assign([self.cards.pop() for _ in range(5)])
            self.player2.assign([self.cards.pop() for _ in range(5)])
            self.floor.extend([self.cards.pop() for _ in range(4)])
    
    def play(self):
        while True:
            print self
            self.player1.play()
            self.cards.pop()
            print self
            self.player2.play()
            self.cards.pop()
            if len(self.cards) == 0:
                break

    def __str__(self):
        out = []
        out.append(str(self.player2))
        out.append(str(map(str, self.floor)))
        out.append(str(self.player1))
        return '\n'.join(out)

game = TwoPlayerGoStopGame()
game.play()

