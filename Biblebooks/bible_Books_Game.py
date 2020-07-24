import random
import json


def main():
    bible_Books = [
        "Genesis",
        "Exodus",
        "Leviticus",
        "Numbers",
        "Deuteronomy",
        "Joshua",
        "Judges",
        "Ruth",
        "1 Samuel",
        "2 Samuel",
        "1 Kings",
        "2 Kings",
        "1 Chronicles",
        "2 Chronicles",
        "Ezra",
        "Nehemiah",
        "Esther",
        "Job",
        "Psalms",
        "Proverbs",
        "Ecclesiastes",
        "Song of Solomon",
        "Isaiah",
        "Jeremiah",
        "Lamentations",
        "Ezekiel",
        "Daniel",
        "Hosea",
        "Joel",
        "Amos",
        "Obadiah",
        "Jonah",
        "Micah",
        "Nahum",
        "Habakkuk",
        "Zephaniah",
        "Haggai",
        "Zechariah",
        "Malachi",
        "Matthew",
        "Mark",
        "Luke",
        "John",
        "Acts",
        "Romans",
        "1 Corinthians",
        "2 Corinthians",
        "Galatians",
        "Ephesians",
        "Philippians",
        "Colossians",
        "1 Thessalonians",
        "2 Thessalonians",
        "1 Timothy",
        "2 Timothy",
        "Titus",
        "Philemon",
        "Hebrews",
        "James",
        "1 Peter",
        "2 Peter",
        "1 John",
        "2 John",
        "3 John",
        "Jude",
        "Revelation",
    ]
    print("*" * 160)
    print(
        "\n                                                        Welcome to Harold's Bible Order Tester, 'H-BOT'!\n"
    )
    print("*" * 160)

    keepGoing = True
    number_correct = 0
    # This loop determines how many questions will be on the test
    while keepGoing:
        print("\nHow many questions would you like? ")
        num_questions = input().strip()
        while not num_questions.isnumeric() or num_questions == 0:
            print("ERROR: Please enter a number")
            print("\nHow many questions would you like? ")
            num_questions = input().strip()
            print("-" * 80)
        print("-" * 80)
        keepGoing = Game(num_questions, bible_Books, number_correct)
    print("Thanks for playing H-BOT!")


def Game(num_questions, bible_Books, number_correct):

    number_left = int(num_questions)
    q_exceptions = []
    # ========================================================
    # values for incorrect answer scorecard. They are stored here
    # so that they do not reset with each loop iteration.
    # ========================================================
    incorrect_response_book = []
    incorrect_response_boolean = []
    incorrect_response_wrong_ans = []
    incorrect_response_right_ans = []
    # ========================================================
    # Where the question "What bible book comes.." is made
    # ========================================================
    for questions in list(range(int(num_questions))):
        random_bit = random.getrandbits(1)
        random_boolean = bool(random_bit)
        answer_randomizer_no_repeat = []
        mult_choice_ans = []
        # --------------------------------------------------------
        # if statements meant to translate
        # the random_bit value to before or after for use in the question.
        # --------------------------------------------------------
        if random_boolean == True:
            random_boolean = "before"
        else:
            random_boolean = "after"
        # a random_book of the bible is selected for the question
        random_book = random.randrange(0, 65, 1)
        # --------------------------------------------------------
        # meant to add the books used in each questions to an exceptions list so that you
        # don't get the same question twice until you have cycled through all 66 books of the bible
        # --------------------------------------------------------
        if len(q_exceptions) == 65:
            q_exceptions = []
        while random_book in q_exceptions:
            random_book = random.randrange(0, 65, 1)
        if random_book not in q_exceptions:
            q_exceptions.append(random_book)
        # So you dont get a "what is before Genesis" or "...after Revelation" question
        if random_book == 0:
            random_boolean = "after"
        if random_book == 65:
            random_boolean = "before"
        # printed question
        print(
            "\nWhat book of the Bible comes "
            + random_boolean
            + " "
            + bible_Books[random_book]
            + "?"
        )
        # ========================================================
        # Where the multiple choice is generated.
        # ========================================================
        # This statement is to make a semi random variation in the number of choices
        if random_boolean == "before":
            mult_letters = [1, 2, 3, 4]
        else:
            mult_letters = [1, 2, 3, 4, 5]

        mult_letters_index = 0
        # --------------------------------------------------------
        # begins with assigning RNG to certain values.
        # Also a no-repeat loop so that none of the answers repeat within
        # the same set of mult choice answers
        # --------------------------------------------------------
        for items in mult_letters:
            before_random_book = random_book - 1
            after_random_book = random_book + 1
            if random_boolean == "before":
                answer_randomizer = random.randrange(1, 5, 1)
            else:
                answer_randomizer = random.randrange(1, 6, 1)
            random_ans = random.randrange(2, 66, 1)
            # loop is for ensuring that the answer_randomizer value does not reapeat. This ensures that you will always get 1 correct answer
            while answer_randomizer in answer_randomizer_no_repeat:
                if random_boolean == "before":
                    answer_randomizer = random.randrange(1, 5, 1)
                else:
                    answer_randomizer = random.randrange(1, 6, 1)
            if answer_randomizer not in answer_randomizer_no_repeat:
                answer_randomizer_no_repeat.append(answer_randomizer)
            # ensures that the incorrect answers are not repeated in the same question
            while random_ans in mult_choice_ans or random_ans == random_book:
                random_ans = random.randrange(1, 66, 1)
            # adds the random_book in the list so that you will not get it as an answer
            # mult_choice_ans.append(random_book)
            # --------------------------------------------------------
            # The following if statements give conditions
            # for a correct answer and a means of producing incorrect answers.
            # Then the values are stored for reference for no-repeat and
            # for if an incorrect answer is selected
            # --------------------------------------------------------

            if answer_randomizer == 1 and random_boolean == "after":
                correct_answer = mult_letters_index + 1
                mult_choice_ans.append(after_random_book)
                print(
                    str(mult_letters[mult_letters_index])
                    + ". "
                    + str(bible_Books[after_random_book])
                )
                mult_letters_index += 1
            elif answer_randomizer == 2 and random_boolean == "before":
                correct_answer = mult_letters_index + 1
                mult_choice_ans.append(before_random_book)
                print(
                    str(mult_letters[mult_letters_index])
                    + ". "
                    + str(bible_Books[before_random_book])
                )
                mult_letters_index += 1
            else:
                print(
                    str(mult_letters[mult_letters_index])
                    + ". "
                    + bible_Books[random_ans]
                )
                if random_ans not in mult_choice_ans:
                    mult_choice_ans.append(random_ans)
                mult_letters_index += 1
        # Answer input and statements for if there are 4 or 5 choices
        ans = input("\nYour answer? ").strip()
        if random_boolean == "before":
            while not ans.isnumeric() or int(ans) > 4 or int(ans) < 1:
                print("ERROR: Please select '1', '2', '3', or '4' as a valid response")
                ans = input("\nYour answer? ").strip()
        else:
            while not ans.isnumeric() or int(ans) > 5 or int(ans) < 1:
                print("ERROR: Please select '1', '2', '3', or '4' as a valid response")
                ans = input("\nYour answer? ").strip()

        # ========================================================
        # # Correct/Incorrect answer response and counter for correct answer
        # ========================================================
        if int(ans) == correct_answer:
            print("\nCorrect!")
            number_correct += 1
        # --------------------------------------------------------
        # if the answer is incorrect the data for that question is stored in lists.
        # in INT for for reference on the scorecard.
        # --------------------------------------------------------
        else:
            print("\nIncorrect :,(")
            # how we find and store the bible book that was selected incorrectly
            wrong = int(ans) - 1
            wrong_ans = mult_choice_ans[wrong]
            # here is where we append the data to lists noted above the initial for loop to be accessed at the end.
            if random_boolean == "after":
                incorrect_response_book.append(random_book)
                incorrect_response_boolean.append(random_boolean)
                incorrect_response_right_ans.append(after_random_book)
                incorrect_response_wrong_ans.append(wrong_ans)
            if random_boolean == "before":
                incorrect_response_book.append(random_book)
                incorrect_response_boolean.append(random_boolean)
                incorrect_response_right_ans.append(before_random_book)
                incorrect_response_wrong_ans.append(wrong_ans)

        # --------------------------------------------------------
        # The following statements are for the questions left counter.
        # The messages changes depending on number_left variable's proximity to 0.
        # This is for when 1 question remains
        # --------------------------------------------------------
        if number_left == 2:
            number_left -= 1
            print("Only " + str(number_left) + " question left...")
            print("-" * 80)
        # This is for when 3-2 questions remain
        elif number_left == 4 or number_left == 3:
            number_left -= 1
            print(
                "THE FINAL COUNTDOOOWWWN!! " + str(number_left) + " questions left..."
            )
            print("-" * 80)
        # Final question
        elif number_left == 1:
            print("Calculating your results...")
        # Greater than 3 questions remain
        else:
            number_left -= 1
            print("You have " + str(number_left) + " left...")
            print("-" * 80)
    # ========================================================
    # Scorecard section. I will calculate a percentage and give a grade.
    # Also a correction sheet will be printed.
    # ========================================================
    percent = number_correct / int(num_questions)
    percent *= 100
    # --------------------------------------------------------
    # Grades depending on your percentage
    # --------------------------------------------------------
    if percent == 100:
        print(
            "\nCongratulations bible scholar! You got an 'A+' at "
            + str(int(percent))
            + "%. WOOT!"
        )
    elif percent >= 90 and percent < 100:
        print("\nYou got an 'A' at " + str(int(percent)) + "%. Awesome work!")
    elif percent >= 80 and percent < 90:
        print("\nYou got an 'B' at " + str(int(percent)) + "%. Good job!")
    elif percent >= 70 and percent < 80:
        print("\nYou got an 'C' at " + str(int(percent)) + "%. Well... You passed =)!")
    elif percent >= 60 and percent < 70:
        print("\nYou got an 'D' at " + str(int(percent)) + "%. Ouch!")
    else:
        print(
            "\nYou got an 'F' at "
            + str(int(percent))
            + "%. JW.ORG has a free copy of the bible for you to study from!"
        )
    # --------------------------------------------------------
    # This is the correction sheet section
    # --------------------------------------------------------
    print("\n" + "=" * 80)
    print("\nHere are your incorrect answers and the correct responses\n")
    print("=" * 80)

    incorrect_response_index = 0
    # this will loop through to produce all of the incorrect answers and their corrections
    while incorrect_response_index <= len(incorrect_response_book) - 1:
        # book in the question converted to str value// boolean does not need conversion
        response_book = incorrect_response_book[incorrect_response_index]
        response_book = bible_Books[response_book]
        # wrong ans converted to book
        response_wrong_ans = incorrect_response_wrong_ans[incorrect_response_index]
        response_wrong_ans = bible_Books[response_wrong_ans]
        # correct answer converted to book
        response_right_ans = incorrect_response_right_ans[incorrect_response_index]
        response_right_ans = bible_Books[response_right_ans]
        print(
            "\nWhat book of the Bible comes "
            + incorrect_response_boolean[incorrect_response_index]
            + " "
            + response_book
            + "?\n"
        )
        print("Your response was " + response_wrong_ans)
        print("The correct answer was " + response_right_ans)
        incorrect_response_index += 1
        print("=" * 80)

    # --------------------------------------------------------
    # Input for for replaying the game.
    # while loop is an error provision.
    # --------------------------------------------------------
    play_again = 3
    while play_again != 1 and play_again != 2:
        print("\nWould you like to play again?")
        print("\n1. Yes", "\n2. No\n")
        play_again = input().strip()
        if not play_again.isnumeric():
            print("ERROR: Please select either '1' or '2' as a valid response")
        # Statements for play_again input
        elif int(play_again) == 1:
            return True
        elif int(play_again) == 2:
            return False
        else:
            print("ERROR: Please select either '1' or '2' as a valid response")


if __name__ == "__main__":
    main()
