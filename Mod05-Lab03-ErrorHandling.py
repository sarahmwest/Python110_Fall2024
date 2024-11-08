# ------------------------------------------------------------------------------------------ #
# Title: Mod05-Lab01- Working with dictionaries and files using error handling
# Desc: shows how to work with dictionaries and use error handling
# Change Log: (Who, When, What)
#   Sarah West, 11/08/24,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Student's GAP ---------------------
  Select from the following menu:  
    1. Show Current Student Data.
    2. Enter New Student Data
    3. Save Data to a File.
    4. Exit the Program.
----------------------------------------- 
'''
FILE_NAME: str = "MyLabData.json"

# Define the Programs Data
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the name of a course entered by the user.
message: str = ''  # Holds a custom message.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # One row of student data as a dictionary.
students: list = []  # All the student data in a table.
file_data: str = ''  # Holds combined string data seperated by commas.

# When the program starts, open the json file, dumps the data into the students variable, and closes the file
# Add a try block for error handling:
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running the script!")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!")
    print("--Technical Error Message--")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.close == False:
        file.close()

# Repeat the following tasks:
while True:
    print(MENU)
    menu_choice = input("Enter your menu choice: ")
    print()

    # display the table's current data
    if menu_choice == "1":
        print("-" * 50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = (f'{student["FirstName"]} {student["LastName"]} earned an A with a '
                           f'{student["GPA"]}')
            elif student["GPA"] >= 3.0:
                message = (f'{student["FirstName"]} {student["LastName"]} earned a B with a '
                           f'{student["GPA"]}')
            elif student["GPA"] >= 2.0:
                message = (f'{student["FirstName"]} {student["LastName"]} earned a C with a '
                           f'{student["GPA"]}')
            elif student["GPA"] >= 1.0:
                message = (f'{student["FirstName"]} {student["LastName"]} earned a D with a '
                           f'{student["GPA"]}')
            else:
                message = (f'{student["FirstName"]} {student["LastName"]} failed with a '
                           f' {student["GPA"]}')
            print(message)
        print("-" * 50)
        continue

    # Add data to the table
    elif menu_choice == "2":
        try:
            student_first_name = input("What is the student's first name? ")
            # Exception handling
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            try:  # using a nested try block to capture when an input cannot be changed to a float
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            student_data = {"FirstName": student_first_name, "LastName": student_last_name,
                            "GPA": student_gpa}
            students.append(student_data)
        except ValueError as e:
            print(e)  # prints the custom message
            print("--Technical Error Message--")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There as a non-specific error!")
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')
        print(f"{student_first_name} {student_last_name}'s GPA is entered!")
        continue

    # Save the data to the json file
    elif menu_choice == "3":
        # Error handling
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            continue
        except TypeError as e:
            print("Please check the data is in the JSON format\n")
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("--Technical Error Message--")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
    elif menu_choice == "4":
        break
    else:
        print("You did not enter a valid option.")
