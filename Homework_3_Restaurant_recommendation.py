#setting time as int
time: int = int(input("enter time: "))

#"make" him bool
is_quick_service = time < 15 and time > 0

#setting time as int
price: int = int(input("enter price: "))

#"make" him bool
is_expensive = price > 100

#printing
print (is_quick_service)
print (is_expensive)

if is_quick_service and not is_expensive:
    print ("recommended")
else:
    print ("not recommended")