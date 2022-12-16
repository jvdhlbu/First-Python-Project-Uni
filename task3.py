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

