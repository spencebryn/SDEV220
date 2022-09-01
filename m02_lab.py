# Spencer Strange
# SDEV 220 
# m02_lab.py
# Purpose of program:
#   Accept input of student's name and GPA and determine if they have earned academic honors.
# Variables:
#   lastName: str; student last name
#   firstName: str; student first name
#   gpa: float; student gpa

lastName = str(input("Please provide student's last name: "))
while lastName.upper() != "ZZZ":
    firstName = str(input("Please provide student's first name: "))
    gpa = float(input("Please provide student's GPA: "))
    if gpa >= 3.5:
        print(firstName + "", lastName +" has made the Dean's List.")
    elif 3.5 > gpa >= 3.25:
        print(firstName + "", lastName + " has made the Honor Roll.")
    else:
        print(firstName + "", lastName + " has not achieved academic honors at this time.")
    lastName = str(input("Please provide another student's last name (or enter ZZZ to quit): "))


