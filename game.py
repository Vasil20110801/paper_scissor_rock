import tkinter as tk
import random

root = tk.Tk()
root.title("paper_scissors_rock_with_gui")
root.geometry("800x800")
lst = ["paper", "scissors", "rock"]

win = 0
lose = 0
equality = 0
random1 = random.choice(lst)

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
    else:
        label.config(text="ERROR")


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

button4 = tk.Button(root,text="Exit", command=lambda:exit1("tab"),font=("Arial",29),fg="red")
button4.place(x=100, y=250)

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
        label2 = tk.Label(root, text=f"win = {win}, lose = {lose}, equality = {equality}", font=("Arial", 29))
        label2.place(x=100,y=400)
        run = True

button5 = tk.Button(root,text="Restart", command=restart11,font=("Arial",29),fg="pink")
button5.place(x=400, y=250)

button6 = tk.Button(root,text="Stat",command=stat,font=("Arial",29),fg="orange")
button6.place(x=100, y=300)

root.mainloop()