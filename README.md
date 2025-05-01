# EduTrack: A Simple Student Record Manager

## About the Project

### Project Title

EduTrack: A Simple Student Record Manager

### Project Description

EduTrack allows users to add, update, delete, and search student records. It provides functionalities to store student names, IDs, and grades, ensuring easy retrieval and management of academic records.

### Core Problem

The core problem EduTrack addresses is the manual and disorganized handling of student records in small educational settings. Many classrooms or small institutions still rely on paper-based systems or scattered files, which can lead to lost information, difficulty in finding records, and errors in managing student details. Without a simple digital tool, tasks like updating grades or finding a specific student’s record can be time-consuming and prone to mistakes. EduTrack solves this by offering a basic, easy-to-use digital system where users can efficiently add, view, update, and manage student records—all through a console interface. It helps reduce paperwork and makes record management more consistent and accessible.

## Pseudo Code

<pre>
START PROGRAM

IMPORT necessary components (models, manager, menu)

INITIALIZE StudentManager
DEFINE menuActions:
    1 -> registerStudent
    2 -> displayAllStudents
    3 -> updateStudent
    4 -> displayOneStudent
    5 -> deleteStudent
    6 -> exitProgram

DISPLAY "Welcome to EduTrack"

REPEAT FOREVER:
    DISPLAY main menu options
    PROMPT user to enter choice (1-6)
    
    IF input is not an integer:
        DISPLAY error message
        CONTINUE loop

    RETRIEVE corresponding function from menuActions using choice

    IF function exists:
        CALL function
    ELSE:
        DISPLAY "Invalid choice"

--- FUNCTION: registerStudent ---
DISPLAY "Registration Form"
PROMPT for first name, last name
PROMPT for gender (must be 'M' or 'F')
IF gender is invalid:
    DISPLAY error
    RETURN
PROMPT for year level (1–4)
IF year level is invalid:
    DISPLAY error
    RETURN
GENERATE student ID based on list length
CREATE new Student object
REGISTER student using StudentManager

--- FUNCTION: displayAllStudents ---
IF no students in list:
    DISPLAY "Student list is empty"
ELSE:
    FOR each student in list:
        DISPLAY student information

--- FUNCTION: updateStudent ---
DISPLAY update options menu (e.g., First Name, Last Name, etc.)
PROMPT user to choose update option
RETRIEVE corresponding update function
IF function exists:
    CALL function
ELSE:
    DISPLAY "Invalid choice"

--- FUNCTION: displayOneStudent ---
PROMPT user for student ID
RETRIEVE student using StudentManager
IF student exists:
    DISPLAY student information
ELSE:
    DISPLAY "Student not found"

--- FUNCTION: deleteStudent ---
PROMPT user for student ID
FIND and DELETE student from list
IF deletion successful:
    DISPLAY confirmation
ELSE:
    DISPLAY "Student not found"

--- FUNCTION: exitProgram ---
DISPLAY exit message
TERMINATE program

END PROGRAM
</pre>

### Group information
1. Altiz, Khaim Michael C.
2. Alcaraz, Rica May G.
3. Apritado, Allyssa Grace A.