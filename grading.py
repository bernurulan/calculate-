def calculate_statistics(grades):
    #have to make starting point
    grade_A=grade_B=grade_C=grade_D=grade_F= 0
    #have to initialize the variables
    for grade in grades:
        if 90<=grade<=100:
            grade_A+=1
        elif 75<=grade<=89:
            grade_B+=1
        elif 60<=grade<=74:
            grade_C+=1
        elif 50<=grade<=59:
            grade_D+=1
        else:
            grade_F+=1
    #len collects grades and makes total
    total_grades = len(grades)
    #if totalgrade is 2 then 2/6 program calculates that and * 100 to know what part takes this totalgrades
    def percentage(count):
        return (count / total_grades) * 100 if total_grades > 0 else 0
        # Function to decide singular or plural for "grade"

    def count(count):
        return "grade" if count <= 1 else "grades"
    #decimal places makes the output more readable (.2f)
    print("A: {} {} ({:.2f}%)".format(grade_A, count(grade_A), percentage(grade_A)))
    print("B: {} {} ({:.2f}%)".format(grade_B, count(grade_B), percentage(grade_B)))
    print("C: {} {} ({:.2f}%)".format(grade_C, count(grade_C), percentage(grade_C)))
    print("D: {} {} ({:.2f}%)".format(grade_D, count(grade_D), percentage(grade_D)))
    print("F: {} {} ({:.2f}%)".format(grade_F, count(grade_F), percentage(grade_F)))
def main():
    num_grades = int(input("grade numbers: "))
    #have to collect grades (grades=[] is first empty)
    grades = []
    for i in range(num_grades):
        #user cannot move on to the next grade with while true
        while True:
            try:
                grade = int(input("Enter grade "+str(i + 1)+": "))
                if 0<=grade<=100:
                    grades.append(grade)
                    # append allows you to add an item to the end of a list.
                    break
                    #break infinite while loop
                else:
                    print("Grade between 0 and 100")
            except ValueError:
                print("enter a valid integer")

    # Calculate and print the statistics
    calculate_statistics(grades)

if __name__ == "__main__":
    main()
