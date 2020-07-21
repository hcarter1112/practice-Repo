import random

def main():
    bible_Books = ['Genesis',
'Exodus',
'Leviticus',
'Numbers',
'Deuteronomy',
'Joshua',
'Judges',
'Ruth',
'1 Samuel',
'2 Samuel',
'1 Kings',
'2 Kings',
'1 Chronicles',
'2 Chronicles',
'Ezra',
'Nehemiah',
'Esther',
'Job',
'Psalms',
'Proverbs',
'Ecclesiastes',
'Song of Solomon',
'Isaiah',
'Jeremiah',
'Lamentations',
'Ezekiel',
'Daniel',
'Hosea',
'Joel',
'Amos',
'Obadiah',
'Jonah',
'Micah',
'Nahum',
'Habakkuk',
'Zephaniah',
'Haggai',
'Zechariah',
'Malachi',
'Matthew,'
'Mark',
'Luke',
'John',
'Acts',
'Romans',
'1 Corinthians',
'2 Corinthians',
'Galatians',
'Ephesians',
'Philippians',
'Colossians',
'1 Thessalonians',
'2 Thessalonians',
'1 Timothy',
'2 Timothy',
'Titus',
'Philemon',
'Hebrews',
'James',
'1 Peter',
'2 Peter',
'1 John',
'2 John',
'3 John',
'Jude',
'Revelation',
]

print("Welcome to Harold's Bible Order Tester, 'H-BOT'!")
print("In this game your knowledge of the order of Bible books will be tested.")
print("You can input how many questions you would like to go through before you get your scorecard.")
print("From there you will be able to select to play the game again.")

keepGoing = True
repeat = True
num_questions = 0
while repeat:
    while keepGoing:
        num_questions = int(input("How many questions would you like? "))
        keepGoing = Game(num_questions, bible_Books)

def Game(num_questions, bible_Books):#this is where the questions will be generated
    q_Num = 1
    for questions in list(range(num_questions)):
        random_bit = random.getrandbits(1)
        random_boolean = bool(random_bit)
        if random_boolean == True:
            random_boolean = 'before'
        else:
            random_boolean = 'after'
        random_book = random.randrange(1, 66, 1)
        print(str(q_Num) + ". What book of the Bible comes " + random_boolean + " " + bible_Books[random_book] + "?")
        q_Num += 1

def scorecard():#this will dispay after the game has completed and will give them a grade for their performance. This should also include the option to play again





if __name__ == "__main__":
    main()