from dataclasses import dataclass

from src.api_handler import API_Handler
from src.ui import UI


@dataclass
class GameController:
    api_handler: API_Handler
    ui: UI

    def play_game(self) -> bool:
        """Handles Ordering Game controller functions"""

        answer = self.game_start()
        username = self.ui.pick_player_name()
        game_won = False
        for i in range(10):
            game_won = self.turn(i + 1, answer)
            if game_won:
                self.ui.display_win(answer, username, i + 1)
                break

        if not game_won:
            self.ui.display_loss(answer, username)

        replay = self.ui.prompt_play_again()
        return replay

    def game_start(self) -> str:
        """
        Uses the API Handler to generate code, and the UI to display the game rules.
        Returns the str "answer" which is the secret code for the game.
        """
        self.ui.display_rules()
        answer = self.api_handler.get_code()
        return answer

    def turn(self, guess_number: int, answer: str) -> bool:
        """
        Utilizes the UI to organize a single guessing round in the game.
        Returns bool of whether the game has been won or not
        """

        answer_len = len(answer)
        guess = self.ui.guess_input(guess_number, answer_len)
        correct_right_loc, correct_wrong_loc = self.compare_guess_to_answer(
            guess, answer
        )
        if correct_right_loc == answer_len:
            return True
        self.ui.display_feedback(correct_right_loc, correct_wrong_loc)
        return False

    def compare_guess_to_answer(self, guess: str, answer: str) -> tuple[int, int]:
        """
        Compares the Player's Guess and the generated Answer to provide the feedback to the player.
        Returns a tuple of the guess information (correct_right_location, correct_wrong_location)
        """

        correct_right_location = 0
        correct_wrong_location = 0
        dummy_guess = [x for x in guess]
        dummy_answer = [x for x in answer]
        for i in range(len(guess)):
            if dummy_answer[i] == dummy_guess[i]:
                correct_right_location += 1
                dummy_guess[i], dummy_answer[i] = "", ""
        for i in range(len(guess)):
            if dummy_guess[i] and (dummy_guess[i] in dummy_answer):
                dummy_answer[dummy_answer.index(dummy_guess[i])] = ""
                correct_wrong_location += 1

        return correct_right_location, correct_wrong_location
