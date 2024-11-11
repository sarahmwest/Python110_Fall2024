# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, json files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Sarah West/11/09/2024, Finished Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
# Deleted the csv_data variable - didn't need this extra variable since we are using json files.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

import json  # imports json module

# When the program starts, read the file data into a list of dictionaries (table):
# Included try/except blocks to handle basic errors.
try:
    file = open(FILE_NAME, "r")  # opens the json file.
    students = json.load(file)  # json.load() function parses the data into a python list of
    # dictionaries and "dumps" it into the 'students' variable.
    file.close()  # closes the file.
except FileNotFoundError as e:  # if the file doesn't exist, this block will execute; error stored in "e".
    print("JSON file not found!")  # prints custom error message.
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')  # prints technical error message with error class.
except Exception as e:  # if any other exception is raised, this block will execute.
    print("There was a non-specific error associated with opening the file!")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
finally:  # this block will execute regardless if exceptions are executed.
    if file.close == False:
        file.close()  # this will close the file if the "try" block encounters an exception.

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:  # the try block will execute first
            student_first_name = input("Enter the student's first name: ")
            # Exception handling
            if not student_first_name.isalpha():
                raise ValueError("The first name shouldn't contain numbers.")  # Error raised if name has numbers.
            student_last_name = input("Enter the student's last name: ")
            # Exception handling
            if not student_last_name.isalpha():
                raise ValueError("The last name shouldn't contain numbers")  # Error raised if name has numbers
            course_name = input("Please enter the name of the course: ")
            if not course_name.isalnum():
                raise ValueError("Course name must be alphanumeric!")
        except ValueError as e:
            print(e)  # prints the custom message
            print("--Technical Error Message--")
            print(e.__doc__, type(e), sep='\n')  # prints the technical message
        except Exception as e:  # the catch-all error message in case not ValueError.
            print("There as a non-specific error regarding student registration !")
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')  # prints the technical message
            # Add entered data to the students variable and tell the user they successfully entered the info.
        else:  # This block will execute if no error found.
            student_data = {"FirstName": student_first_name, "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(
                student_data)  # adds the inputed student data to the list of dictionaries stored in students.
            print(f'You have registered {student_first_name} {student_last_name} for {course_name}.')
        continue

    # Present the current data as a string.
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            message = (f'{student["FirstName"]} {student["LastName"]} is enrolled in '
                       f'{student["CourseName"]}')
            print(message)  # prints the message for each student in the list students.
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")  # opens the file.
            json.dump(students, file)  # writes the table list (i.e., dictionaries) to file in json format.
            file.close()  # save the file
            print("The following data was saved to file:")
            for student in students:
                print(f'Student {student["FirstName"]} {student["LastName"]} '
                      f'is enrolled in {student["CourseName"]}')  # prints the student info for each registered student
        except IOError as e:  # an exception to handle input/output errors when writing data.
            print("There is an error with the file name or location!")
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:  # the catch-all error message.
            print("There as a non-specific error regarding saving data to the file!")
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')  # prints the technical message
        finally:  # this block will execute regardless if exceptions are executed.
            if file.close == False:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
