import random
from typing import Optional, Tuple
from generic_game import GenericGame

class StringGuessingGame(GenericGame):
    
    def __init__(self, guess_prompt, setup_prompt, msg_to_high, msg_to_low, user_input_type, words) -> None:
        super().__init__(guess_prompt, setup_prompt, msg_to_high, msg_to_low, user_input_type)
        self.words = words
    
    def get_random_value(self) -> str:
        return random.choice(self.words)
    
    def get_user_guess(self) -> str:
        return input(self.guess_prompt)

def main() -> None:
    words = [
    "cat", "dog", "ant", "bat", "owl",
    "frog", "fish", "bear", "lion", "wolf",
    "shark", "crane", "snake", "whale", "horse",
    "tree", "bush", "fern", "rock", "moss",
    "sand", "dust", "snow", "rain", "wind",
    "star", "moon", "fire", "lava", "wave"
]
    string_game = StringGuessingGame(
        guess_prompt="Please guess a word between of length 3 and 5 characters: ",
        setup_prompt="What is your name? Hello, {name}! I'm thinking of a word between 3 and 5 characters long.",
        msg_to_high="The word is alphabetically before the word I'm thinking of.",
        msg_to_low="The word is alphabetically after the word I'm thinking of.",
        user_input_type=str,
        words=words)
    random_word: str = string_game.setup_game()
    string_game.start_game(random_word,  3)    
    

if __name__ == "__main__":
    main()