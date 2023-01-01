from dataclasses import dataclass

from src.api_handler import API_Handler

@dataclass
class GameController():
    api_handler: API_Handler

    def play_game(self):
        
        answer, username = self.game_start()
        print(answer) #debugging only
        for i in range(10):
            game_over = False
            game_over = self.turn(i+1, answer)
            if game_over:
                break

        play_again = input(f'Would you like to play again? (Y/n) ')
        if play_again.lower() in ["y", "yeah", "yes"]:
            return True
        else:
            return False

    def game_start(self):
        print("Welcome to Mastermind! \nYou are tasked with cracking the secret code!")
        print("Be warned, you only have 10 guesses")

        answer = self.api_handler.get_code()
        username = input("Enter your name: ")
        return answer, username

    def turn(self, guess_number, answer):
        answer_len = len(answer)
        guess = self.obtain_guess(guess_number, answer_len)
        correct_right_loc, correct_wrong_loc = self.compare_guess_to_answer(guess, answer)
        if correct_right_loc == answer_len:
            return True
        print(f"Nice Try, You got {correct_right_loc} right in the correct location and {correct_wrong_loc} right in the wrong location.")
        return False

    def obtain_guess(self, guess_number, answer_len):
        guess_valid = False
        while not guess_valid:
            guess = input(f"Enter guess number {guess_number}: ")
            if len(guess) == answer_len and guess.isnumeric():
                guess_valid = True
            else:
                print(f"Please enter a valid {answer_len} digit number")
        return guess
        

    def compare_guess_to_answer(self, guess, answer):
        correct_right_location = 0
        correct_wrong_location = 0
        dummy_guess = [x for x in guess]
        dummy_answer = [x for x in answer]
        for i in range(len(guess)):
            if dummy_answer[i] == dummy_guess[i]:
                correct_right_location += 1
                dummy_guess[i], dummy_answer[i] = "", ""
        for i in range(len(guess)):
            if dummy_guess[i] and dummy_guess[i] in dummy_answer:
                dummy_answer[dummy_answer.index(dummy_guess[i])] = ""
                correct_wrong_location += 1
        
        return correct_right_location, correct_wrong_location