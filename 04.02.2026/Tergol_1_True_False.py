import time

#bonus
is_prime: int = int(input('Enter an number to check if positive: '))

#tergol - setting up
rating: int = int(input("Enter a number for rating: "))
is_valid: bool = rating in range(1 , 6)
is_best: bool = rating == 5
is_medium: bool = rating == 2 or rating == 3 or rating == 4
is_positive: bool = is_prime > 0

#checking if T or F
if is_valid:
    print(is_valid , 'is_valid is in range')
    time.sleep (1)


    if is_best and is_valid:
        print ('highest score')
        time.sleep (1)
    else:
        print ('Not highest score')
        time.sleep (1)

    if is_medium is is_valid:
        print ('medium score')
        time.sleep (1)
    else:
        print ('score high or low')
        time.sleep (1)

    if is_positive:
        print ('positive' ,is_positive)
        time.sleep (1)
    else:
        print ('negative' ,is_positive)
        time.sleep (1)

else:
    print(is_valid)
    print ('Not in range')


