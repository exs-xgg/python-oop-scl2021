from student import Student
from teacher import Teacher
import pickle

def start():
    print("Welcome to the school database editor")

def promptForInput(message):
    selection = ""
    while not (selection == "S" or selection == "T"):
        selection  = input(message).upper()
    return selection


def addNewStudent(listToAdd):
    newFirstName = input("Student's First Name: ")
    newLastName = input("Student's Last Name: ")
    newIdNum = input("Student's ID Number: ")
    newStudentId = input("Student's School ID: ")
    newFormClass = input("Student's Form Class: ")
    
    newStudent = Student(newFirstName,newLastName,newIdNum,newStudentId,newFormClass)
    listToAdd.append(newStudent)

def addNewTeacher(listToAdd):
    newFirstName = input("Teacher's First Name: ")
    newLastName = input("Teacher's Last Name: ")
    newIdNum = input("Teacher's ID Number: ")
    newStaffId = input("Teacher's Staff ID: ")
    newDept = input("Student's Department: ")
    
    newTeacher = Student(newFirstName,newLastName,newIdNum,newStaffId,newDept)
    listToAdd.append(newTeacher)

def showList(listToShow):
    if bool(listToShow):
        for i in range(len(listToShow)):
            print(str(i + 1) + " | " + listToShow[i].getFullInfo())
    else:
        print("Error: There is nobody on ths list!")

        
def deleteEntry(listToDelete):
    try:
        entryToDelete = int(input("Which entry do you want to delete? (0 to cancel)"))
        if 0 < entryToDelete < len(listToDelete) :
            temp = listToDelete[entryToDelete - 1].getFullInfo()
            print("Deleting: " + temp)
            del listToDelete[entryToDelete - 1]
        elif entryToDelete == 0:
            print("Cancelled. Nothing will get deleted.")
        else:
            print("Invalid entry")
    except :
        print("Please enter a valid number.")

def updateEntry(listToUpdate, selection):
    try:
        entryToUpdate = int(input("Which entry do you want to update? (0 to cancel)"))
        if 0 < entryToUpdate < len(listToUpdate) :
            temp = listToUpdate[entryToUpdate - 1].listToUpdate()
            print("Update: " + temp)
            
            if selection == "S":
                fieldToUpdate = int(input("""Which field do you want to update?
                1 | First Name
                2 | Last Name
                3 | ID Number
                4 | School ID
                5 | Form Class
                0 | Cancel
                                          """))
                if fieldToUpdate == 5:
                    print("Cancelled. Nothing will get Updated.")
                elif 0 < fieldToUpdate <= 5:
                    newValue = input("What is the new value? ")
                    listToUpdate[entryToUpdate - 1].update(fieldToUpdate, newValue)
                else:
                    print("Invalid Selection")
                    
                    
                    
            elif selection == "T":
                fieldToUpdate = int(input("""Which field do you want to update?
                1 | First Name
                2 | Last Name
                3 | ID Number
                4 | Staff ID
                5 | Department
                0 | Cancel
                                          """))
                if fieldToUpdate == 5:
                    print("Cancelled. Nothing will get Updated.")
                elif 0 < fieldToUpdate <= 5:
                    newValue = input("What is the new value? ")
                    listToUpdate[entryToUpdate - 1].update(fieldToUpdate, newValue)
                else:
                    print("Invalid Selection")
                  
        elif 0 < entryToUpdate <= 5:
            print("Cancelled. Nothing will get Updated.")
        else:
            print("Invalid entry")
    except:
        print('Error, invalid selection')

# START MAIN =======
databaseFileName = "schoolDB.pickle"
# load data from pickle db
start()
try:
    file = open(databaseFileName, "rb")
    teachersList = pickle.load(file)
    studentsList = pickle.load(file)
    file.close()
except:
    print("Creating new file...")
    teachersList = []
    studentsList = []
    
runProg = True
while runProg:
    user = input("""What do you want to do?
A: Add new entry
S: Show & list database
U: Update an entry
D: Delete an entry
E: Exit the program
                 """).upper()
                 
    if user == "E":
        print("Saving data to file .. Please wait..")
        file = open(databaseFileName,"wb")
        pickle.dump(teachersList, file)
        pickle.dump(studentsList, file)
    elif user == "A":
        selection = promptForInput("""Which Entry do you with to add?
S - Students
T - Teachers
""").upper()
        if selection == 'S':
            addNewStudent(studentsList)
        elif selection == 'T':
            addNewTeacher(teachersList)
            
            
    elif user == 'S':
        selection = promptForInput("""Which List do you with to show?
S - Students
T - Teachers
""").upper()
        if selection == 'S':
            showList(studentsList)
        elif selection == 'T':
            showList(teachersList)
    
    elif user == 'D':
        selection = promptForInput("""Which entry do you with to delete?
S - Students
T - Teachers
""").upper()
        if selection == 'S':
            showList(studentsList)
            deleteEntry(studentsList)
            
        elif selection == 'T':
            showList(teachersList)
            deleteEntry(teachersList)
    
    elif user == 'U':
        selection = promptForInput("""Which entry do you with to Update?
S - Students
T - Teachers
""").upper()
        if selection == 'S':
            showList(studentsList)
            updateEntry(studentsList,selection)
            
        elif selection == 'T':
            showList(teachersList)
            deleteEntry(teachersList,selection)
    else:
        print("Invalid selection, please try again.")
            
        