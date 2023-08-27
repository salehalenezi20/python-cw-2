my_name= input("whats your name:")
my_age=input("enter your age:")
print(f"My name is {my_name} and I am {my_age} years old")


first_number=int(input("number one:"))
seconde_number=int(input("number two:"))
operation=input("enter an operation:")

if operation == "+":
    print(first_number+seconde_number)

elif operation == "-":
    print(first_number-seconde_number)
    
elif operation =="*":
    print(first_number*seconde_number)
elif operation=="/":
    print(first_number/seconde_number)

bus_capacity=19
people_inbus=int(input("how many people in the bus?:"))
poeple_how_wants_to_get_in=int(input("how many people wants to get in the bus"))
empty_seats = (poeple_how_wants_to_get_in - people_inbus)
if empty_seats >= people_inbus:
    print("there are empty seats")


elif empty_seats <= poeple_how_wants_to_get_in:
    print("no seats on the bus are full")
    