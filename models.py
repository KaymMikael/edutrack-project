class Student:
    # Constructor to initialize a Student object with specific attributes
    def __init__(
        self,
        id: int,  # Unique identifier for the student
        firstName: str,  # First name of the student
        lastName: str,  # Last name of the student
        gender: str,  # Gender of the student
        yearLevel: int,  # Academic year level (e.g., 1 for freshmen, 2 for sophomores, etc.)
    ):
        self.id = id  # Initialize student ID
        self.firstName = firstName  # Initialize first name
        self.lastName = lastName  # Initialize last name
        self.gender = gender
        self.yearLevel = yearLevel
        self.grades = {}

    # Method to display student's information
    def displayInfo(self):
        print("------------------------------")
        print(f"Student Id: {self.id}")  # Display student ID
        print(f"Name: {self.firstName} {self.lastName}")  # Display student's full name
        print(f"Year Level: {self.yearLevel}")  # Display year level
        print(f"Gender: {self.gender}")  # Display year level
        if not self.grades:
            print("No grades available")
        else:
            print("Grades:")  # Display grades in the following format:
            for subject, grade in self.grades.items():
                print(
                    f"  {subject}: {grade:.2f}"
                )  # Show each subject with its grade (rounded to 2 decimal places)

            # Calculate and display the average grade
            self.displayAverage()

    # Method to calculate the average of all grades
    def calculateAverage(self):
        return sum(self.grades.values()) / len(
            self.grades
        )  # Compute and return average grade

    # Method to display the average grade
    def displayAverage(self):
        average = (
            self.calculateAverage()
        )  # Calculate the average using the method above
        print(
            f"Average Grade: {average:.2f}"
        )  # Display the average grade rounded to 2 decimal places

    def setNewFirstName(self, newFirstName: str):
        self.firstName = newFirstName

    def setNewLastName(self, newLastName: str):
        self.lastName = newLastName

    def setNewGender(self, newGender: str):
        self.gender = newGender

    def setNewYearLevel(self, newYearLevel: int):
        self.yearLevel = newYearLevel

    def addGrade(self, subject: str, grade: float):
        self.grades[subject] = grade
