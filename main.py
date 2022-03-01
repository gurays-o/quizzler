from ui import QuizInterface
from data import question_bank
from quiz_brain import QuizBrain

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
