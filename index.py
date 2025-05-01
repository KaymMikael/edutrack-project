from system import *

# Map menu options to corresponding functions
menuActions = {
    1: registerStudent,
    2: displayAllStudents,
    3: updateStudent,
    4: displayOneStudent,
    5: deleteStudent,
    6: exitProgram,
}

print("Welcome to EduTrack")
while True:
    displayMenu()
    messagePrompt = f"Enter your choice 1-{len(menuList)}: "
    try:
        choice = int(input(messagePrompt))
        action = menuActions.get(choice)  # Get the corresponding function
        if action:
            action()  # Call the function
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Invalid input type, please try again.")
