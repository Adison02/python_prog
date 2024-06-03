from tkinter import *

def calc_action():
    calc_km = int(miles_input.get()) * 1.609344
    label_03.config(text=round(calc_km))

window = Tk()
window.title("Mile to Km Converter")
window.config( padx=20, pady=20)

miles_input = Entry()
miles_input.config(width=7)
miles_input.grid(column=1, row=0)

label_01 = Label()
label_01.config(text="Miles")
label_01.grid(column=2, row=0)

label_02 = Label()
label_02.config(text="is equal to")
label_02.grid(column=0, row=1)

label_03 = Label()
label_03.config(text="0")
label_03.grid(column=1, row=1)

label_04 = Label()
label_04.config(text="Km")
label_04.grid(column=2, row=1)

calc_button = Button()
calc_button.config(text="Calculate", command=calc_action)
calc_button.grid(column=1, row=2)

window.mainloop()