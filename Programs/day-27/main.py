from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("Tkinter window")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Courier", 24, "normal"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
my_button = Button(text="Click me", command=button_clicked)
my_button.grid(column=1, row=1)

# New button
new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())


window.mainloop()