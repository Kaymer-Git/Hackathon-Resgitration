workshops = ("Game Design", "AI Chatbots", "Robotics")
registrations = {
    "maya": "Game Design",
    "jordan": "AI Chatbots",
    "alex": "Robotics",
    "sam": "Game Design",
    "taylor": "AI Chatbots"
}
checked_in = set()
Exit = False
def menu():
    print("1. View Workshops")
    print("2. Look Up a Registration")
    print("3. Check In a Student")
    print("4. View Attendance Report")
    print("5. Remove One Check-In")
    print("6. Clear All Check-Ins")
    print("7. Register a New Student")
    print("8. Change a Student's Workshop")
    print("9. View Check-Ins for One Workshop")
    print("10. Exit")
    print()
def choice1():
    for i in workshops:
        print(f"{workshops.index(i) + 1}. {i}")
def choice2():
    student = input("Enter student name: ")
    if student in registrations:
        print(f"Workshop: {registrations[student]}")
    else:
        print("Student not found.")
def choice3():
    student = input("Enter student name: ")
    if student not in registrations:
        print("Student not found")
    else:
        if student in checked_in:
            print("This student is already checked in.")
        else:
            checked_in.add(student)
def choice4():
    print("========== ATTENDANCE REPORT ==========")
    print()
    print(f"Registered students: {len(registrations)}")
    print(f"Checked in: {len(checked_in)}")
    print(f"Still waiting for: {len(registrations) - len(checked_in)}")
    print()
    for i in registrations:
        if i not in checked_in:
            print(f"- {i}")
def choice5():
    student = input("Enter student name: ")
    if student in checked_in:
        pop = checked_in.pop()
        print(f"{pop} removed from checked in")
    else:
        print("There are no check-ins to remove.")
def choice6():
    rm = input("You sure you want to remove all check-ins: ")
    while rm != "yes" and rm != "no":
        rm = input("Error, do you want to remove all check-ins(yes/no): ")
    if rm == "yes":
        checked_in.clear()
    else:
        print("Reset canceled.")
def choice7():
    name = input("Enter student name: ")
    if name in registrations:
        print("This student is already registered.")
    else:
        for i in workshops:
            print(f"{workshops.index(i) + 1}. {i}")
        workshop = int(input("Enter workshop: "))
        while workshop != 1 and workshop != 2 and workshop != 3:
            print("Enter 1, 2, or 3")
            workshop = int(input("Enter workshop: "))
        if workshop == 1:
            registrations[name] = "Game Design"
        elif workshop == 2:
            registrations[name] = "AI Chatbots"
        elif workshop == 3:
            registrations[name] = "Robotics"
def choice8():
    student_name = input("Enter student name: ")
    if student_name not in registrations:
        print("Student not found")
    else:
        print(registrations[student_name])
        for i in workshops:
            print(f"{workshops.index(i) + 1}. {i}")
        workshop = int(input("Enter workshop: "))
        while workshop != 1 and workshop != 2 and workshop != 3:
            print("Enter 1, 2, or 3")
            workshop = int(input("Enter workshop: "))
        if workshop == 1:
            registrations[student_name] = "Game Design"
        elif workshop == 2:
            registrations[student_name] = "AI Chatbots"
        elif workshop == 3:
            registrations[student_name] = "Robotics"
def choice9():
    print("========== GAME DESIGN CHECK-INS ==========")
    print()
    print(f"Checked_in: {len(checked_in)}")
    for i in checked_in:
        if i in registrations:
            print(f"- {i}")
print("========== HACKATHON CHECK-IN ==========")
print()
while Exit == False:
    menu()
    choice = int(input("Enter choice: "))
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    elif choice == 3:
        choice3()
    elif choice == 4:
        choice4()
    elif choice == 5:
        choice5()
    elif choice == 6:
        choice6()
    elif choice == 7:
        choice7()
    elif choice == 8:
        choice8()
    elif choice == 9:
        choice9()
    elif choice == 10:
        print("Goodbye! Program ending...")
        Exit =True
    else:
        print("Enter number from 1 ~ 10")