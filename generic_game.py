from abc import ABC, abstractmethod
import random
from typing import Optional, Tuple
from game_config import GameConfig

class GenericGame(ABC):
    def __init__(self, game_config: GameConfig) -> None:
        self.guess_prompt: str = game_config.guess_prompt
        self._setup_prompt: str = game_config.setup_prompt
        self.msg_to_high:str  =  game_config.msg_to_high
        self.msg_to_low :str = game_config.msg_to_low
        self.user_input_type: type = game_config.user_input_type
    
    @abstractmethod
    def get_random_value(self):
        pass

    @abstractmethod
    def get_user_guess(self):
        pass
    
    @property
    def setup_prompt(self):
        return self._setup_prompt
    
    def setup_game(self):
        random_value = self.get_random_value()
        name: str = input("What is your name?")
        print(self.setup_prompt.format(name=name))
        return random_value
    
    def is_under_max_tries(self, max_tries: int, attempts: int) -> bool:
        if max_tries is None:
            return True
        return attempts < max_tries
        
    def determine_if_player_won(self, user_input: int, random_number: int, attempts:int) -> None:
        if user_input != random_number:
            print("You ran out of tries!")
        else:
            print(f"Congratulations! You guessed correctly in {attempts} tries.")
    
    def evaluate_guess(self, random_number: int, user_input: int) -> None:
        if user_input > random_number:
            print(self.msg_to_high)
        else:
            print(self.msg_to_low)
            
    def play_game(self, random_word:str , max_tries: int , attempts: int, user_input: int)-> Tuple[int, int]:
        while user_input != random_word and self.is_under_max_tries(max_tries, attempts):
            self.evaluate_guess(random_word, user_input)
            user_input = self.get_user_guess()
            attempts += 1
        return user_input, attempts
    
    def start_game(self, random_number: int, max_tries: Optional[int] = None ) -> None:
        attempts: int = 1
        user_input: int = self.get_user_guess()
        user_input, attempts = self.play_game(random_number, max_tries, attempts, user_input)
        self.determine_if_player_won(user_input, random_number, attempts)

