first_name = input("Enter your first name: ").capitalize()
last_name = input("Enter your last name: ").capitalize()
length_fname = len(first_name)
length_lname = len(last_name)
print(f"Your first name is   ", first_name) 
print(f"Your last name is   ", last_name) 
print(f"Your full name is  {first_name} {last_name}")
print(f"Your full name can also be  {last_name} {first_name}")
print(f"Your  first name {first_name} has {length_fname} characters")
print(f"Your  last name {last_name} has {length_lname} characters")


