############################################# Multiple Choice Quiz #########################################
#
# keep login_info in a dictionary with function boolean values
# input username : PGR107 password : Python
# if login is successful, show the first choice for the user
# else if the login is failed, show msg "Invalid username and/or password"
# Keep the questions in a list
# Keep the answer in a tuple
# Print correct and wrong answer
# Print the user score & answer/guesses
# Addon: Ask the user to play the game again - I was tired of login  😵‍💫
#
############################################# Multiple Choice Quiz #########################################

login = {"username": "PGR107", "password": "Python"}


def login_info():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == login["username"] and password == login["password"]:
            print(" 🎉 Success!! Welcome to the Multiple Choice Quiz Game! 🎉 ")
            return True
        else:
            print("Invalid username and/or password. Please try again.")


def run_quiz():
    questions = ("Q1. What is the capital of Norway? ",
                 "Q2. What is the currency of Norway? ",
                 "Q3. What is the largest city in Norway? ",
                 "Q4. When is constitution day the national day of Norway? ",
                 "Q5. What color is the background of the Norwegian flag? ",
                 "Q6. How many countries does Norway border? ",
                 "Q7. What is the name of the university in Trondheim? ",
                 "Q8. How long is the border between Norway and Russia? ",
                 "Q9. Where in Norway is Stavanger? ",
                 "Q10. From which Norwegian city did the world’s famous composer Edvard Grieg come? ")

    options = (("A. Bergen", "B. Oslo", "C. Stavanger", "D. Trondheim"),
               ("A. Euro", "B. Pound", "C. Krone", "D. Deutche Mark"),
               ("A. Oslo", "B. Bergen", "C. Stavanger", "D. Trondheim"),
               ("A. 27th May", "B. 17th May", "C. 17th April", "D. 27th April"),
               ("A. Red", "B. White", "C. Blue", "D. Yellow"),
               ("A. 1", "B. 2", "C. 3", "D. 4"),
               ("A. UiS", "B. UiO", "C. NMBU", "D. NTNU"),
               ("A. 96 km", "B. 198 km", "C. 296 km", "D. 396 km"),
               ("A. North", "B. South", "C. South-west", "D. South-east"),
               ("A. Oslo", "B. Bergen", "C. Stavanger", "D. Tromsø"))

    answers = ("B: Oslo", "C: Krone", "A: Oslo", "B: 17th May", "A: Red",
               "C: 3", "D: NTNU", "B: 198 km", "C: South-west", "B: Bergen")
    question_num = 0
    guesses = []
    correct_answers = []
    incorrect_answers = []
    score = 0

    for question in questions:
        print("---------------------------------------------------------")
        print(question)
        print("---------------------------------------------------------")
        for option in options[question_num]:
            print(option)
            print("----------------------")

        guess = input("Enter your answer A, B, C, D >>>  ").upper()
        guesses.append(guess)
        if guess[0] == answers[question_num][0]:
            score += 1
            correct_answers.append(guess)
            print("⭐ Correct! ⭐")
        else:
            incorrect_answers.append(guess)
            print(f"😭 NAH, SORRY, WRONG! ")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("----------------------")
    print("    🏆 RESULTS 🏆      ")
    print("----------------------")

    score = int(score / len(questions) * 100)
    print(f"You scored {score}% out of {len(questions)} questions.")
    print("Correct answers:", end=" ")
    for answer in correct_answers:
        print(answer, end=" ")
    print()

    print("Incorrect answers:", end=" ")
    for answer in incorrect_answers:
        print(answer, end=" ")
    print()


while True:
    if login_info():
        while True:
            run_quiz()
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                exit()
