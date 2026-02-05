import time

print("welcome you the post office delivery, please enter the following information: ")
time.sleep(1)
print ("*" *40)

#inputs
first_name: str = input ("please enter your first name: ")
time.sleep(0.5)

#first name must be lower
while first_name is not first_name.islower():
    if first_name.islower():
        break
    first_name: str = input ("please enter your first name in small letters: ")
#################################################################
last_name: str = input ("please enter your last name: ")
time.sleep(0.5)

#last name must be upper
while last_name is not last_name.isupper():
    if last_name.isupper():
        break
    last_name: str = input ("please enter your last name in CAPITAL LETTERS: ")
#################################################################
country: str = input ("please enter your country: ")
time.sleep(0.5)

#must be 3 letters
while country is not country.isalpha():
    if country.isalpha() and len (country) <=3:
        break
    country: str = input ("please enter your country with 3 letters at most: ")
#################################################################
city_address: str = input ("please enter your city address: ")
time.sleep(0.5)
#################################################################
zip_code = input("please enter your zip code: ")

#must be at least four dig zip code
while zip_code is not zip_code.isdigit():
        if len(zip_code) >= 4 and zip_code.isdigit():
            break
        else:
            zip_code: str = input("please enter your 4 digit zip code: ")

#################################################################
print ("processing..... please wait"'\n')
time.sleep(1.5) #make it real

print(f"FOR: {last_name}, {first_name}\nCOUNTRY: {country}\nADDRESS: {city_address}\nZIP: {zip_code}")
