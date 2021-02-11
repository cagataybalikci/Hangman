import random
import art
import words


print(art.logo)

lives = 6
stages = art.stages
display = []
chosen_word = random.choice(words.placeholder_words)
is_game_ended = False


word_length = len(chosen_word)

for letter in range(word_length):
    display += "_"

print(chosen_word)

prev_guess = ""

while not is_game_ended:

    guess = input("Make your guess: ").lower()

    if guess == prev_guess:
        print("You've already enter that letter...")
    else:
        prev_guess = guess

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"{guess} is not in the word :( ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(" ".join(display))

    if "_" not in display:
        print(f"Word was {chosen_word}, And you are win....")
        is_game_ended = True
            
    print(stages[lives])
            





