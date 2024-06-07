import random
from generic_game import GenericGame
from game_config import GameConfig, numeric_game_config

class NumericGame(GenericGame):
    def __init__(self, game_config: GameConfig) -> None:
        super().__init__(game_config)
        self.random_base: int = random.randint(2,16)
    
    
    @property
    def setup_prompt(self):
        return self._setup_prompt.format('{name}', self.random_base)
    
    def get_random_value(self) -> int:
        return random.randint(1, 100)
    
    def get_user_guess(self) ->int:
        return int (input(self.guess_prompt), base=self.random_base)
    
    
    
def main() -> None:
    numeric_game = NumericGame(numeric_game_config)
    random_number: int = numeric_game.setup_game()
    numeric_game.start_game(random_number,  3) 
    

if __name__ == "__main__":
    main()