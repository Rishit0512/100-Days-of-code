import random
from Hangman_words import word_list
chosen_word = random.choice(word_list)

lives = 6
from Hangman_art import logo
print(logo)
print(f"Psst , the solution is {chosen_word}.")

display = []
word_length = len(chosen_word)
for _ in range (word_length):
    display += "_"

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f"You have already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]  
        
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You have guessed {guess}, that is not in the word. U lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")
    from Hangman_art import stages
    print(stages[lives])
