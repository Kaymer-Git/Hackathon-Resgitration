workshops = ("Game Design", "AI Chatbots", "Robotics")
checked_in = set(["sam"])
registrations = {
    "maya": "Game Design",
    "jordan": "AI Chatbots",
    "alex": "Robotics",
    "sam": "Game Design",
    "taylor": "AI Chatbots"
}
student_name = input("Enter student name: ")
if student_name not in registrations:
    print("Student not found")
else:
    print(registrations[student_name])