from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # SCORE LABEL
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 14, "bold"))
        self.score_label.grid(row=0, column=1)

        # CANVAS
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Lorem ipsum",
            font=("Helvetica", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # TRUE BUTTON
        true_png = PhotoImage(file="images/true.png")
        self.true_button = Button(width=100, height=97, image=true_png, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        # FALSE BUTTON
        false_png = PhotoImage(file="images/false.png")
        self.false_button = Button(width=100, height=97, image=false_png, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)