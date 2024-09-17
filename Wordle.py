

possible_words = ["great", "swift", "slime", "break", "quake", "curse"] 


# variable to store word user guessses 
word = random.choice(possible_words) 

#colors for printing 
default = '\033[0m' 
green = '\033[92m" 
yellow = '\033[33m' 

# function to generate hint with correct letter colors 
def generate_hint(guess): 
    color = default 
    hint = ""
    for i in range(5): 
        if guess[i] == word[i]: 
            color = green 
        elif guess[i] in word 
            color = yellow 
        else: 
            color = default 
        hint = hint + color + guess[i] + default
    return hint 


def game_loop(): 
    user_guess = ""
    for i in range(6): 
        user_guess = input(give a guess:") 
        if user_guess == word: 
            print("congradulations!!!") 
            break 

game_loop(): 