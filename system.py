import models  # Importing the models module
import manager  # Importing the manager module
from menu import *  # Importing everything from the menu module

# Creating an instance of StudentManager
studentManager = manager.StudentManager()


def registerStudent():
    print("-----Registration Form-----")
    # Taking input for student details
    firstName = input("First Name: ").strip()
    lastName = input("Last Name: ").strip()

    # Ensuring valid gender input
    gender = input("Gender (M/F): ").strip().upper()
    if gender not in ["M", "F"]:
        print("Invalid choice, please try again.")
        return

    # Ensuring valid year level input
    yearLevel = int(input("Year Level (1-4): ").strip())
    if yearLevel < 1 or yearLevel > 4:
        print("Invalid choice, please try again.")
        return

    # Assigning a unique student ID
    studentsTotal = len(studentManager.studentsList)
    id = 1 if studentsTotal == 0 else studentManager.studentsList[studentsTotal - 1].id + 1

    # Creating and registering a new student
    newStudent = models.Student(id, firstName, lastName, gender, yearLevel)
    studentManager.registerStudent(newStudent)


def displayAllStudents():
    # Displaying all registered students
    studentManager.displayAllStudents()


# Mapping update options to corresponding functions
updateOptions = {
    1: studentManager.updateStudentFirstName,
    2: studentManager.updateStudentLastName,
    3: studentManager.updateStudentGender,
    4: studentManager.updateStudentYearLevel,
    5: studentManager.updateStudentGrade,
}


def updateStudent():
    # Displaying update options to the user
    displayUpdateOptions()
    messagePrompt = f"Enter your choice 1-{len(updateOptions)}: "
    choice = int(input(messagePrompt))
    
    # Executing the chosen update action
    action = updateOptions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice, please try again.")


def displayOneStudent():
    # Displaying a specific student by ID
    id = int(input("Enter student ID: ").strip())
    studentManager.displayStudentById(id)


def deleteStudent():
    # Deleting a student by ID
    id = int(input("Enter student ID: ").strip())
    studentManager.deleteStudentById(id)


def exitProgram():
    # Exiting the program
    print("Exiting the program. Goodbye!")
    exit()
