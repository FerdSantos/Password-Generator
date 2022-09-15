import random


list_letters = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",\
                "v", "w", "x", "y", "z"]
list_letters_capital = []
for x in range(len(list_letters)): list_letters_capital.append(list_letters[x].capitalize())

list_symbols = ["!", "@", "#", "$", "%", "&", "(", ")", "*", "+", "-", "_", ".", "/", "?", "=", "<", ">", "{", "}",\
                "|", "^", ":", ";"]

list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
len_password = ()


while True :
    len_password = 10 #input("What is the password lenght you wish? : ")
    if type(int(len_password)) == int:
        len_password = int(len_password)
        break
    elif type(len_password) == str:
        print("Please choose a valid length (ie: 9)")


password = []

for i in range(len_password):
    password.append(''.join(random.choices(list_numbers + list_symbols + list_letters + list_letters_capital)))

password = ''.join((password))
print((password))

