
import random
from typing import Optional, Tuple
guess_number_prompt: str = "Please enter a number between 1 and 100: "
random_base: int = random.randint(2,16)


def setup_game() -> int:
    random_number: int = random.randint(1, 100)
    name: str = input("What is your name? ")
    print(f"Hello, {name}! I'm thinking of a number between 1 and 100. Enter the number in base {random_base}.")
    return random_number
    
        
def start_game(random_number: int, max_tries: Optional[int] = None ) -> None:
    attempts: int = 1
    user_input: int = int(input(guess_number_prompt), base=random_base)
    user_input, attempts = play_game(random_number, max_tries, attempts, user_input)
    determine_if_player_won(user_input, random_number, attempts)

def play_game(random_number:int , max_tries: int , attempts: int, user_input: int)-> Tuple[int, int]:
    while user_input != random_number and is_under_max_tries(max_tries, attempts):
        evaluate_guess(random_number, user_input)
        user_input: int = int(input(guess_number_prompt), base=random_base)
        attempts += 1
    return user_input, attempts

def evaluate_guess(random_number: int, user_input: int) -> None:
    if user_input > random_number:
        print("Too high")
    else:
        print("Too low")

def determine_if_player_won(user_input: int, random_number: int, attempts:int) -> None:
    if user_input != random_number:
        print("You ran out of tries!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} tries.")
        

def is_under_max_tries(max_tries: int, attempts: int) -> bool:
    if max_tries is None:
        return True
    return attempts < max_tries
    
    
def main() -> None:
    random_number: int = setup_game()
    start_game(random_number,  3) 
    


if __name__ == "__main__":
    main()

    