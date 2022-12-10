#importing the random and string modules!
import random
import string

#prints the welcome message
print("Hello, Welcome to Password Gen!")

#gets the password length from the user
length = int(input('\nEnter the length of password: '))

#rather then typing abc and 123 you can use string and ascii which already has it all stored
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#adds all up
all = lower + upper +  num + symbols

#creates the randomness and uses the length provided by the user
temp = random.sample(all,length)

#creates the password by using the join
password = "".join(temp)

#prints the password
print(password)

#created a simple password gen project, next is to add a question to ask if another password is needed and continue from there, 

ans = str(input("\nDo you need another password? "))

while ans == 'yes':
    length = int(input('\nEnter the length of password: '))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper +  num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    print(password)
    ans = str(input("\nDo you need another password? "))
    continue
    if ans == no:
        break
else:
    print ("Thank you, have a great day!")