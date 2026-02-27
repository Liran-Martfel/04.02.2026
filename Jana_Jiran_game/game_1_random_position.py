import random
from random import choice

chooice = None
sure: str
where = random.choice (['in bed','on the floor','standing up','on a chair','in front of a mirror','your choice','shower','in car'])
position = random.choice(
    ['Doggy', 'cowgirl', 'blowjob', 'misenery', 'revers cowgirl', 'going down on your girl', 'upside down blowjob',
     'handjob', 'foot job', 'somthing new', 'ass eating (for your girl)', 'sitting on face', 'finger in ass'])
finish = random.choice (['cum on boobs','cum on ass','cum on feet','cum in mouth','cum on back', 'cum on leg'])
print (f'you will have sex at {where} in this position: {position}, and will be finished on or in {finish}')


while True:
    chooice = int(input('press 1 for new choice in position or 0 to stay: '))
    if chooice == 1:
        position = random.choice(
            ['Doggy', 'cowgirl', 'blowjob', 'misenery', 'revers cowgirl', 'going down on your girl',
             'upside down blowjob', 'handjob', 'foot job', 'somthing new', 'ass eating (for your girl)',
             'sitting on face', 'finger in ass'])
        print (position)
    elif chooice == 0:
        sure = input("are you sure? answer with y or n: ")
        if sure == 'y':
            break
    else:
        continue



