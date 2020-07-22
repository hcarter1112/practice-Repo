import random


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

    print("Welcome to Harold's Bible Order Tester, 'H-BOT'!")
    print("In this game your knowledge of the order of Bible books will be tested.")
    print(
        "You can input how many questions you would like to go through before you get your scorecard."
    )
    print("From there you will be able to select to play the game again.")

    keepGoing = True
    repeat = True
    number_correct = 0
    while repeat:
        while keepGoing:
            print("\nHow many questions would you like? ")
            num_questions = int(input())
            keepGoing = Game(num_questions, bible_Books, number_correct)


def Game(
    num_questions, bible_Books, number_correct
):  # this is where the questions will be generated

    number_left = num_questions
    q_exceptions = []
    for questions in list(range(num_questions)):
        random_bit = random.getrandbits(1)
        random_boolean = bool(random_bit)
        book_exceptions = []
        ans_exceptions = []
        if random_boolean == True:
            random_boolean = "before"
        else:
            random_boolean = "after"
        random_book = random.randrange(2, 66, 1)
        while random_book in q_exceptions:
            random_book = random.randrange(2, 66, 1)
        if random_book not in q_exceptions:
            q_exceptions.append(random_book)
        print(
            "What book of the Bible comes "
            + random_boolean
            + " "
            + bible_Books[random_book]
            + "?"
        )

        mult_letters = [1, 2, 3, 4]
        mult_letters_index = 0
        for items in mult_letters:
            before_random_book = random_book - 1
            after_random_book = random_book + 1
            answer_randomizer = random.randrange(101, 105, 1)
            random_ans = random.randrange(2, 66, 1)
            while answer_randomizer in book_exceptions:
                answer_randomizer = random.randrange(101, 105, 1)
            if answer_randomizer not in book_exceptions:
                book_exceptions.append(answer_randomizer)

            while random_ans in ans_exceptions:
                random_ans = random.randrange(1, 66, 1)
            if random_ans not in ans_exceptions:
                ans_exceptions.append(random_ans)
            ans_exceptions.append(random_book)

            if answer_randomizer == 101 and random_boolean == "after":
                correct_answer = mult_letters_index + 1
                ans_exceptions.append(after_random_book)
                print(
                    str(mult_letters[mult_letters_index])
                    + ". "
                    + str(bible_Books[after_random_book])
                )
                mult_letters_index += 1
            elif answer_randomizer == 102 and random_boolean == "before":
                correct_answer = mult_letters_index + 1
                ans_exceptions.append(after_random_book)
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
                mult_letters_index += 1

        ans = int(input("\nYour answer? "))
        if ans == correct_answer:
            print("\nCorrect!")
            number_correct += 1

        else:
            print("\nIncorrect :,(")

        if number_left == 2:
            number_left -= 1
            print("Only " + str(number_left) + " question left...")
            print("-" * 80)

        elif number_left == 4 or number_left == 3:
            number_left -= 1
            print(
                "THE FINAL COUNTDOOOWWWN!! " + str(number_left) + " questions left..."
            )
            print("-" * 80)

        elif number_left == 0:
            break

        else:
            number_left -= 1
            print("You have " + str(number_left) + " left...")
            print("-" * 80)
    percent = number_correct / num_questions
    percent *= 100

    if percent == 100:
        print(
            "Congratulations bible scholar! You got an 'A+' at "
            + str(int(percent))
            + "%. WOOT!"
        )
    elif percent >= 90 and percent < 100:
        print("You got an 'A' at " + str(int(percent)) + "%. Awesome work!")
    elif percent >= 80 and percent < 90:
        print("You got an 'B' at " + str(int(percent)) + "%. Good job!")
    elif percent >= 70 and percent < 80:
        print("You got an 'C' at " + str(int(percent)) + "%. Well... You passed =)!")
    elif percent >= 60 and percent < 70:
        print("You got an 'D' at " + str(int(percent)) + "%. Ouch!")
    else:
        print(
            "You got an 'F' at "
            + str(int(percent))
            + "%. JW.ORG has a free copy of the bible for you to study from!"
        )

    print("\nWould you like to play again?")
    print("\n1. Yes", "\n2. No\n")

    play_again = int(input())

    if play_again == 1:
        return True
    if play_again == 2:
        return False


if __name__ == "__main__":
    main()
