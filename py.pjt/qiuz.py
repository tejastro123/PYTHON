  
def main():
    score = 0
    for question in questions:
        user_answers = display_question(question["question"], question["answers"])
        score += validate_answers([question], [user_answers])[0]
    print("Your score: {}/{}".format(score, len(questions)))

if __name__ == "__main__":
    main()