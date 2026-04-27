# Problem 1 — Basic functions & return values

# def calculate_bmi(weight, height):
#     bmi = weight /(height**2)
#     if bmi < 18.5:
#         return bmi, "Underweight"
#     elif 18.5 < bmi <24.9:
#         return bmi, "Normal"
#     elif 25 < bmi <29.9:
#         return bmi, "Overweight"
#     else:
#         return bmi, "Obese"

# result = tuple(calculate_bmi(70,170));
# print(f"BMI: {result[0]}");
# print(f"Category: {result[1]}");

# Problem 2 — Default arguments & keyword arguments

# def create_profile(name, age, city="Hyderabad", role="Student"):
#     print("============")
#     print(f"Name : {name}")
#     print(f"Age : {age}")
#     print(f"City : {city}")
#     print(f"Role : {role}")
#     print("============")


# create_profile("Ravi", 22)
# create_profile("Rohith", 38, city="vizag", role="Cricketer")
# create_profile("Rohith", 38, role="Cricketer", city="vizag")

# Problem 3 — *args and **kwargs

# def generate_invoice(customer, *items, **details):
#     items_total = sum(items)
    
#     discount = details.get('discount', 0)
#     tax = details.get('tax', 0)
    
#     # Apply discount first
#     discounted_price = items_total - (discount / 100) * items_total
    
#     # Apply tax on discounted price
#     final_total = discounted_price + (tax / 100) * discounted_price
    
#     print(f"Invoice for: {customer}")
#     print(f"Items total: ₹{items_total}")
#     print(f"Discount   : {discount}%")
#     print(f"Tax        : {tax}%")
#     print(f"Final total: ₹{final_total}")


# # Example call
# generate_invoice("Ravi", 20, 30, 40, 50, discount=10, tax=5)

# Problem 4 — Scope challenge

x = 10

def outer():
    x = 20
    def inner():
        global x
        x=99
        print(f"inner: {x}")
    inner()
    print(f"outer: {x}")

outer()
print(f"global: {x}")