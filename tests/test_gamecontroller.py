from src.api_handler import API_Handler
from src.gamecontroller import GameController
from pytest import MonkeyPatch

import pytest

def test_game_start(monkeypatch: MonkeyPatch) -> None:
    input_name = 'Test_Name'
    monkeypatch.setattr("builtins.input", lambda _: input_name)
    controller = GameController(API_Handler())
    _, user_name = controller.game_start()
    assert user_name == "Test_Name"

def test_play_game(monkeypatch: MonkeyPatch) -> None:
    input_value = "9999"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler())
    controller.play_game()

def test_turn_match(monkeypatch: MonkeyPatch) -> None:
    input_value = "0000"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler())
    assert controller.turn(1, "0000") == True

def test_turn_wrong(monkeypatch: MonkeyPatch) -> None:
    input_value = "0000"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler())
    assert controller.turn(1, "0001") == False

def test_obtain_guess(monkeypatch: MonkeyPatch) -> None:
    input_value = "9999"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler())
    assert controller.obtain_guess(1, 4) == "9999"

@pytest.mark.parametrize(
    "guess_input, answer_input, cor_right_loc, cor_wrong_loc",
    [
        ("0000","1111",0,0),
        ("0001","1111",1,0),
        ("0011","1111",2,0),
        ("0111","1111",3,0),
        ("1111","1111",4,0),
        ("1110","1111",3,0),
        ("1100","1111",2,0),
        ("1000","1111",1,0)
    ]
)
def test_compare_guess_to_answer(guess_input, answer_input, cor_right_loc, cor_wrong_loc):
    controller = GameController(API_Handler())
    a,b = controller.compare_guess_to_answer(guess_input, answer_input) 
    assert (a,b) == (cor_right_loc, cor_wrong_loc)