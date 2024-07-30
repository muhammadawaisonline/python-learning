def ask_question(question, correct_answer):
    user_answer = input(question + "")
    if user_answer.lower() == correct_answer.lower():
        print("correct!")
        return True
    else:
        print("Wrong: The correct answer is: ", correct_answer)
        return False
    

