def calculate_price(price, discount=10):
    discount_amount = price * discount / 100
    final_price = price - discount_amount
    return final_price
print(calculate_price(1000, 20))
print(calculate_price(1000))

def employee_details(name, age, department):
    print(f"Name: {name}")
    print(f"age: {age}")
    print(f"department: {department}")
employee_details(
    department="GenAI",
    name="Rakshith",
    age=28
)


def create_user(name, role="User", active=True):
    return name, role, active
user1 = create_user("Rakshith")
user2 = create_user(
    "Arun", 
    role="Admin"
)
user3 = create_user(
    name="Priya", 
    role="Developer", 
    active=False
)
print(user1)
print(user2)
print(user3)