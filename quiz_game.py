def ask_question(question, correct_answer):
    user_answer = input(question + "")
    if user_answer.lower() == correct_answer.lower():
        print("correct!")
        return True
    else:
        print("Wrong: The correct answer is: ", correct_answer)
        return False
    

def quiz_game():
    score = 0

    print("Welcome to the Quiz Game.")
    print("Let's get started\n")

    if ask_question("What is the capital of France?", "Paris"):
        score+=1

    if ask_question("What is 5 + 7?", "12"):
        score+=1
    if ask_question("Who wrote 'Hamlet?'", "Sharspeare"):
        score+=1
    if ask_question("What is the chemical symbol for water?", "H2O"):
        score+=1
    print("\n You Got:", score, "out of 4 questions correct!")

quiz_game()
