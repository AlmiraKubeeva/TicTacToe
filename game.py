from field import Field
class Game:
    def __init__(self):
        self.field = Field()

    def startGame(self):
        print("Выбери, будешь играть крестиком или ноликом: ", end='')
        choosing = " "
        while choosing != 'x' or choosing != 'o':
            try:
                choosing = input()
                if choosing != 'x' or choosing != 'o':
                    raise Exception("Ты должен выбрать либо х, либо о!")
            except Exception as e:
                print(e)
        while not self.field.haveTicOrTacWon():
            self.field.printField()
            #if choosing == "x":



