name='elgun'
password='root'
count=0
print('Login page')
while True:
    e_name=input('Username: ')
    e_password=input('Password: ')
    if e_name==name:
        if e_password==password:
            print('Login successfully')
        elif len(e_password)>5:
            print('Pass is too long')
        else:
            print('Password is incorrect')
            count+=1
            if count==2:
                break
    else:
        print('Username is not correct')


