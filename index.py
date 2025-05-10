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

# welcome message
print("Welcome to EduTrack")

while True:
    displayMenu()  # Display the menu options to the user

    # Prompt user for input based on the number of available choices
    messagePrompt = f"Enter your choice 1-{len(menuList)}: "

    try:
        choice = int(input(messagePrompt))  # Get and convert user input to an integer
        action = menuActions.get(choice)  # Retrieve the corresponding function

        if action:
            action()  # Execute the function
        else:
            print("Invalid choice, please try again.")  # Handle invalid selections

    except ValueError:
        print(
            "Invalid input type, please try again."
        )  # Handle cases where input isn't a number
