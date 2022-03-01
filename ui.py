from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"




class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler Pro")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        self.scoreboard = Label(text="Score: 0")
        self.scoreboard.config(bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.scoreboard.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="")
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR, font=("Arial", 16, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.scoreboard.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz\n"
                                        f"Your final score is: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1500, self.get_next_question)

