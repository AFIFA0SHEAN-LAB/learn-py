print("-- STUDENT RECORD --")
print("--------------------\n")

student_amnt = int(input("How many students do you want on the record?: "))
top_student = None
top_avg = -1

students = {}

for _ in range(student_amnt):
    while True:
        student_name = input("Enter the name of the student: ")
        if not student_name.isalpha():
            print("Invalid name.")
            continue
        else:
            break

    while True:
        try:
            while True:
                math_grade = float(input("Enter their grade for math: "))
                if math_grade < 0 or math_grade > 100:
                    continue
                else:
                    break
            
            while True:
                sci_grade = float(input("Enter their grade for science: "))
                if sci_grade < 0 or sci_grade > 100:
                    continue
                else:
                    break
            
            while True:
                eng_grade = float(input("Enter their grade for english: "))
                if eng_grade < 0 or eng_grade > 100:
                    continue
                else: 
                    break
        except ValueError:
            print("Invalid input. Grades must be a number")
            continue   
        
        student_avg = (math_grade + sci_grade + eng_grade) / 3

        if student_avg > top_avg:
            top_avg = student_avg
            top_student = student_name

        break

    print(f"Name: {student_name}")
    print("--------------------")
    print("Grades:")

    students[student_name] = {
        "Math" : math_grade,
        "Science" : sci_grade,
        "English" : eng_grade,
    }

    print(students[student_name])
    print("--------------------")
    print(f"Average grade: {student_avg}")

while True:
    print("---- YOUR MENU ----")
    print("-------------------\n")
    print("1. Show top student\n2. Show all students\n3. Show only averages\n4. Exit")
    
    try:
        menu_opt = input("Pick an option (between 1-4): ")

        if menu_opt == "1":
            print("-- TOP STUDENT --")
            print(top_student)
            print(students[top_student])
            print(top_avg)
            print("------------------")
        elif menu_opt == "2":
            print("-- ALL STUDENTS --")
            print("------------------\n")

            for name, data in students.items():
                print(f"Name: {name}")
                print("------------------")
                print("Grades:")
                print(f"Math: {data['Math']}")
                print(f"Science: {data['Science']}")
                print(f"English: {data['English']}")
                print("------------------")
                avg = (data["Math"] + data["Science"] + data["English"]) / 3
                print(f"Average {avg}")
                print("------------------")
        elif menu_opt == "3":
            print("-- AVERAGES --")
            for name, data in students.items():
                avg = (data["Math"] + data["Science"] + data["English"]) / 3
                print(f"Name {name} -- Average: {avg}")
                print("------------------")
        elif menu_opt == "4":
            print("Thank you for using Python's student record!")
            break
        else:
            print("Invald input. Please enter a number between 1 and 4.")
            print("------------------")
            continue
    except ValueError:
        print("Invalid. Input must be a number between 1 and 4.")
        continue