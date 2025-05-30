import tkinter as tk
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("paper_scissors_rock_with_gui")
root.geometry("800x800")
lst = ["paper", "scissors", "rock","spok","lizard"]

image1 = Image.open("image_background.png")
image1 = image1.resize((800 , 800))
image2 = ImageTk.PhotoImage(image1)
win = 0
lose = 0
equality = 0
random1 = random.choice(lst)

background_label = tk.Label(root, image=image2)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def paper(paper):
    global win, lose, equality
    if paper == "paper"and random1 == "scissors":
        label.config(text="Загуби !!! ")
        lose += 1
    elif paper == "paper"and random1 == "paper":
        label.config(text="Равенство !!!")
        equality += 1
    elif paper == "paper" and random1 == "rock":
        label.config(text="Ти спечели !!! ")
        win += 1
    elif paper == "paper" and random1 == "spok":
        label.config(text="Ти спечели")
        win += 1
    elif paper == "paper" and random1 == "lizard":
        label.config(text="Загуби !!!")
        lose += 1
    else :
        label.config(text= "ERROR")

def scissors(scissors):
    global win, lose, equality
    if scissors == "scissors"and random1 == "rock":
        label.config(text="Загуби !!! ")
        lose += 1
    elif scissors == "scissors"and random1 == "scissors":
        label.config(text="Равенство !!!")
        equality += 1
    elif scissors == "scissors" and random1 == "paper":
        label.config(text="Ти спечели !!! ")
        win += 1
    elif scissors == "scissors" and random1 == "spok":
        label.config(text="Ти спечели")
        win += 1
    elif scissors == "scissors" and random1 == "lizard":
        label.config(text="Загуби !!!")
        lose += 1
    else :
        label.config(text= "ERROR")

def rock(rock):
    global win, lose, equality
    if rock == "rock" and random1 == "paper":
        label.config(text="Загуби !!! ")
        lose += 1
    elif rock == "rock" and random1 == "rock":
        label.config(text="Равенство !!!")
        equality += 1
    elif rock == "rock" and random1 == "scissors":
        label.config(text="Ти спечели !!! ")
        win += 1
    elif rock == "rock" and random1 == "lizard":
        label.config(text="Ти спечели")
        win += 1
    elif rock == "rock" and random1 == "spok":
        label.config(text="Загуби !!!")
        lose += 1
    else:
        label.config(text="ERROR")
def lizard(lizard):
    global win, lose, equality
    if lizard == "lizard" and random1 == "paper":
        label.config(text="Ти спечели !!! ")
        win += 1
    elif lizard == "lizard" and random1 == "rock":
        label.config(text="Загуби !!!")
        lose  += 1
    elif rock == "lizard" and random1 == "scissors":
        label.config(text="Загуби !!! ")
        lose += 1
    elif lizard == "lizard" and random1 == "spok":
        label.config(text="Ти спечели")
        win += 1
    elif lizard == "lizard" and random1 == "lizard":
        label.config(text="Равенство !!!")
def spok (spok):
    global win, lose, equality
    if spok == "spok" and random1 == "paper":
        label.config(text="Загуби !!! ")
        lose += 1
    elif spok == "spok" and random1 == "rock":
        label.config(text="Ти спечели !!!")
        win += 1
    elif spok == "spok" and random1 == "scissors":
        label.config(text="Ти спечели !!! ")
        win += 1
    elif spok == spok and random1 == "lizard":
        label.config(text="Загуби")
        lose += 1
    elif spok == spok and random1 == "spok":
        label.config(text="Равенство !!!")
        equality += 1

def exit1(tab):
    if tab == "tab":
        exit()
    else:
        label.config(text="ERROR")

button1 = tk.Button(root,text = "Paper", command=lambda:paper("paper"),font=("Arial",29),fg="orange")
button1.place(x=100,y=100)

button2 = tk.Button(root,text= "Scissors", command=lambda:scissors("scissors"),font=("Arial",29),fg="blue")
button2.place(x=100, y=150)

button3 = tk.Button(root,text="Rock", command=lambda:rock("rock"),font=("Arial",29),fg="green")
button3.place(x=100, y=200)

button7 = tk.Button(root,text="Гущер",command=lambda:lizard("lizard"),font=("Arial",29),fg="red")
button7.place(x=100, y=250)

button8 = tk.Button(root,text="Спок",command=lambda:spok("spok"),font=("Arial",29),fg="blue")
button8.place(x=100, y=300)
button4 = tk.Button(root,text="Exit", command=lambda:exit1("tab"),font=("Arial",29),fg="red")
button4.place(x=100, y=400)

label = tk.Label(root,text="Нека започваме",font=("Arial",29))
label.place(x=400, y=100)


def restart11():
    global random1
    random1 = random.choice(lst)
    label.config(text="Нека започваме")

run = False
def stat():
    global run,label2
    if run :
        label2.place_forget()
        run = False
    else:
        label2 = tk.Label(root, text=f"win = {win}, lose = {lose}, equality = {equality}",bg="green" ,font=("Arial", 29))
        label2.place(x=100,y=450)
        run = True

button5 = tk.Button(root,text="Restart", command=restart11,font=("Arial",29),fg="pink")
button5.place(x=400, y=250)

button6 = tk.Button(root,text="Stat",command=stat,font=("Arial",29),fg="orange")
button6.place(x=100, y=350)

root.mainloop()