import argparse

from src.api_handler import API_Handler
from src.cli import Cli
from src.pig_latin_cli import pl_Cli
from src.gamecontroller import GameController
from src.scoreboard import Scorekeeper

def main():
    
    parser = argparse.ArgumentParser(description='Choose the UI to use:')
    parser.add_argument('--piglatin', '-p', action='store_true', help='Select the Pig Latin UI.')
    args = parser.parse_args()
    if args.piglatin:
        ui = pl_Cli()
    else:
        ui = Cli()

    mastermind = GameController(API_Handler(), ui, Scorekeeper('.\data'))
    replay = True
    while replay:
        replay = mastermind.play_game()
        

if __name__ == "__main__":
    main()