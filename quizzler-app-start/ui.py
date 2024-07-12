THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.c_canvas = Canvas(width=300, height=250)
        self.q_body = self.c_canvas.create_text(
            150,
            125,
            width=280,
            text="hello",
            font=("Arial", 20, "italic")
        )
        self.c_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.T_button = Button(image=true_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.T_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.F_button = Button(image=false_img, highlightthickness=0, bd=0, command=self.false_pressed)
        self.F_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.c_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.c_canvas.itemconfig(self.q_body, text=q_text)
        else:
            self.c_canvas.itemconfig(self.q_body, text="You've reached the end of the quiz.")
            self.T_button.config(state="disabled")
            self.F_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):

        if is_right:
            self.c_canvas.config(bg="green")
        else:
            self.c_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
