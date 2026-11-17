# Version 2
#Inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")
favorite_subject = input("Enter your favorite subject: ")

# Processing & Formatting
full_name = f"{first_name} {last_name}"
proper_full_name = full_name.title()
full_name_uppercase = full_name.upper()
section_upper = section.upper()
subject_proper = favorite_subject.title()

# Outputs
print("Formatted Output:")
print("Full name:", proper_full_name)
print("Name Code:", full_name_uppercase)
print("Section:", section_upper)
print("Favorite Subject:", subject_proper)
print("Number of characters in Full name:", len(full_name))