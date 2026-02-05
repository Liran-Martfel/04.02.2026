#match
rating: int = int(input("enter your rating : "))

match rating:
    case 1:
        print ('really needs improvement')
    case 2:
        print ('needs improvement')
    case 3:
        print ('good')
    case 4 | 5:
        print ('very good')
    case _:
        print ('not in range')

#time - it's like delay in C coding - needs to import library time

import time
time.sleep (2)
