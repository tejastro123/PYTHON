import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question = 0

    def play(self):
        while self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            print(f"Question {self.current_question + 1}: {question.question}")
            for i, option in enumerate(question.options):
                print(f"  {i + 1}. {option}")
            answer = input("Enter your answer (1-4): ")
            if int(answer) == question.options.index(question.correct_answer) + 1:
                print("Correct!")
                self.score += 1
            else:
                print(f"Sorry, the correct answer is {question.correct_answer}.")
            self.current_question += 1
        print(f"Game over! Your final score is {self.score} out of {len(self.questions)}.")

def create_questions():
    questions = []
    questions.append(Question("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"], "Paris"))
    questions.append(Question("What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], "Jupiter"))
    questions.append(Question("Who is the CEO of SpaceX?", ["Elon Musk", "Jeff Bezos", "Mark Zuckerberg", "Bill Gates"], "Elon Musk"))
    # Add more questions here...
    random.shuffle(questions)
    return questions

def main():
    questions = create_questions()
    game = QuizGame(questions)
    game.play()

if __name__ == "__main__":
    main()