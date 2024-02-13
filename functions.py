# Inbuilt function
number = max(60, 45, 53, 95, 742)
print(number)

y = min(45, 86, 63, 541)
print(y)

z = pow(2, 3)
print(z)


# User-defined function
def name():
    print("Ruthqie")


name()  # calling a funcction


def details():
    name = " mumbe"
    age = 19
    course = "MIT"
    print(name, age, course)


details()


# Parameters/ variables and arguments/values
def patient(name, gender, age, tell_number):
    print(name, gender, age, tell_number)


patient("heezy", "male", 15, 759496596)
patient("james", "male", 16, 5769874)
patient("ndanu", "female", 18, 5769874)
patient("kyalo", "male", 19, 5769874)
patient("musyoka", "male", 19, 5769874)
patient("mbiti", "male", 14, 5769874)
patient("ndunge", "female", 18, 5769874)


def multiply(x, y):
    print(x * y)


multiply(2, 9)
multiply(2, 9)
multiply(5, 9)
multiply(6, 9)


# Create a user-defined function


def employee(full_name, age, position, salary):
    print(full_name, age, position, salary)

employee("Ruth_Mumbe",18,"CEO","$100")
employee("Agnes muia",18,"CEO","$100")
employee("Mary Kanyiva",18,"CEO","$100")
employee("Esther Mueni",18,"CEO","$100")
employee("Mercy Muthoki",18,"","$100")
employee("Mutu mutu",18,"manager","$100")
