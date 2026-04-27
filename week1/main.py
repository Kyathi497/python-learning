# Problem 1:-printing using f-string

# name = "Kyathi Vardhan"
# age = 23
# city = "Vijayawada"

# print(f"Hi! I'm {name}, {age} years old and I live in {city}. \nIn 5 years, I'll be {age+5}")

# Problem 2:-Operator Challenge

# product = "Headphones"
# original_price = 2000
# discount = 15
# saved = int(discount/100*original_price);
# final_price = original_price-saved

# print(f"Product: {product}\nOrginal price: ${original_price}\nDiscount: {discount}%\nYou save: ${saved}\nFinal price: ${final_price}")

# Problem 3:-Think it through

no_of_Tickets = int(input("Enter number of tickets: "))
day = str(input("Enter which day is it eighter Weekday or Weekend: "))

ticket_cost_weekdays = 250
ticket_cost_weekends = 350

if day == "Weekday":
    total_cost = ticket_cost_weekdays*no_of_Tickets
    print(f"Total Cost: ${total_cost}")
elif day == "Weekend":
    total_cost = ticket_cost_weekends*no_of_Tickets
    print(f"Total Cost: ${total_cost}")
else:
    print("Enter correct day either Weekday or Weekend")