from src.api_handler import API_Handler
from src.cli import Cli
from src.gamecontroller import GameController
from src.scoreboard import Scorekeeper

def main():
    ui = Cli()
    mastermind = GameController(API_Handler(), ui, Scorekeeper('.\data'))
    replay = True
    while replay:
        replay = mastermind.play_game()
        

if __name__ == "__main__":
    main()