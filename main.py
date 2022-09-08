from textwrap import fill
from tkinter import *
from numpy import flip
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_bg = PhotoImage(file = "day_31/images/card_front.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card.create_image(400,263,image = card_bg)
card_title = card.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
card_word = card.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))
card.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file = "day_31/images/wrong.png")
right_img = PhotoImage(file = "day_31/images/right.png")

data = pandas.read_csv("day_31/data/french_words.csv")
data_dict = data.to_dict(orient="records")
current_card = {}
new_image = PhotoImage(file = "day_31/images/card_back.png")

def translated_word():
    card.itemconfig(canvas_image, image = new_image)
    card.itemconfig(card_title, text = "English", fill = "white")
    card.itemconfig(card_word, text = current_card['English'], fill = "white")


def next_card():
    global current_card, fliptimer
    window.after_cancel(fliptimer)
    card.itemconfig(canvas_image, image = card_bg)
    current_card = random.choice(data_dict)
    card.itemconfig(card_title, text = "French", fill = "black")
    card.itemconfig(card_word, text = current_card['French'], fill = "black")
    fliptimer = window.after(3000, translated_word)

wrong_btn = Button(image=wrong_img,highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_btn = Button(image=right_img, highlightthickness=0, command=next_card)
right_btn.grid(column=1, row=1)

fliptimer = window.after(3000, translated_word)

next_card()


window.mainloop()