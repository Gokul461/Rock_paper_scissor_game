from tkinter import *
from PIL import ImageTk, Image
import random

def clear():
	canvas.delete('result')
	canvas.create_image(0, 100, anchor=NW, image=img_p)
	canvas.create_image(500, 100, anchor=NW, image=img_c)

def game(player):
    select = [1, 2, 3]
    computer = random.choice(select)
    if (player == 1):
        canvas.create_image(0, 100, anchor=NW, image=rock_p)
    elif player == 2:
        canvas.create_image(0, 100, anchor=NW, image=paper_p)
    else:
        canvas.create_image(0, 100, anchor=NW, image=scissor_p)
    if computer == 1:
        canvas.create_image(500, 100, anchor=NW, image=rock_c)
    elif computer == 2:
        canvas.create_image(500, 100, anchor=NW, image=paper_c)
    else:
        canvas.create_image(500, 100, anchor=NW, image=scissor_c)
    if player == computer: 
        res = '     Draw'
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or(player == 3 and computer == 2):
        res = '  You won'
    else:
        res = ' Computer\n     won'
    canvas.create_text(390, 350, text='    Result: \n' + res,fill="black", font=('Tw Cen MT', 25), tag='result')
root = Tk()
root.config(bg='purple3')
root.title('Rock Paper Scissor')
root.geometry('800x600')
root.resizable(False,False)
canvas = Canvas(root, width=800,bg='mediumpurple3',height=680)
canvas.grid(row=0, column=0)
l1 = Label(root, text='Player', font=('Maiandra GD', 25),bg = 'mediumpurple3')
l2 = Label(root, text='Computer', font=('Maiandra GD', 25),bg = 'mediumpurple3')
l3 = Label(root, text='Vs', font=('Algerian', 40),bg = 'mediumpurple3')

l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=230)

img_p = Image.open("default.jpeg")
img_p = img_p.resize((300, 300))

img_c = img_p.transpose(Image.FLIP_LEFT_RIGHT)

img_p = ImageTk.PhotoImage(img_p)
img_c = ImageTk.PhotoImage(img_c)

rock_p = Image.open('rock_comp.png')
rock_p = rock_p.resize((300, 300))

rock_c = rock_p.transpose(Image.FLIP_LEFT_RIGHT)

rock_p = ImageTk.PhotoImage(rock_p)
rock_c = ImageTk.PhotoImage(rock_c)

paper_p = Image.open('paper_comp.png')
paper_p = paper_p.resize((300, 300))

paper_c = paper_p.transpose(Image.FLIP_LEFT_RIGHT)

paper_p = ImageTk.PhotoImage(paper_p)
paper_c = ImageTk.PhotoImage(paper_c)

scissor_p = Image.open('sci_comp.png')
scissor_p = scissor_p.resize((300, 300))

scissor_c = scissor_p.transpose(Image.FLIP_LEFT_RIGHT)


scissor_p = ImageTk.PhotoImage(scissor_p)
scissor_c = ImageTk.PhotoImage(scissor_c)

canvas.create_image(0, 100, anchor=NW, image=img_p)
canvas.create_image(500, 100, anchor=NW, image=img_c)
rock_b = Button(root, text='Rock', command=lambda: game(1))
rock_b.place(x=35, y=487)

paper_b = Button(root, text='Paper', command=lambda: game(2))
paper_b.place(x=128, y=487)

scissor_b = Button(root, text='Scissor', command=lambda: game(3))
scissor_b.place(x=220, y=487)

clear_b = Button(root, text='Play again', font=('Times', 10, 'bold'),width=10, command=clear).place(x=110, y=550)

root.mainloop()
