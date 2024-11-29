# Fixed locations for the boxes (you can change these to test)
locations = [2, 4, 6]
weights = [213, 300, 200]  # Fixed weights summing to 713
print("Welcome to the Martian Cargo Finder Game!")
print("Find the 3 hidden boxes (locations 0 to 7). Good luck!\n") #n\ to separate sentences
# A simple function to move boxes in a predefined way
def move_boxes(locations):
    return [(loc + 1) % 8 for loc in locations]#need to shift them by 1
while True:
    guesses = list(map(int, input("Enter 3 guesses (space-separated): ").split())) #need user input

    if sorted(guesses) == sorted(locations):
        print("congrats, you ate that!")
        print(f"The weights of the cargo are: {weights}")
        print(f"Total weight: {sum(weights)} kg")
        break
    else:
        print("you missed it. The boxes have moved!")
        locations = move_boxes(locations)
