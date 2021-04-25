def get_possible_characters():
    possibles = ''
    with open('config.txt', 'r') as f:
        possible_list = list(f.readline())
        
        del possible_list[:20]
        for i in possible_list:
            possibles += i
        
        return possibles

class Key():

    def __init__(self, possible_characters):
        self.possibles = possible_characters
        self.key = []
        self.keyCharactersPosition = {}

    def add(self):
        self.key.append(self.possibles[0])
        self.keyCharactersPosition[len(self.keyCharactersPosition)] = 0
    
    def reset(self, index=-1):
        if index == -1:
            c = 0
            for i in self.key:
                self.keyCharactersPosition[c] = 0
                self.key[c] = self.possibles[0]
                c += 1
        else:
            self.keyCharactersPosition[index] = 0
            self.key[index] = self.possibles[0]

    def next(self, index=0):
        try:
            self.keyCharactersPosition[index] += 1
            self.key[index] = self.possibles[self.keyCharactersPosition[index]]
        
        except IndexError:
            self.up(index)
    
    def up(self, index):
        allAtEndCounter = 0
        for i in self.key:
            if i == self.possibles[len(self.possibles) - 1]:
                allAtEndCounter += 1

        if allAtEndCounter == len(self.key):
            self.add()
            self.reset()
        
        else:
            self.reset(index)
            self.next(index + 1)

    def convertToString(self):
        converted = ''
        for i in self.key:
            converted += i
        return converted