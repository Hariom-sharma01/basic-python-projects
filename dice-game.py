#dice face print
import random
print('DO YOU WANT TO PLAY?'.rjust(55))
s=input()
while s in 'YESyes':
    print('HOW MANY TIME DO YOU WANT TO ROLL DICE?'.rjust(60))
    n=input()
    num=eval(n)
    rolls=[]
    for i in range(num):
        dice=random.randint(1,6)
        rolls.append(dice)
    for i in rolls:
        if i==1:
            print("/---------\\n"
            "|         |\n"
            "|    ",chr(11044),"    |\n"
            "|         |\n"
             "\---------/",sep='')
            continue
        elif i==2:
            print("/---------\\n"
            "|",chr(11044),"        |\n"
            "|         |\n"
            "|         ",chr(11044),"|\n"
             "\---------/",sep='')
            continue
        elif i==3:
            print("/---------\\n"
            "|",chr(11044),"        |\n"
            "|    ",chr(11044),"    |\n"
            "|        ",chr(11044),"|\n"
             "\---------/",sep='')
            continue
        elif i==4:
            print("/---------\\n"
            "|",chr(11044),"       ",chr(11044),"|\n"
            "|         |\n"
            "|",chr(11044),"       ",chr(11044),"|\n"
             "\---------/",sep='')
            continue
        elif i==5:
            print("/---------\\n"
            "|",chr(11044),"       ",chr(11044),"|\n"
            "|    ",chr(11044),"    |\n"
            "|",chr(11044),"       ",chr(11044),"|\n"
             "\---------/",sep='')
            continue
        elif i==6:
            print("/---------\\n"
            "|",chr(11044),"       ",chr(11044),"|\n"
            "|",chr(11044),"       ",chr(11044),"|\n"
            "|",chr(11044),"       ",chr(11044),"|\n"
             "\---------/",sep='')
            continue
    print(f'YOU ROLLED A TOTAL OF:{sum(rolls)}'.rjust(55))
    s=input(f'DO YOU WANT TO ROLL AGAIN?(Y/N)'.rjust(55))
print('THANK YOU FOR PLAYING!!!'.rjust(55))