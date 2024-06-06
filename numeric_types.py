import random
from generic_game import GenericGame
class NumericGame(GenericGame):
    def __init__(self, guess_prompt, setup_prompt, msg_to_high, msg_to_low, user_input_type) -> None:
        super().__init__(guess_prompt, setup_prompt, msg_to_high, msg_to_low, user_input_type)
        self.random_base: int = random.randint(2,16)
    
    
    @property
    def setup_prompt(self):
        return self._setup_prompt.format('{name}', self.random_base)
    
    def get_random_value(self) -> int:
        return random.randint(1, 100)
    
    def get_user_guess(self) ->int:
        return int (input(self.guess_prompt), base=self.random_base)
    
    
    
def main() -> None:
    numeric_game = NumericGame(
        guess_prompt="Please enter a number between 1 and 100: ",
        setup_prompt="Hello, {}! I'm thinking of a number between 1 and 100. Enter the number in base {}.",
        msg_to_high="Too high",
        msg_to_low="Too low",
        user_input_type=int)
    numeric_game.random_base = 10
    random_number: int = numeric_game.setup_game()
    numeric_game.start_game(random_number,  3) 
    

if __name__ == "__main__":
    main()