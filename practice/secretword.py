
secret_word = "pie"
guess = ''
guess_count = 0
guess_limit = 4
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter guess: ')
        guess_count += 1
    elif guess_count != guess_limit:
        print('Try again FOOO!')
    else:
        out_of_guesses = True 
if out_of_guesses:
    print('Out of guesses, YOU SUCK!')
else:
    print("You win!")
