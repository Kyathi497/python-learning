# read a file use "r" method for reading file
# with open("data.txt", "r") as f:
#     content = f.read()
# print(content)

#use the "w" method for creating a file or overwrites existing
# with open("notes.txt", "w") as f:
#     f.write("Hello thi python\n")
#     f.write("This is line 2.\n")

#use this "a" method for appending into existing file
# with open("notes.txt", "a") as f:
#     f.write("This line is appended.\n")

#write multiple lines at once
# lines = ["Ravi\n", "Vijay\n", "Arjun\n"]
# with open("notes.txt", "w") as f:
#     f.writelines(lines)

#Read entire file as one string
# with open("notes.txt", "r") as f:
#     content = f.read()
#     print(content)

#Read one line at a time 
# with open("notes.txt", "r") as f:
#     line = f.readline()
#     print(line)

#Read all lines into a list
# with open("notes.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

#Loop line by line - most memory efficient for large files
# with open("notes.txt", "r") as f:
#     for line in f:
#         print(line.strip())

#Trying error handling
# try:
#     with open("notes.txt", "r") as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError:
#     print("File not Found!")
# except PermissionError:
#     print("You dont have permission to read this file")
from pathlib import Path

#current directory we are in
# current = Path(".")
# print(current.resolve())

#build paths safely
# data_file = Path("data") / "students.txt"

#check if file exists before opening
# if data_file.exists():
#     with open(data_file, "r") as f:
#         print(f.read())
# else:
#     print("File doesnt exist")

#Creates directories
# Path("output").mkdir(exist_ok=True)

#List all .txt files in a folder
# for file in Path(".").glob("*.txt"):
#     print(file.name)

# import csv

# students = [
#     ["Name",  "Age", "Score"],
#     ["Ravi",   22,    85],
#     ["Priya",  21,    92],
#     ["Arjun",  23,    78],
# ]

# with open("students.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(students)    # write all rows at once


import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)         # skip the header row
    print(f"Columns: {header}")

    for row in reader:
        print(f"{row[0]} scored {row[2]}")