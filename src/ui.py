from typing import Protocol
from src.difficulty import Difficulty


class UI(Protocol):
    def display_menu(self) -> str:
        """Prompt the Player for Menu Options: Play, Scoreboard, Exit"""

        raise NotImplementedError()

    def choose_difficulty(self) -> Difficulty:
        """
        Prompt the Player for a difficulty setting for the game.
        Returns a Difficulty obj from the difficulty enum
        """

        raise NotImplementedError()

    def display_rules(self) -> None:
        """Display the Game rules upon start"""

        raise NotImplementedError()

    def display_loss(self, answer, username) -> None:
        """Display 'You Lose' message"""

        raise NotImplementedError()

    def display_win(self, answer, username, guess_number) -> None:
        """Display 'You Win' message"""

        raise NotImplementedError()

    def display_feedback(self, correct_right_loc: int, correct_wrong_loc: int) -> None:
        """Display the feedback clues from the guess/answer comparison to the player."""
        raise NotImplementedError()

    def pick_player_name(self) -> str:
        """Prompt player for input to set username,"""

        raise NotImplementedError()

    def guess_input(self, guess_number: int, answer_len: int) -> str:
        """Prompt player for input to guess code."""

        raise NotImplementedError()

    def prompt_play_again(self) -> bool:
        """Prompt player for whether they'd like to play again or not."""

        raise NotImplementedError()

    def prompt_for_scoreboard(self) -> bool:
        """Prompt Player for whether they'd like to view the scoreboard or not"""

        raise NotImplementedError()

    def display_scores(self, scores) -> None:
        """Display scores provided from the scoreboard"""

        raise NotImplementedError()
