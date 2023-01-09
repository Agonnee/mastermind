from src.difficulty import Difficulty


class Cli:
    """Implementing the UI Protocol to create simple CLI"""

    def display_menu(self) -> str:
        """Prompt the Player for Menu Options: Play, Scoreboard, Exit"""
        menu_options = ["Play Game", "Scoreboard", "Exit"]

        print("\n")
        print("Mastermind")
        print("================================================")
        print("Main Menu:")
        for count, i in enumerate(menu_options, 1):
            print(f"{count}. {i}")
        print("================================================")
        while True:
            try:
                choice = int(input("Enter selection. (1-3): "))
                if 0 < choice < len(menu_options) + 1:
                    return choice
                else:
                    print("Please choose a valid selection.")
            except ValueError:
                print("Please choose a valid selection.")

    def choose_difficulty(self, game_display=False) -> Difficulty:
        """
        Prompt the Player for a difficulty setting for the game.
        Returns a Difficulty obj from the difficulty enum
        """

        print("\n")
        print("Difficulty selection:")
        print("================================================")
        if game_display:
            for count, i in enumerate(Difficulty, 1):
                print(
                    f"{count}. {i.value}, {i.code_length} digit code with digits ranging 0-{i.digit_max}"
                )
        else:
            for count, i in enumerate(Difficulty, 1):
                print(f"{count}. {i.value}")
        print("================================================")
        while True:
            try:
                choice = int(input("Enter a difficulty setting. (1-4): "))
                if 0 < choice < len(Difficulty) + 1:
                    return list(Difficulty)[choice - 1]
            except ValueError:
                print("Please choose a valid difficulty.")

    def display_rules(self) -> None:
        """Print the Games rules at the beginning of the game"""

        print("\n")
        print("================================================")
        print("Welcome to Mastermind!")
        print("You are tasked with cracking the secret code!")
        print("Note, there may be duplicate numbers in the code.")
        print("After each guess, you'll receive feedback on your guess")
        print("Using the feedback, figure out the secret code!")
        print("Be warned, you only have 10 guesses...")
        print("================================================")
        print("\n")

    def display_loss(self, answer, username) -> None:
        """Display 'You Lose' message"""

        print("\n")
        print("================================================")
        print("Unfortunately, You did not successfully crack the code.")
        print(f"For your information, the code was {answer}.")
        print(f"Maybe You'll have better luck next time {username}.")
        print("================================================")
        print("\n")

    def display_win(self, answer, username, guess_number) -> None:
        """Display 'You Win' message"""

        print("\n")
        print("================================================")
        print(f"Congratulations {username}, You cracked the code!")
        print(f"You were able to guess {answer} in only {guess_number} tries!")
        print(f"Maybe you should try to see if you can beat that score.")
        print("================================================")
        print("\n")

    def display_feedback(self, correct_right_loc: int, correct_wrong_loc: int) -> None:
        """Display the feedback clues from the guess/answer comparison to the player."""

        print("\n")
        print("Guess Feedback:")
        print("================================================")
        print(
            f"You guessed {correct_right_loc} digits correctly in the right location."
        )
        print(
            f"You guessed {correct_wrong_loc} digits correctly in the wrong location."
        )
        print("================================================")
        print("\n")

    def pick_player_name(self) -> str:
        """Prompt player for input to set username"""

        username = input("Enter your name: ")
        return username

    def guess_input(self, guess_number: int, answer_len: int) -> str:
        """Prompt player for input to guess code."""

        guess_valid = False
        while not guess_valid:
            guess = input(f"Enter guess number {guess_number}: ")
            if len(guess) == answer_len and guess.isnumeric():
                guess_valid = True
            else:
                print(f"Please enter a valid {answer_len} digit number")
        return guess

    def prompt_play_again(self) -> bool:
        """Prompt Player for whether they'd like to play again or not"""

        play_again = input(f"Would you like to play again? (y/N) ")
        if play_again.lower() in ["y", "yeah", "yes"]:
            return True
        else:
            return False

    def prompt_for_scoreboard(self) -> bool:
        """Prompt Player for whether they'd like to view the scoreboard or not"""

        view_scores = input(f"Would you like to view the Scoreboard? (y/N) ")
        if view_scores.lower() in ["y", "yeah", "yes"]:
            return True
        else:
            return False

    def display_scores(self, scores: list[tuple], difficulty_name) -> None:
        """Display scores provided from the scoreboard"""

        print("\n")
        print(f"Best Scores: {difficulty_name}")
        print("================================================")
        for count, i in enumerate(scores[:5], 1):
            print(f"{count}. {i[0]}: {i[1]}")
        print("================================================")
        _ = input("Press Enter to Continue.")
