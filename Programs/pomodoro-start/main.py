from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps <= 8:
        if reps % 8 == 0:
            count_down(LONG_BREAK_MIN * 60)
            title_label.config(text="BREAK", fg=RED)
        elif reps % 2 == 0:
            count_down(SHORT_BREAK_MIN * 60)
            title_label.config(text="BREAK", fg=PINK)
        else:
            count_down(WORK_MIN * 60)
            title_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text="✓", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)

window.mainloop()
