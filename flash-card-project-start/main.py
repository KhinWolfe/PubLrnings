import pandas

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
timer = None
word = {}
def new_card():
    global timer, word
    word = random.choice(to_learn)
    try:
        window.after_cancel(timer)
    except:
        pass
    finally:
        canvas.itemconfig(card_side, image=card_front_img)
        canvas.itemconfig(card_title, fill="black", text="French")
        canvas.itemconfig(card_word, fill="black", text=word["French"])
        timer = window.after(3000, flip_card)


def flip_card():
    global word
    canvas.itemconfig(card_side, image=card_back_img)
    canvas.itemconfig(card_word, fill="white", text=word["English"])
    canvas.itemconfig(card_title, fill="white", text="English")

def remove_card():
    global word
    to_learn.remove(word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    new_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
card_right_img = PhotoImage(file="./images/right.png")
card_wrong_img = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800, height=526)
card_side = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

r_btn = Button(image=card_right_img, highlightthickness=0, bd=0, command=remove_card)
r_btn.grid(column=0,row=1)
W_btn = Button(image=card_wrong_img, highlightthickness=0, bd=0, command=new_card)
W_btn.grid(column=1,row=1)

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

to_learn = data.to_dict(orient="records")

new_card()


window.mainloop()
