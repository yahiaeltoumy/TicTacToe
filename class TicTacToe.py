import random

val = [' ' for i in range(16)]


class player:
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn
        self.moves = []
        self.chance = 0

    def play(self):
        if (self.turn == 1):
            while (1):
                try:
                    print(f"Player {self.name}  turn. Choose your Block : ", end="")  # takes input from the player
                    self.chance = int(input())
                except ValueError:  # prints message if a non integer is inputted
                    print("Invalid Input!!! Try Again")
                    continue

                if self.chance < 1 or self.chance > 16:  # prints message if a number out of range from the list is inputted
                    print("Invalid Input!!! Try Again")
                    continue

                if val[self.chance - 1] != ' ':  # prints message if the position is already taken
                    print("Oops! The Place is already occupied. Try again!!")
                    continue
                val[self.chance - 1] = self.name
                self.moves.append(self.chance)
                break
    def computer(self):
        if (self.turn == 1):
            while (1):
                try:
                    print(f"Player {self.name}  turn. Choose your Block : ", end="")  # takes input from the player
                    self.chance = random.choice(range(1,17))
                except ValueError:  # prints message if a non integer is inputted
                    continue

                if self.chance < 1 or self.chance > 16:  # prints message if a number out of range from the list is inputted
                    continue

                if val[self.chance - 1] != ' ':  # prints message if the position is already taken
                    continue
                val[self.chance - 1] = self.name
                self.moves.append(self.chance)
                break
    def switch(self):
        if (self.turn == 1):
            self.turn = 0
        else:
            self.turn = 1

    def check_Victory(self):  # compares list of all moves made by the current player with all possible winning combinations.
        solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5, 9, 13], [2, 6, 10, 14],
                    [3, 7, 11, 15], [4, 8, 12, 16], [1, 6, 11, 16], [4, 7, 10, 13]]
        for i in solution:
            if all(j in self.moves for j in i):
                return True


def check_Tie(x,
              y):  # if the number of moves made by each player is equal to all the squares on the board then it is a tie
    if len(x) + len(y) == 16:
        return True
    return False


def mytictactoe(val):  # displays the "val" list as a matrix
    print("\n")
    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}".format(val[0], val[1], val[2], val[3]))
    print('\t_____|_____|_____|_____')

    print("\t     |     |     |")
    print("\t  {}  |  {}  |  {}  |  {}".format(val[4], val[5], val[6], val[7]))
    print('\t_____|_____|_____|_____')
    print("\t  {}  |  {}  |  {}  |  {}".format(val[8], val[9], val[10], val[11]))
    print("\t     |     |     |")
    print('\t_____|_____|_____|_____')
    print("\t  {}  |  {}  |  {}  |  {}".format(val[12], val[13], val[14], val[15]))
    print("\t     |     |     |")
    print("\n")
p1=player('X',1)
p2=player('O',1)
p3=player('O',1)
L=input("play against a computer? (Y/N): ",)
L=L.upper()
if(L=='N'):
    mytictactoe(val)
    while (1):
        p1.play()
        mytictactoe(val)
        if (p1.check_Victory()):
            print("Player X wins!")
            break
        p2.play()
        mytictactoe(val)
        if (p2.check_Victory()):
            print("player O wins!")
            break
        if (check_Tie(p1.moves, p2.moves)):
            print("It's a Tie!")
            break
else:
    mytictactoe(val)
    while (1):
        p1.play()
        mytictactoe(val)
        if (p1.check_Victory()):
            print("Player X wins!")
            break
        p3.computer()
        mytictactoe(val)
        if (p3.check_Victory()):
            print("player O wins!")
            break
        if (check_Tie(p1.moves, p3.moves)):
            print("It's a Tie!")
            break