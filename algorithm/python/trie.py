
class Trie(object):
    def __init__(self):
        self.trie = dict()

    def add(self, word):
        if len(word) > 0:
            ch = word[0]
            if ch in self.trie:
                sub = self.trie[ch]
                sub.add(word[1:])
            else:
                sub = Trie()
                sub.add(word[1:])
                self.trie[ch] = sub

    def travel_all(self):
        ret=[]
        for ch in self.trie:
            sub = self.trie[ch]
            subset = sub.travel_all()

            if len(subset) > 0:
                ret.extend([''.join([ch, item]) for item in subset])
            else:
                ret.append(ch)

        return ret



data=['ape', 'apple', 'banana', 'balance','africa']


t=Trie()
for item in data:
    t.add(item)


print t.travel_all()



