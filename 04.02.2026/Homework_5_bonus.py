new_password: str = input ("please enter your password: ")
is_upper = False
is_lower = False
is_digit = False

for i in new_password:
    if i.isupper():
        is_upper = True

    elif i.islower():
        is_lower = True

    elif i.isdigit():
        is_digit = True

if is_upper == True and is_lower == True and is_digit == True:
    print ("valid password")
else:
    print("weak password")