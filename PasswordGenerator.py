import random
import string

def randomPassGenerator(length,supporting=''):
    password=str(supporting)
    support_len=len(str(supporting))
    random_len=length-support_len

    for i in range(random_len):
        word=random.choice([random.choice(string.ascii_letters),random.choice(string.punctuation)])
        password=password+word
    return password

print('-----------------------------------------')
print('Welcome to random password generator ^_^')
print('-----------------------------------------')
password_lenght=int(input('Please enter the length of your password:'))
user_input=input('Do you want to add your own supporting data(Yes/No):')
if(user_input.lower()=='yes'):
    data=input('Enter your data:')
    answer=randomPassGenerator(password_lenght,data)

elif(user_input.lower()=='no'):
    answer=randomPassGenerator(password_lenght)

else:
    print('Please answer in yes or no.')
    answer='The password is not generator because of wrong input T_T'
print(answer)