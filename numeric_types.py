
import random

guess_number_prompt: str = "Please enter a number between 1 and 100: "

def setup_game() -> int:
        random_number: int = random.randint(1, 100)
        name: str = input("What is your name? ")
        print(f"Hello, {name}! I'm thinking of a number between 1 and 100.")
        return random_number
        
def start_game(random_number: int, max_tries=None) -> None:
    attempts: int = 1
    user_input: int = int(input(guess_number_prompt))
    user_input: int = play_game(random_number, max_tries, attempts, user_input)
    determine_if_player_won(user_input, random_number, attempts)

def play_game(random_number, max_tries, attempts, user_input)-> int:
    while user_input != random_number and is_under_max_tries(max_tries, attempts):
        evaluate_guess(random_number, user_input)
        user_input: int = int(input(guess_number_prompt))
        attempts += 1
    return user_input

def evaluate_guess(random_number, user_input):
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
    start_game(random_number, 3) 
    


if __name__ == "__main__":
    main()

    