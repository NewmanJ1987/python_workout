import random
from typing import Optional, Tuple
words = [
    "cat", "dog", "ant", "bat", "owl",
    "frog", "fish", "bear", "lion", "wolf",
    "shark", "crane", "snake", "whale", "horse",
    "tree", "bush", "fern", "rock", "moss",
    "sand", "dust", "snow", "rain", "wind",
    "star", "moon", "fire", "lava", "wave"
]

guess_word_prompt: str = "Please guess a word between of length 3 and 5 characters: "

def setup_game() -> str:
    random_word: str = random.choice(words)
    name: str = input("What is your name? ")
    print(f"Hello, {name}! I'm thinking of a word between 3 and 5 characters long.")
    return random_word

def start_game(random_word: str, max_tries: Optional[int] = None ) -> None:
    attempts: int = 1
    user_input: str = input(guess_word_prompt)
    user_input, attempts = play_game(random_word, max_tries, attempts, user_input)
    determine_if_player_won(user_input, random_word, attempts)

def play_game(random_word:str , max_tries: int , attempts: int, user_input: int)-> Tuple[int, int]:
    while user_input != random_word and is_under_max_tries(max_tries, attempts):
        evaluate_guess(random_word, user_input)
        user_input: str = input(guess_word_prompt)
        attempts += 1
    return user_input, attempts

def evaluate_guess(random_word: str, user_input: str) -> None:
    if user_input > random_word:
        print("The word is alphabetically before the word I'm thinking of.")
    else:
        print("The word is alphabetically after the word I'm thinking of.")

def determine_if_player_won(user_input: int, random_number: int, attempts:int) -> None:
    if user_input != random_number:
        print("You ran out of tries!")
    else:
        print(f"Congratulations! You guessed the word in {attempts} tries.")
        
def is_under_max_tries(max_tries: int, attempts: int) -> bool:
    if max_tries is None:
        return True
    return attempts < max_tries

def main() -> None:
    random_word: str = setup_game()
    start_game(random_word,  3) 
    


if __name__ == "__main__":
    main()