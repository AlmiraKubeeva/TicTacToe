import random
class Field:
    def __init__(self):
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def setTic(self, x, y):
        self.field[x][y] = 'x'

    def setTac(self, x, y):
        self.field[x][y] = 'o'

    def showLine(self):
        print('-------------')

    def showStrOfField(self, numOfStr):
        print('| ', end="")
        for i in self.field[numOfStr]:
            print(i, '|', end=" ")
        print("\n")

    def printField(self):
        self.showLine()
        for i in range(0, 3):
            self.showStrOfField(i)
            self.showLine()

    def haveTicOrTacWon(self):
        for row in self.field:
            if row == ['x', 'x', 'x'] or row == ['o', 'o', 'o']:
                return True
        for i in range(0, 3):
            for j in range(0, 3):
                if self.field[i][j] == self.field[i + 1][j] and self.field[i][j] == self.field[i + 2][j]:
                    return True
            break

        if self.field[0][0] == self.field[1][1] and self.field[0][0] == self.field[2][2]:
            return True
        if self.field[0][2] == self.field[1][1] and self.field[0][2] == self.field[2][0]:
            return True
        return False

    def doStep(self, choosing):
        #to do
        x = random.randint(0, 2)
        y = random.randint(0, 2)