# Quiz App in Python (English Version)

def quiz():
    questions = {
        "What is the capital of India?": "Delhi",
        "Python is what type of language?": "Programming",
        "What is 2 + 2?": "4"
    }

    score = 0
    print("\n--- Quiz App ---\n")

    for question, answer in questions.items():
        user_ans = input(question + " : ")
        if user_ans.strip().lower() == answer.lower():
            print("✅ Correct Answer!")
            score += 1
        else:
            print("❌ Wrong Answer! Correct is:", answer)

    print("\nYour score is:", score, "/", len(questions))

quiz()
