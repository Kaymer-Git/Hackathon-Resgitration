workshops = ("Game Design", "AI Chatbots", "Robotics")
checked_in = set(["sam"])
registrations = {
    "maya": "Game Design",
    "jordan": "AI Chatbots",
    "alex": "Robotics",
    "sam": "Game Design",
    "taylor": "AI Chatbots"
}
name = input("Enter student name: ")
if name in registrations:
    print("This student is already registered.")