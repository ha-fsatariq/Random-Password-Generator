import random
import string

def randomPassGenerator(length,numbers,chars,specialchars,supporting=''):
    try:
        random_selection=''
        password=supporting
        if(length >= 1):
            
            if specialchars:
                random_selection=random_selection+string.punctuation
            if chars:
                random_selection=random_selection+string.ascii_letters
            if numbers:
                random_selection=random_selection+string.digits
                
            for i in range(length):
                password=password+random.choice(random_selection)
            return password
        else:
            raise ValueError(
                "Lenght of the password should be greater then zero.")
    except ValueError as e:
        print(e)

print('-----------------------------------------')
print('Welcome to random password generator ^_^')
print('-----------------------------------------')

nums=input('If you want to include numbers then please enter yes otherwise no: ').lower() == 'yes'
specChars=input('If you want to include special charaters then please enter yes otherwise no: ').lower() == 'yes'
Chars=input('If you want to include charaters then please enter yes otherwise no: ').lower() == 'yes'

if(nums==False and specChars==False and Chars==False):
    print('You have to select atleast one of the options.')
else:
    user_input=input('Do you want to add your own supporting data(Yes/No):')
    password_lenght=int(input('Please enter the length of your password other then your data:'))
    if(user_input.lower()=='yes'):
        data=input('Enter your data:')
        answer=randomPassGenerator(password_lenght,supporting=data,numbers=nums,chars=Chars,specialchars=specChars)

    elif(user_input.lower()=='no'):
        answer=randomPassGenerator(password_lenght,numbers=nums,chars=Chars,specialchars=specChars)

    else:
        print('Please answer in yes or no.')
        answer='The password is not generator because of wrong input T_T'
    print(answer)
