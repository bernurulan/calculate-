import random
import os

G_S = 7
EMPTY = '.'
HIT = 'H'
MISS = 'M'
SHIP = 'S'
SHIP_SIZES = [3, 2, 2, 1, 1, 1, 1]

# Game boards
board = [[EMPTY] * G_S for _ in range(G_S)]
display_board = [[EMPTY] * G_S for _ in range(G_S)]
ships = []
sunk_ships = 0
shots_taken = 0

name = input("Enter your name: ")

# ships randomly
for size in SHIP_SIZES:
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        row, col = random.randint(0, G_S - 1), random.randint(0, G_S - 1)

        if direction == 'horizontal' and col + size <= G_S and all(
                board[row][col + i] == EMPTY for i in range(size)):
            for i in range(size):
                board[row][col + i] = SHIP
            ships.append([(row, col + i) for i in range(size)])
            placed = True

        if direction == 'vertical' and row + size <= G_S and all(
                board[row + i][col] == EMPTY for i in range(size)):
            for i in range(size):
                board[row + i][col] = SHIP
            ships.append([(row + i, col) for i in range(size)])
            placed = True

#
while sunk_ships < len(SHIP_SIZES):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    # player's view
    print("  A B C D E F G")
    print("  -------------")
    for i, row in enumerate(display_board):
        print(f"{i + 1} {' '.join(row)}")

    shot = input("Enter your shot coordinates (e.g., A1): ").upper()
    col, row = ord(shot[0]) - ord('A'), int(shot[1]) - 1

    if 0 <= col < G_S and 0 <= row < G_S:
        if board[row][col] == SHIP:
            display_board[row][col] = HIT
            board[row][col] = EMPTY
            print("You hit a ship!")
            for ship in ships:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        sunk_ships += 1
                        print("You sunk a ship!")
                    break
        elif board[row][col] == EMPTY:
            display_board[row][col] = MISS
            print("You missed.")
        else:
            print("You already shot here!")
        shots_taken += 1
    else:
        print("Invalid coordinates. Try again.")

print(f"Game over! You took {shots_taken} shots to sink all the ships.")

# Ask to play again
if input("Do you want to play again? (yes/no): ").lower() == 'yes':
    board = [[EMPTY] * G_S for _ in range(G_S)]
    display_board = [[EMPTY] * G_S for _ in range(G_S)]
    ships = []
    sunk_ships = 0
    shots_taken = 0
    for size in SHIP_SIZES:
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical'])
            row, col = random.randint(0, G_S - 1), random.randint(0, G_S - 1)

            if direction == 'horizontal' and col + size <= G_S and all(
                    board[row][col + i] == EMPTY for i in range(size)):
                for i in range(size):
                    board[row][col + i] = SHIP
                ships.append([(row, col + i) for i in range(size)])
                placed = True

            if direction == 'vertical' and row + size <= G_S and all(
                    board[row + i][col] == EMPTY for i in range(size)):
                for i in range(size):
                    board[row + i][col] = SHIP
                ships.append([(row + i, col) for i in range(size)])
                placed = True
else:
    print("Thanks for playing!")
