word = "great"

#colors for printing 
default = '\033[0m' 
green = '\033[92m" 
yellow = '\033[33m' 

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