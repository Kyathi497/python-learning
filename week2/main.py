# Problem 1:- Pattern Printing

value = 5

# for i in range(1, value+1):
#     for j in range(1,i+1):
#         print(f"{j} ",end="")
#     print()

# Problem 2 — while loop + input validation

while True:
    value = int(input("enter value in between 1 to 10: "))
    if 1<value<10:
        print(f"Great choice: [{value}]")
        break
    else:
        print("Invalid! Try again.")
# Problem 3 — enumerate() challenge

# students = ["Ravi", "Priya", "Arjun", "Sneha", "Kiran"]
# scores =   [45, 82, 91, 60, 78]


# for i, (student, score) in enumerate(zip(students,scores), start=1):
#     is_pass = "✅ Pass" if score >= 50 else "❌ Fail"
#     print(f"{i}. {student} - {score} {is_pass}")


# Problem 4 — break & continue

# for i in range(1,51):
    
#         if(i%3 == 0):
#             continue
#         if(i%7 == 0):
#             break
#         print(i)