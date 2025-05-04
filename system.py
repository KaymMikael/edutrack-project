import models
import manager
from menu import *

studentManager = manager.StudentManager()


def registerStudent():
    print("-----Registration Form-----")
    firstName = input("First Name: ").strip()
    lastName = input("Last Name: ").strip()

    gender = input("Gender (M/F): ").strip().upper()
    if gender not in ["M", "F"]:
        print("Invalid choice, please try again.")
        return

    yearLevel = int(input("Year Level (1-4): ").strip())
    if yearLevel < 1 or yearLevel > 4:
        print("Invalid choice, please try again.")
        return

    studentsTotal = len(studentManager.studentsList)
    id = 1 if studentsTotal == 0 else studentManager.studentsList[studentsTotal - 1].id + 1
    newStudent = models.Student(id, firstName, lastName, gender, yearLevel)
    studentManager.registerStudent(newStudent)


def displayAllStudents():
    studentManager.displayAllStudents()


updateOptions = {
    1: studentManager.updateStudentFirstName,
    2: studentManager.updateStudentLastName,
    3: studentManager.updateStudentGender,
    4: studentManager.updateStudentYearLevel,
    5: studentManager.updateStudentGrade,
}


def updateStudent():
    displayUpdateOptions()
    messagePrompt = f"Enter your choice 1-{len(updateOptions)}: "
    choice = int(input(messagePrompt))
    action = updateOptions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice, please try again.")


def displayOneStudent():
    id = int(input("Enter student ID: ").strip())
    studentManager.displayStudentById(id)


def deleteStudent():
    id = int(input("Enter student ID: ").strip())
    studentManager.deleteStudentById(id)


def exitProgram():
    print("Exiting the program. Goodbye!")
    exit()
