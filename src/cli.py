class Cli:
    """Implementing the UI Protocol to create simple CLI"""

    def display_rules(self) -> None:
        """Print the Games rules at the beginning of the game"""

        print("================================================")
        print("Welcome to Mastermind!")
        print("You are tasked with cracking the secret code!")
        print("The code consists of 4 digits, between 0 and 7")
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

        print("================================================")
        print("Guess Feedback:")
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

        play_again = input(f"Would you like to play again? (Y/n) ")
        if play_again.lower() in ["y", "yeah", "yes"]:
            return True
        else:
            return False