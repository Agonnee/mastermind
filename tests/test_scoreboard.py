import os
import pathlib
from src.scoreboard import Scorekeeper

def test_Scorekeeper_no_load(tmp_path):
    test_scorekeeper = Scorekeeper(save_path = tmp_path)
    assert test_scorekeeper.scores == {}

def test_record_score_first(tmp_path):
    test_scorekeeper = Scorekeeper(save_path = tmp_path)
    test_scorekeeper.record_score("test_name", "Easy", 6)
    assert test_scorekeeper.scores["test_name"]["Easy"] == 6

def test_record_score_new(tmp_path):
    test_scorekeeper = Scorekeeper(save_path = tmp_path)
    test_scorekeeper.record_score("test_name", "Easy", 8)
    test_scorekeeper.record_score("test_name", "Easy", 7)
    assert test_scorekeeper.scores["test_name"]["Easy"] == 7

def test_get_scores(tmp_path):
    test_scorekeeper = Scorekeeper(save_path = tmp_path)
    test_scorekeeper.record_score("name1", "Easy", 1)
    test_scorekeeper.record_score("name3", "Easy", 3)
    test_scorekeeper.record_score("name2", "Easy", 2)
    test_scorekeeper.record_score("name4", "Easy", 4)
    score_list = test_scorekeeper.get_scores("Easy")
    assert score_list[0] == ("name1", 1)
    assert score_list[1] == ("name2", 2)
    assert score_list[2] == ("name3", 3)
    assert score_list[3] == ("name4", 4)

def test_load_scores(tmp_path):
    pass

def test_save_scores(tmp_path):
    test_scorekeeper = Scorekeeper(save_path = tmp_path)
    test_scorekeeper.record_score("name3", "Easy", 2)
    test_scorekeeper.save_scores()
    save_file = os.path.join(tmp_path, "scores.json")
    with open(save_file, "r") as f:
        content = f.read()
    assert content == '{"name3": {"Easy": 2, "Medium": 11, "Hard": 11, "Very Hard": 11}}'