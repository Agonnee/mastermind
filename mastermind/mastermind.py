from api_handler import API_Handler
from gamecontroller import GameController

def main():
    mastermind = GameController(API_Handler())
    mastermind.play_game()
    mastermind.prompt_play_again()

if __name__ == "__main__":
    main()