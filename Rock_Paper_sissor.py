from tkinter import *
from PIL import Image, ImageTk
from random import randint

window= Tk()
window.title("ROCK PAPER AND SCISSOR")
window.configure(bg="black")

#Loaded Images
image_rock1 =ImageTk.PhotoImage(Image.open("rock 1.png"))
image_paper1 =ImageTk.PhotoImage(Image.open("paper 1.png"))
image_scissor1 =ImageTk.PhotoImage(Image.open("scissor 1.png"))
image_rock2 =ImageTk.PhotoImage(Image.open("rock 2.png"))
image_paper2 =ImageTk.PhotoImage(Image.open("paper 2.png"))
image_scissor2 =ImageTk.PhotoImage(Image.open("scissor 2.png"))


#label for computer and player
label_player=Label(window, image=image_scissor1)
label_computer=Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

#Score for computer and player
computer_score=Label(window,text=0,font=("arial",60, "bold"),fg="red")
player_score=Label(window,text=0,font=("arial",60, "bold"),fg="red")
computer_score.grid(row=1, column=1)
player_score.grid(row=1, column=3)

#indicator placed
player_indicator =Label(window,font=("arial",60, "bold"),
                        text="PLAYER",bg="orange",fg="blue")
computer_indicator =Label(window,font=("arial",60, "bold"),
                        text="COMPURTER",bg="orange",fg="blue")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

def updateMessage(a):
    final_message['text']= a

def Computer_update():
    final =int(computer_score['text'])
    final +=1
    computer_score["text"]= str(final)

def Player_update():
    final =int(player_score['text'])
    final +=1
    player_score["text"]= str(final)


def winner_check(p,c):
    if p==c:
        updateMessage("Its a tie!")

    elif p=="rock":
        if c=="paper":
            updateMessage("Computer wins!")
            Computer_update()

        else:
            updateMessage("Player wins!")
            Player_update()

    elif p=="paper":
        if c=="scissor":
            updateMessage("Computer winns!")
            Computer_update()
        else:
            updateMessage("Player wins!")
            Player_update()

    elif p== "scissor":
        if c=="rock":
            updateMessage("Computer wins!")
            Computer_update()

        else:
            updateMessage("Player wins!")
            Player_update()
    else:
        pass

to_select=["rock", "paper", "scissor"]

def choice_update(a):
    choice_computer = to_select[randint(0,2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer== "paper":
        label_computer.configure(image=image_paper2)
    elif choice_computer== "scissor":
        label_computer.configure(image=image_scissor2)

    if a=="rock":
        label_player.configure(image=image_rock1)

    elif a=="paper":
        label_player.configure(image=image_paper1)

    elif a=="scissor":
        label_player.configure(image=image_scissor1)

    winner_check(a,choice_computer)


#message update to who will be the  winner
final_message=Label(window,font=("arial",60,"bold"),bg="red",fg="white")
final_message.grid(row=3, column=2)


# Button placed
button_rock = Button(window,width =16, height=3, text="ROCK",
                     font=("arial",20, "bold"), bg ="yellow",fg="red",command=lambda:choice_update("rock")).grid(row=2, column=1)

button_paper = Button(window,width =16, height=3, text="PAPER",
                     font=("arial",20, "bold"), bg ="yellow",fg="red",command=lambda:choice_update("paper")).grid(row=2, column=2)

button_scissor = Button(window,width =16, height=3, text="SCISSOR",
                     font=("arial",20, "bold"), bg ="yellow",fg="red",command=lambda:choice_update("scissor")).grid(row=2, column=3)

window.mainloop()