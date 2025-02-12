# main.py
# Colton Ramsey
# ramseyc6@mail.uc.edu

import random

def sports_word():
    """
    randomly selects a word from the predetermined list of sports words
    @return string: sports word that is selected
    """
    word_list = [
        "game", "team", "player", "win", "lose", "score", "goal", "points", "match",
        "season", "ball", "sport", "play", "time", "coach", "league", "champion",
        "final", "competition", "victory"]
    chosen_word = random.choice(word_list).lower()
    return chosen_word

def food_word():
    """
    randomly selects a word from the predetermined list of food words
    @return string: food word that is selected
    """
    word_list = [
        "Chicken", "knife", "fork", "apple", "orange", "grape", "strawberry", 
        "raspberry", "juice", "beer", "beef", "steak", "turkey"]
    chosen_word = random.choice(word_list).lower()
    return chosen_word

def gaming_word():
    """
    randomly selects a word from the predetermined list of gaming words
    @return string: gaming word that is selected
    """
    word_list = [
        "controller", "xbox", "playstation", "fortnite", "headset", "processor", 
        "graphics", "dekupomdomnem"]
    chosen_word = random.choice(word_list).lower()
    return chosen_word

def display_word(word, guessed_letters):
    """
    """
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
             displayed_word += letter
        else:
             displayed_word += "_"
    return displayed_word
    
def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():  # Check for single letter input
            return guess
        else:
            print("Invalid input. Please enter a single letter.")

def play_hangman():
    while True: # loop for difficulty selection
        difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            break # break the loop if valid difficulty is selected
        else:
            print("Invalid difficulty. Please choose easy, medium, or hard.")
    
    while True: # loop for category selection
        category = input("Choose category (sports, food, gaming): ").lower()
        if category in ["sports", "food", "gaming"]:
            break # break the loop if valid category is selected
        else:
            print("Invalid category. Please choose sports, food, or gaming.")

    # Logic to run the word selectors for the selected category
    if category == "sports":
        word = sports_word()
    elif category == "food":
        word = food_word()
    else:
        word = gaming_word()
        
    guessed_letters = set()

    if difficulty == "easy":
        tries = 9  # More tries for easy mode
    elif difficulty == "medium":
        tries = 6  # Standard number of tries
    else:  # hard
        tries = 4  # Fewer tries for hard mode

    print(f"Welcome to Hangman! You're playing the {category} category on {difficulty} mode with {tries} tries.") #f-string for dynamic difficulty

    while True:
        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

        if tries == 0:
            print("You ran out of tries. The word was:", word)
            break

        guess = get_guess()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print("Incorrect. You have", tries, "tries left.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()  # Recursive call to play again
    else:
        print("Thanks for playing!")