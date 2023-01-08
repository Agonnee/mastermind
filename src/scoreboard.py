import json
import pathlib
import os

from src.difficulty import Difficulty

class Scorekeeper:
    def __init__(self, save_path) -> None:
        self.save_location: pathlib.Path = save_path        
        self.scores: dict = self.load_scores()
        self.empty_scoresheet: dict = {}
        for i in Difficulty:
            self.empty_scoresheet[i.value] = 11


    def record_score(self, user: str, difficulty: str, num_of_turns: int) -> None:
        """Record the results of this round of Mastermind if better than the player's best score"""
        
        if (user in self.scores) and (num_of_turns < self.scores[user][difficulty]):
            self.scores[user][difficulty] = num_of_turns
        else:
            self.scores[user] = dict(self.empty_scoresheet)
            self.scores[user][difficulty] = num_of_turns

    def get_scores(self, difficulty: str) -> list[tuple]:
        """Provide the scoreboard information to be displayed"""

        scores_to_display = {}
        for key, value in self.scores.items():
            if value[difficulty] < 11:
                scores_to_display[key] = value[difficulty]
        sorted_scores = sorted(scores_to_display.items(), key=lambda x: x[1])
        return sorted_scores      
        

    def load_scores(self) -> dict:
        """Loads the saved scoreboard from file, or returns {} if no scores.json file found."""
        file_loc = os.path.join(self.save_location, "scores.json")
        if pathlib.Path(file_loc).exists():
            with open(file_loc, 'r') as f:
                data = json.load(f)
        else:
            data = {}
        return data

    def save_scores(self) -> None:
        """Saves the updated scoreboard from self.scores to file."""
        file_loc = os.path.join(self.save_location, "scores.json")
        with open(file_loc, 'w') as f:
            json.dump(self.scores, f)