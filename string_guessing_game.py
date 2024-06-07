import random
from generic_game import GenericGame
from game_config import  string_game_config, GameConfig
from typing import List

class StringGuessingGame(GenericGame):
    
    def __init__(self, game_config: GameConfig, words: List[str]) -> None:
        super().__init__(game_config)
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
    string_game = StringGuessingGame(string_game_config,
        words=words)
    random_word: str = string_game.setup_game()
    string_game.start_game(random_word,  3)    
    

if __name__ == "__main__":
    main()