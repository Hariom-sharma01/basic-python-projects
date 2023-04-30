# secure password
import random
def password():
    s=''
    l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    l2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    l3=['0','1','2','3','4','5','6','7','8','9']
    l4=['@','#','&','*','$']
    for  i in range(14):
        if i<=7:
            s+=random.choice(l1)
        elif i>7 and i<=9:
            s+=random.choice(l2)
        elif i>9 and i<=12:
            s+=random.choice(l3)
        else:
            s+=random.choice(l4)
    print('Your secure password is::',s)
print('To generate your password press enter')
input()
password()