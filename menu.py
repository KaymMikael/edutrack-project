menuList = [
    "Register",
    "Display All Student",
    "Update Student",
    "Display One Student",
    "Delete Student",
    "Exit",
]

updateOptions = [
    "Update First Name",
    "Update Last Name",
    "Update Gender",
    "Update Year Level",
    "Add Grade",
]

def displayMenu():
    print("-----Menu-----")
    for i in range(len(menuList)):
        print(f"{i + 1}. {menuList[i]}")


def displayUpdateOptions():
    print("-----Update Options-----")
    for i in range(len(updateOptions)):
        print(f"{i + 1}. {updateOptions[i]}")