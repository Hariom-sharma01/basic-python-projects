import random
def game():
    l1=['Rock','Paper','Scissor']
    a=random.choice(l1) 
    print('Please select one option against computer from the given!!')
    print('Rock::\n','Paper::\n','Scissor::')
    t1=input()
    t=t1.title()
    if t=='Rock' and a=='Scissor':
        print('You win!!')
    elif t=='Rock' and a=='Paper':
        print('You loss')
    elif t=='Rock' and a=='Rock':
        print("it's draw ")
    elif t=='Paper' and a=='Scissor':
        print('You loss ')
    elif t=='Paper' and a=='Paper':
        print("it's draw ")
    elif t=='Paper' and a=='Rock':
        print('You win!!')
    elif t=='Scissor' and a=='Scissor':
        print("it's draw ")
    elif t=='Scissor' and a=='Paper':
        print('You win!!')
    else:
        print('You loss')
    print('Your move::',t,'Vs')
    print("computer's move::",a)
    print('Do you want to play again??y/n')
    s=input()
    return s
print('Welcome to the game'.center(100))
print('Rock::Vs::Paper::Vs::Scissor')
print('Do you want to try it??:y/n')
s1=input()
if s1 in 'Yy':
    re=game()
    while(re not in 'Nn'):
        re=game()
    print('Thank You!')
else:
    print('Thank You!')
        
   

