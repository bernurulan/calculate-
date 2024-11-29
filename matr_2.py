import random
import os

gridsize = 7
EM = '.'
HIT = 'H'
MISS = 'M'
shipS = [3, 2, 2, 1, 1, 1, 1]
board = [[EM] * gridsize  for _ in range(gridsize)]
ships = []
sunk_ships = 0
shots_taken = 0

name = input("your name: ")

#random
for size in shipS :
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        row, col = random.randint(0, gridsize - 1), random.randint(0,gridsize - 1)

        if direction == 'horizontal' and col + size <= gridsize and all(
                board[row][col + i] == EM for i in range(size)):
            for i in range(size):
                board[row][col + i] = 'S'
            ships.append([(row, col + i) for i in range(size)])
            placed = True

        if direction == 'vertical' and row + size <= gridsize and all(
                board[row + i][col] == EM for i in range(size)):
            for i in range(size):
                board[row + i][col] = 'S'
            ships.append([(row + i, col) for i in range(size)])
            placed = True

#loop
while sunk_ships < len(shipS):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print("  A B C D E F G")
    print("  -------------")
    for i, row in enumerate(board):
        print(f"{i + 1} {' '.join(row)}")

    shot = input("your shot coordinates (e.g., A1): ").upper()
    col, row = ord(shot[0]) - ord('A'), int(shot[1]) - 1

    if 0 <= col < gridsize and 0 <= row < gridsize:
        if board[row][col] == 'S':
            board[row][col] = HIT
            print("You hit a ship!")
            for ship in ships:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        sunk_ships += 1
                        print("You sunk a ship!")
                    break
        elif board[row][col] == EM:
            board[row][col] = MISS
            print("You missed.")
        shots_taken += 1
    else:
        print("Invalid coordinates. Try again.")

print(f"Game over! You took {shots_taken} shots to sink all the ships.")

#play again
if input("Do you want to play again? (yes/no): ").lower() == 'yes':
    board = [[EM] * gridsize for _ in range(gridsize)]
    ships = []
    sunk_ships = 0
    shots_taken = 0
    for size in shipS:
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical'])
            row, col = random.randint(0, gridsize - 1), random.randint(0, gridsize - 1)

            if direction == 'horizontal' and col + size <= gridsize and all(
                    board[row][col + i] == EM for i in range(size)):
                for i in range(size):
                    board[row][col + i] = 'S'
                ships.append([(row, col + i) for i in range(size)])
                placed = True

            if direction == 'vertical' and row + size <= gridsize and all(
                    board[row + i][col] == EM for i in range(size)):
                for i in range(size):
                    board[row + i][col] = 'S'
                ships.append([(row + i, col) for i in range(size)])
                placed = True
else:
    print("Thanks for playing!")

