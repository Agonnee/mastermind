from src.difficulty import Difficulty


class pl_Cli:
    """Example of implementation of another UI instead of the standard CLI based on the UI Protocol"""

    def choose_difficulty(self) -> Difficulty:
        """
        Prompt the Player for a difficulty setting for the game.
        Returns a Difficulty obj from the difficulty enum
        """
        print("Ifficultyday Electionsay:")
        for count, i in enumerate(Difficulty, 1):
            print(
                f"{count}. {i.pl_name}, {i.code_length} igitday odecay ithway igitsday angingray 0-{i.digit_max}"
            )
        while True:
            try:
                choice = int(input("Enteryay ayay ifficultyday ettingsay. (1-4): "))
                if 0 < choice < len(Difficulty) + 1:
                    return list(Difficulty)[choice - 1]
            except ValueError:
                print("Easeplay oosechay ayay alidvay ifficultyday.")

    def display_rules(self) -> None:
        """Print the Games rules at the beginning of the game"""

        print("================================================")
        print("Elcomeway otay Astermindmay!")
        print("Ouyay areyay askedtay ithway ackingcray ethay ecretsay odecay!")
        print("Otenay , erethay aymay ebay uplicateday umbersnay inyay ethay odecay.")
        print("Afteryay eachyay uessgay , ou'llyay eceiveray eedbackfay onyay ouryay uessgay")
        print("Usingyay ethay eedbackfay , igurefay outyay ethay ecretsay odecay!")
        print("Ebay arnedway , ouyay onlyyay avehay 10 uessesgay...")
        print("================================================")
        print("\n")

    def display_loss(self, answer, username) -> None:
        """Display 'You Lose' message"""

        print("\n")
        print("================================================")
        print("Unfortunatelyyay , ouyay idday otnay uccessfullysay ackcray ethay odecay.")
        print(f"Orfay ouryay informationyay , ethay odecay asway {answer}.")
        print(f"Aybemay ou'llyay avehay etterbay ucklay extnay imetay {username}.")
        print("================================================")
        print("\n")

    def display_win(self, answer, username, guess_number) -> None:
        """Display 'You Win' message"""

        print("\n")
        print("================================================")
        print(f"Ongratulationscay {username}, ouyay ackedcray ethay odecay!")
        print(f"Ouyay ereway ableyay otay uessgay {answer} inyay onlyyay {guess_number} iestray!")
        print(f"Aybemay ouyay ouldshay ytray otay eesay ifyay ouyay ancay eatbay atthay orescay.")
        print("================================================")
        print("\n")

    def display_feedback(self, correct_right_loc: int, correct_wrong_loc: int) -> None:
        """Display the feedback clues from the guess/answer comparison to the player."""

        print("================================================")
        print("Uessgay Eedbackfay:")
        print(
            f"Ouyay uessedgay {correct_right_loc} igitsday orrectlycay inyay ethay ightray ocationlay."
        )
        print(
            f"Ouyay uessedgay {correct_wrong_loc} igitsday orrectlycay inyay ethay ongwray ocationlay."
        )
        print("================================================")
        print("\n")

    def pick_player_name(self) -> str:
        """Prompt player for input to set username"""

        username = input("Enteryay ouryay amenay (otnay inyay igpay atinlay): ")
        return username

    def guess_input(self, guess_number: int, answer_len: int) -> str:
        """Prompt player for input to guess code."""

        guess_valid = False
        while not guess_valid:
            guess = input(f"Enteryay uessgay umbernay {guess_number}: ")
            if len(guess) == answer_len and guess.isnumeric():
                guess_valid = True
            else:
                print(f"Easeplay enteryay ayay alidvay {answer_len} igitday umbernay")
        return guess

    def prompt_play_again(self) -> bool:
        """Prompt Player for whether they'd like to play again or not"""

        play_again = input(f"Ouldway ouyay ikelay otay ayplay againyay? (y/N) ")
        if play_again.lower() in ["y", "yeah", "yes", "esyay", "eahyay"]:
            return True
        else:
            return False

    def prompt_for_scoreboard(self) -> bool:
        """Prompt Player for whether they'd like to view the scoreboard or not"""
        
        view_scores = input(f"Ouldway ouyay ikelay otay iewvay ethay oreboardscay? (y/N) ")
        if view_scores.lower() in ["y", "yeah", "yes", "esyay", "eahyay"]:
            return True
        else:
            return False

    def display_scores(self, scores:list[tuple], difficulty_name) -> None:
        """Display scores provided from the scoreboard"""

        print("================================================")
        print(f"Estbay Oresscay: {difficulty_name}")
        for count, i in enumerate(scores[:5], 1):
            print(f"{count}. {i[0]}: {i[1]}")
        print("================================================")