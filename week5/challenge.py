# Problem 1 — Text file basics

# multipleLines = [
#     "Python is awesome\n",
# "File handling is useful\n",
# "I am learning Week 5\n",
# "Data persists beyond the program\n",
# "Hyderabad is my city\n"
# ]
# with open("challenge.txt", "w" ) as f:
#     f.writelines(multipleLines)


# with open("challenge.txt", 'r') as f:
#     content = f.readlines()
#     for line in content:
#         print(line)
    
# print("After appending:\n")


# with open("challenge.txt", "a") as f:
#     appended_content = f.write("keep going, don't stop!")


# with open("challenge.txt", 'r') as f:
#     content = f.readlines()
#     for line in content:
#         print(line)

# Problem 2 — CSV read and write

import csv

students = [
    {"name": "Ravi",  "math": 85, "science": 90, "english": 78},
    {"name": "Priya", "math": 92, "science": 88, "english": 95},
    {"name": "Arjun", "math": 70, "science": 65, "english": 80},
    {"name": "Sneha", "math": 45, "science": 55, "english": 60},
    {"name": "Kiran", "math": 88, "science": 91, "english": 85},
]

with open("challenge2.txt", "w", newline="") as f:
    fieldnames = ["name", "math", "science", "english"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

with open("challenge2.txt", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row["name"],row["ag"])