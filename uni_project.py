import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def eng_level():
    print("english level:")
    print("1. Beginner")
    print("2. Elementary")
    print("3. Pre-Intermediate")
    print("4. Intermediate")
    print("5. Upper-Intermediate")
    print("6. Advanced")

    while True:
        try:
            choice = int(input("your choice (1-6): "))
            if 1 <=choice<= 6:
                levels = ["Beginner", "Elementary", "Pre-Intermediate", "Intermediate",
                          "Upper-Intermediate", "Advanced"]
                return levels[choice - 1]
            else:
                print("select between 1 and 6.")
        except ValueError:
            print("enter a valid number.")
def faculty_name():
    print("select your specialty:")
    print("1. Computer Engineering 2500$")
    print("2. Artificial Intelligence 2200$")
    print("3. Psychology 1900$")
    print("4. Journalism 1700$")
    print("5. International Relations 2200$")
    print("6. Law 1800$")
    print("7. Management 2200$")
    print("8. Medicine 3300$")

    while True:
        try:
            choice = int(input("your choice (1-8): "))
            if 1 <=choice<= 8:
                s=[
                    ("Computer Engineering", 2500),
                    ("Artificial Intelligence", 2200),
                    ("Psychology", 1900),
                    ("Journalism", 1700),
                    ("International Relations", 2200),
                    ("Law", 1800),
                    ("Management", 2200),
                    ("Medicine", 3300)
                ]
                return s[choice - 1]
            else:
                print("select between 1 and 8.")
        except ValueError:
            print("Please enter a valid number.")
def dis(ort):
    if 140 <=ort<= 155:
        return 0.05
    elif 156 <=ort<= 174:
        return 0.10
    elif 175 <=ort<= 199:
        return 0.25
    elif 200 <=ort<= 209:
        return 0.50
    elif 210 <=ort<= 218:
        return 0.75
    elif 219 <=ort<= 240:
        return 1.00
    else:
        return 0.00

def main():
    last_name = input("last name: ")
    first_name = input("first name: ")
    print("school education certificate?")
    print("0. Not available")
    print("1. Available")

    while True:
        try:
            cert_choice = int(input("your choice (0 or 1): "))
            if cert_choice in [0, 1]:
                has_certificate = bool(cert_choice)
                break
            else:
                print("Invalid, enter 0 or 1.")
        except ValueError:
            print("enter a valid number.")

    while True:
        try:
            ort= int(input("your ORT score: "))
            if 0 <=ort<= 240:
                break
            else:
                print("ORT score must be between 0 and 240.")
        except ValueError:
            print("enter a valid number.")

    level = eng_level()

    clear_screen()

    if not has_certificate:
        print("you cannot be admitted to Ala-Too University without a school education certificate.")
        return

    if ort< 110:
        print("your ORT score is too low ")
        return

    need= ["Intermediate", "Upper-Intermediate", "Advanced"]
    if level not in need:
        print(
            f"English level ({level}) too low for admission. offered a one year Foundation Course AIU for English.")
        return
    print(f"Congratulations {first_name} {last_name}, you are recommended for admission to Ala-Too University!")
    clear_screen()
    s, cost = faculty_name()

    clear_screen()
    discount = dis(ort)
    discountt= cost * (1 - discount) #have to check

    if discount > 0:
        print(
            f"Dear {first_name} {last_name}, congrats! You have been admitted to the {s} program at Ala-Too.")
        print(
            f"The cost of your tuition with a {int(discount * 100)}% discount will be {int(discountt)}$ per year.")
    else:
        print(
            f"Dear {first_name} {last_name}, congrats! You have been admitted to the {s} program at Ala-Too.")
        print(f"The cost of your tuition will be {cost}$ per year.")


if __name__ == "__main__":
    main()
