from random import choice
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    to_learn = data.to_dict('records')

def known_card():
    to_learn.remove(current_card)
    to_learn_df = pandas.DataFrame.from_records(to_learn)
    to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    print(len(to_learn))
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)



# -------------------- UI ------------------ #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# BUTTONS
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=known_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()