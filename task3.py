#!/usr/bin/env python3

import random
import sys
from re import sub
import os

if __name__ == '__main__':

    ucas_numbers = []
    emails = []
    initials = []

# if students.txt doesn't exist, exit the command line

    if not os.path.exists("students.txt"):
        print("Error: file cannot be located.")
        sys.exit(2)

    # allow students.txt to be read
    # allow emails.txt to be written

    student_file = open("students.txt", 'r')

    email_file = open("emails.txt", 'w')

    # for each student in student_file, append onto ucas_numbers the first 8 characters
    # of eact iteration of student in the for loop.

    for student in student_file:
        ucas_numbers.append(student[:8])
        full_name = student.split(", ")
        first_name = full_name[1]
        second_name = full_name[0]
        initials.append(first_name[0])

        

        #email_file.write(everything you want it to show)

        
        
        --------------------------
        
        
        
        #!/usr/bin/env python3

import random
import sys
import re
import os

if __name__ == '__main__':

    student_file = open("students.txt", 'r')
    email_file = open("emails.txt", 'w')

    if not os.path.exists("students.txt"):
        print("Error: file cannot be located.")
        sys.exit(2)


    # for each student in student_file, append onto ucas_numbers the first 8 characters
    # of each iteration of student in the for loop.
    try:
        for student in student_file:
            ucas_numbers = student[:8])
            student_names = student[9:].split(", ")

        for name in student_names:
            first_name = student_names[1]
            second_name = student_names[0]
            #second_name = re.sub(r"[^a-zA-Z]", "", student_names[0])
            #initials.append(first_name[0])
            random_num = random.randint(1000, 9999)

            initials = ".".join(chars for chars in first_name if chars.isupper())

            #initials = for chars in first_name:
                #if chars.isupper():
                    #joined_chars = ".".join(chars)

            emails = f"{initials}.{second_name}{random_num}@poppleton.ac.uk"

        email_file.write(ucas_numbers + emails.lower() + "\n")

    #emails = (joined_chars, ".", second_name, random_num, "@poppleton.ac.uk")


        student_file.close()
        email_file.close()

    except FileNotFoundError:
        print("Error. File cannot be located")

    sys.exit(1)
