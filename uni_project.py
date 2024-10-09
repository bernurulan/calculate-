import os


# Function to clear the screen
def clear_screen():
    # Clears the screen (works on both Windows and Unix systems)
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to get the English level from user input
def get_english_level():
    print("Please select your English proficiency level:")
    print("1. Beginner")
    print("2. Elementary")
    print("3. Pre-Intermediate")
    print("4. Intermediate")
    print("5. Upper-Intermediate")
    print("6. Advanced")

    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                levels = ["Beginner", "Elementary", "Pre-Intermediate", "Intermediate",
                          "Upper-Intermediate", "Advanced"]
                return levels[choice - 1]
            else:
                print("Invalid choice. Please select between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")


# Function to get the specialty from user input
def get_specialty():
    print("Please select your desired specialty:")
    print("1. Computer Engineering - 2500$")
    print("2. Artificial Intelligence - 2200$")
    print("3. Psychology - 1900$")
    print("4. Journalism - 1700$")
    print("5. International Relations - 2200$")
    print("6. Law - 1800$")
    print("7. Management - 2200$")
    print("8. Medicine - 3300$")

    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                specialties = [
                    ("Computer Engineering", 2500),
                    ("Artificial Intelligence", 2200),
                    ("Psychology", 1900),
                    ("Journalism", 1700),
                    ("International Relations", 2200),
                    ("Law", 1800),
                    ("Management", 2200),
                    ("Medicine", 3300)
                ]
                return specialties[choice - 1]
            else:
                print("Invalid choice. Please select between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")


# Function to calculate discount based on ORT score
def calculate_discount(ort_score):
    if 140 <= ort_score <= 155:
        return 0.05
    elif 156 <= ort_score <= 174:
        return 0.10
    elif 175 <= ort_score <= 199:
        return 0.25
    elif 200 <= ort_score <= 209:
        return 0.50
    elif 210 <= ort_score <= 218:
        return 0.75
    elif 219 <= ort_score <= 240:
        return 1.00
    else:
        return 0.00


# Main function
def main():
    # Get applicant's information
    last_name = input("Enter your last name: ")
    first_name = input("Enter your first name: ")

    # School education certificate
    print("Do you have a school education certificate?")
    print("0. Not available")
    print("1. Available")

    while True:
        try:
            cert_choice = int(input("Enter your choice (0 or 1): "))
            if cert_choice in [0, 1]:
                has_certificate = bool(cert_choice)
                break
            else:
                print("Invalid choice. Please enter 0 or 1.")
        except ValueError:
            print("Please enter a valid number.")

    # ORT score
    while True:
        try:
            ort_score = int(input("Enter your ORT score: "))
            if 0 <= ort_score <= 240:
                break
            else:
                print("ORT score must be between 0 and 240.")
        except ValueError:
            print("Please enter a valid number.")

    # English level
    english_level = get_english_level()

    # Clear the screen for further processing
    clear_screen()

    # Check if the applicant is eligible
    if not has_certificate:
        print("Sorry, you cannot be admitted to Ala-Too University without a school education certificate.")
        return

    if ort_score < 110:
        print("Sorry, your ORT score is too low to be admitted to Ala-Too University.")
        return

    english_levels_needed = ["Intermediate", "Upper-Intermediate", "Advanced"]
    if english_level not in english_levels_needed:
        print(
            f"Your English level ({english_level}) is too low for admission. You are offered a one-year Foundation Course AIU to improve your English.")
        return

    # If all conditions are met
    print(f"Congratulations {first_name} {last_name}, you are recommended for admission to Ala-Too University!")

    # Get the specialty choice
    clear_screen()
    specialty, cost = get_specialty()

    # Clear the screen again and calculate discount
    clear_screen()
    discount = calculate_discount(ort_score)
    discounted_cost = cost * (1 - discount)

    # Display the final message
    if discount > 0:
        print(
            f"Dear {first_name} {last_name}, we congratulate you! You have been admitted to the {specialty} program at Ala-Too International University.")
        print(
            f"The cost of your tuition with a {int(discount * 100)}% discount will be {int(discounted_cost)}$ per year.")
    else:
        print(
            f"Dear {first_name} {last_name}, we congratulate you! You have been admitted to the {specialty} program at Ala-Too International University.")
        print(f"The cost of your tuition will be {cost}$ per year.")


# Run the program
if __name__ == "__main__":
    main()
