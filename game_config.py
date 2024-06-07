class GameConfig:
    def __init__(self, guess_prompt, setup_prompt, msg_to_high, msg_to_low, user_input_type):
        self.guess_prompt = guess_prompt
        self.setup_prompt = setup_prompt
        self.msg_to_high = msg_to_high
        self.msg_to_low = msg_to_low
        self.user_input_type = user_input_type
        

string_game_config = GameConfig(
    guess_prompt="Please guess a word between of length 3 and 5 characters: ",
    setup_prompt="What is your name? Hello, {name}! I'm thinking of a word between 3 and 5 characters long.",
    msg_to_high="The word is alphabetically before the word I'm thinking of.",
    msg_to_low="The word is alphabetically after the word I'm thinking of.",
    user_input_type=str)

numeric_game_config = GameConfig(
    guess_prompt="Please enter a number between 1 and 100: ",
    setup_prompt="Hello, {}! I'm thinking of a number between 1 and 100. Enter the number in base {}.",
    msg_to_high="Too high",
    msg_to_low="Too low",
    user_input_type=int)

