import random
from tkinter import *
import pyperclip
import math

# list_letters = "abcdefghijklmnopqrstuvwxyz"

# list_letters_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# list_symbols = "!@#$%&()*+-_./?=<>{}|^:;"

# list_numbers = "1234567890"
from tkinter import messagebox

list_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", \
                "v", "w", "x", "y", "z"]
list_letters_capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", \
                        "T", "U", "V", "W", "X", "Y", "Z"]
# for x in range(len(list_letters)): list_letters_capital.append(list_letters[x].capitalize())

list_symbols = ["!", "@", "#", "$", "%", "&", "(", ")", "*", "+", "-", "_", ".", "/", "?", "=", "<", ">", "{", "}", \
                "|", "^", ":", ";"]

list_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = []
len_password = ()
count_chkbox = 0
pop_label_password = ""


def lw():
    if lwcase.get() == 1:
        password.append(list_letters)


    else:
        if list_letters in password:
            password.remove(list_letters)


def num():
    if nm.get() == 1:
        password.append(list_numbers)
    else:
        if list_numbers in password:
            password.remove(list_numbers)


def capital():
    if cap.get() == 1:
        password.append(list_letters_capital)
    else:
        if list_letters_capital in password:
            password.remove(list_letters_capital)


def special():
    if spc.get() == 1:
        password.append(''.join(random.choice(list_symbols)))
    else:
        if list_symbols in password:
            password.remove(list_symbols)


final = []


def global_pop():
    global pop
    pop = Toplevel(ws)
    pop.title("test")
    # pop.config(bg = "black")

    pop_label = Label(pop, text="Your password is:  " + pop_label_password.replace("", ''.join(final)),
                      font=("ComicSansMS", 55, "bold"))  # , bg="black", fg="white")
    pop_label.grid(row=1, column=2, padx=30)

    pop_button1 = Button(pop, text="Shuffle", font=("ComicSansMS", 34, "bold"), command=shuffle)
    pop_button1.grid(row=2, column=1, pady=100, padx=30)

    pop_button2 = Button(pop, text="Generate again", font=("ComicSansMS", 34, "bold"), command = generate)
    pop_button2.grid(row=2, column=2, pady=100, padx=30)

    pop_button3 = Button(pop, text="Copy to clipboard", font=("ComicSansMS", 34, "bold"), command = copy_clipboard())
    pop_button3.grid(row=2, column=3, pady=100)

    # messagebox.showinfo("test",''.join(final))
    # print(''.join(final))


def shuffle():
    pop.destroy()
    random.shuffle(final)
    print(''.join(final))
    global_pop()


def generate():

    password.clear()
    if lwcase.get() == nm.get() == cap.get() == spc.get() == 0:
        return (None)
    else:
        final.clear()
        lw()
        num()
        if cap.get() == 1:
            password.append(list_letters_capital)
        else:
            if list_letters_capital in password:
                password.remove(list_letters_capital)

        if spc.get() == 1:
            password.append(list_symbols)
        else:
            if list_symbols in password:
                password.remove(list_symbols)

        for i in range(lenght.get()):
            final.append(random.choice(random.choice(password)))
        print(''.join(final))

        global_pop()

def generate_again():
    generate()

def copy_clipboard():
    pyperclip.copy(''.join(final))

ws = Tk()

ws.title("Password Generator")
ws.geometry("1200x400")

lwcase = IntVar()
nm = IntVar()
cap = IntVar()
spc = IntVar()
lenght = IntVar()

title = Label(ws, text="PASSWORD GENERATOR", font=("ComicSansMS", 55, "bold"), cursor="dot")
title.grid(row=1, column=2)

text1 = Label(ws, text="Type of characters: ", font=("ComicSansMS", 34, "bold"))
text1.grid(row=2, column=2)

lowercase = Checkbutton(ws, text="Lower case ", onvalue=1, offvalue=0, variable=lwcase, command=lw, \
                        font=("ComicSansMS", 21, "bold"))
lowercase.grid(row=3, column=1)

number = Checkbutton(ws, text="Numbers ", onvalue=1, offvalue=0, variable=nm, command=num, \
                     font=("ComicSansMS", 21, "bold"))
number.grid(row=3, column=3)

capital = Checkbutton(ws, text="Upper case ", onvalue=1, offvalue=0, variable=cap, command=capital, \
                      font=("ComicSansMS", 21, "bold"))
capital.grid(row=4, column=1)

special = Checkbutton(ws, text="Special ", onvalue=1, offvalue=0, variable=spc, command=special, \
                      font=("ComicSansMS", 21, "bold"))
special.grid(row=4, column=3)

text2 = Label(ws, text="What is the lenght of your pass: ", \
              font=("ComicSansMS", 21, "bold"))
text2.grid(row=5, column=1)

len_choice = Spinbox(ws, from_=1, to=100, wrap=True, textvariable=lenght, width=5, \
                     font=("ComicSansMS", 21, "bold"))
len_choice.grid(row=5, column=2)

button = Button(ws, text="GENERATE PASSWORD", command=generate, \
                font=("ComicSansMS", 21, "bold"))
button.grid(row=6, column=2)

ws.mainloop()
