from src.api_handler import API_Handler
from src.gamecontroller import GameController

def main():
    mastermind = GameController(API_Handler())
    replay = True
    while replay:
        replay = mastermind.play_game()

if __name__ == "__main__":
    main()