import random as rnd


digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

upcase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
symbol = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
# do-while loop
while True:
    number = int(input("Enter how many password you want to generate\n"))
    length=int(input("Enter the password length you want (Enter the length above 5 for mor security)\n"))
    if length>=5 and number>=1:
        break
    print("Try again")
# password generator loop
for i in range(number):
    password = ""
    password=password+rnd.choice(upcase)+rnd.choice(lowcase)+rnd.choice(symbol)+rnd.choice(digit)
    for j in range(length-4):
        password=password+rnd.choice([rnd.choice(upcase),rnd.choice(lowcase),rnd.choice(symbol),rnd.choice(digit)])
    tmp=[]
    tmp.extend(password)
    rnd.shuffle(tmp)
    password="".join(tmp)
    print(password,end="\n\n")