# Problem 1 — List manipulation

# scores = [72, 45, 88, 92, 55, 38, 76, 91, 63, 48]

# passed = [n for n in scores if n >= 50]
# failed = [n for n in scores if n < 50]


# highest = max(passed)
# lowest = min(passed)
# avg = sum(passed)/len(passed);

# details = {"Highest":highest, "Lowest":lowest, "Average":avg}

# sort = sorted(scores, reverse=True);

# print(f"Passed : {passed}")
# print(f"Failed: {failed}")


# print(f"Top 3 scorers:")
# for i, value in enumerate(sort,start=1):
#     if i >3:
#         break
#     print(f"{i}. {value}")

# for key, value in details.items():
#     print(f"{key} : {value}")



# Problem 2 — Tuple + set challenge
# day1 = ("Ravi", "Priya", "Arjun", "Sneha", "Kiran")
# day2 = ("Priya", "Kiran", "Meera", "Arjun", "Rohan")

# set1 = set(day1)
# set2 = set(day2)

# attend_both = set1 &set2
# attend_day1 = set1 - set2
# attend_day2 = set2 - set1
# attend_as_one = set1 | set2

# print(f"Attend both days :{attend_both}")
# print(f"Only day 1  :{attend_day1}")
# print(f"Only day 2  :{attend_day2}")
# print(f"At least one day :{attend_as_one}")
# print(f"Total unique students :{len(attend_as_one)}")

# Problem 3 — Dictionary deep dive
students = {
    "Ravi"  : {"age": 22, "scores": [85, 90, 78]},
    "Priya" : {"age": 21, "scores": [92, 88, 95]},
    "Arjun" : {"age": 23, "scores": [70, 65, 80]},
    "Sneha" : {"age": 22, "scores": [45, 55, 60]},
    "Kiran" : {"age": 24, "scores": [88, 91, 85]},
}

new_dictonary = {}
for names, info in students.items():
    avg = (sum(info['scores'])/len(info['scores']))
    if avg > 85:
        grade = "A"
    elif 75 <= avg < 85:
        grade = "B"
    elif 60 <= avg <= 74:
        grade = "C"
    else:
        grade = "F"

    new_dictonary.update({"Name": {names}, "Avg": {avg}, "grade": {grade},})
    
    print(f"{names} {avg} {grade}")


