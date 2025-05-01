from models import *


class StudentManager:
    # Constructor to initialize the student manager
    def __init__(self):
        self.studentsList: list[Student] = []  # List to store all registered students

    # Method to register a new student
    def registerStudent(self, student: Student):
        self.studentsList.append(student)  # Add the student to the students list
        print("Registered Successfully")  # Confirm successful registration

    # Method to display all registered students
    def displayAllStudents(self):
        if not self.studentsList:  # Check if the list is empty
            print(
                "Student list is empty"
            )  # Display message if no students are registered
        else:
            print("All of your students:")  # Display header
            for (
                student
            ) in self.studentsList:  # Iterate through and display each student
                student.displayInfo()  # Call the student’s displayInfo method to show details

    # A method for displaying 1 student
    def displayStudentById(self, id: int):
        student = self.getStudentById(id)

        # check if student exists
        if not student:
            # print not found if student does not exists in list
            print(f"Student with id of {id} is not found")
            return

        # display existing student info
        student.displayInfo()

    # Method to delete a student by their ID
    def deleteStudentById(self, id: int):
        for student in self.studentsList:  # Iterate through the list of students
            if student.id == id:  # Check if the ID matches
                self.studentsList.remove(student)  # Remove the student from the list
                print(f"Student with ID {id} has been deleted.")  # Confirm deletion
                return  # Exit the method after deletion

        # If no student with the given ID is found
        print(f"Student with ID {id} does not exist.")  # Display error message

    # Method to get student by id
    def getStudentById(self, id: int) -> Student:
        for student in self.studentsList:
            if student.id == id:
                return student

    # Method for updating student grade by id
    def updateStudentGrade(self):
        id = int(input("Enter ID: "))
        student = self.getStudentById(id)
        if not student:
            print(f"Student with ID {id} does not exist.")  # Display error message
            return

        subject = input("Enter subject: ").strip()
        grade = float(input("Enter grade: "))
        student.addGrade(subject, grade)

    def updateStudentFirstName(self):
        id = int(input("Enter ID: "))
        student = self.getStudentById(id)
        if not student:
            print(
                f"Student with ID {id} does not exist."
            )  # Check if the student exists
            return
        newFirstName = input("Enter new first name: ")  # Prompt for new first name
        student.setNewFirstName(newFirstName)  # Update the student's first name
        print("Updated successfully")  # Confirmation message

    def updateStudentLastName(self):
        id = int(input("Enter ID: "))
        student = self.getStudentById(id)
        if not student:
            print(
                f"Student with ID {id} does not exist."
            )  # Check if the student exists
            return
        newLastName = input("Enter new last name: ")  # Prompt for new last name
        student.setNewLastName(newLastName)  # Update the student's last name
        print("Updated successfully")  # Confirmation message

    def updateStudentGender(self):
        id = int(input("Enter ID: "))
        student = self.getStudentById(id)
        if not student:
            print(
                f"Student with ID {id} does not exist."
            )  # Check if the student exists
            return
        newGender = input(
            "Enter new gender (M/F): "
        ).upper()  # Prompt for new gender input
        if newGender not in ["M", "F"]:
            print("Invalid choice, please try again.")  # Validate input for gender
            return
        student.setNewGender(newGender)  # Update the student's gender
        print("Updated successfully")  # Confirmation message

    def updateStudentYearLevel(self):
        id = int(input("Enter ID: "))
        student = self.getStudentById(id)
        if not student:
            print(f"Student with ID {id} does not exist.")
            return
        newYearLevel = int(input("Enter new year level (1-4): "))
        if newYearLevel < 1 or newYearLevel > 4:
            print("Invalid choice, please try again.")
            return

        student.setNewYearLevel(newYearLevel)
        print("Updated successfully")
