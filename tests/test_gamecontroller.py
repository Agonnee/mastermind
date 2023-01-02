from src.api_handler import API_Handler
from src.cli import Cli
from src.gamecontroller import GameController
from pytest import MonkeyPatch

import requests_mock
import pytest


def test_game_start() -> None:
    controller = GameController(API_Handler(), Cli())

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    body_text = "0\n0\n0\n1\n\n"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, status_code=200, text=body_text)
        answer = controller.game_start()

    assert answer == "0001"


def test_play_game_win(monkeypatch: MonkeyPatch) -> None:
    input_value = "9999"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler(), Cli())

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    body_text = "9\n9\n9\n9\n\n"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, status_code=200, text=body_text)
        controller.play_game()

def test_play_game_lose(monkeypatch: MonkeyPatch) -> None:
    input_value = "4334"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler(), Cli())

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    body_text = "3\n4\n4\n3\n\n"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, status_code=200, text=body_text)
        controller.play_game()

def test_turn_match(monkeypatch: MonkeyPatch) -> None:
    input_value = "0000"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler(), Cli())
    assert controller.turn(1, "0000") == True


def test_turn_wrong(monkeypatch: MonkeyPatch) -> None:
    input_value = "0000"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler(), Cli())
    assert controller.turn(1, "0001") == False


@pytest.mark.parametrize(
    "guess_input, answer_input, cor_right_loc, cor_wrong_loc",
    [
        ("0000", "1111", 0, 0),
        ("0001", "1111", 1, 0),
        ("0021", "2111", 1, 1),
        ("3021", "2131", 1, 2),
        ("3021", "3210", 1, 3),
        ("0011", "1111", 2, 0),
        ("2011", "1211", 2, 1),
        ("2011", "0211", 2, 2),
        ("0111", "1111", 3, 0),
        ("1111", "1111", 4, 0),
        ("1110", "1111", 3, 0),
        ("1100", "1111", 2, 0),
        ("1000", "1111", 1, 0),
        ("0001", "1110", 0, 2),
        ("0011", "1100", 0, 4),
        ("1234", "4321", 0, 4),
        ("1234", "5423", 0, 3),
        ("1234", "6543", 0, 2),
        ("1235", "7654", 0, 1),

    ],
)
def test_compare_guess_to_answer(
    guess_input, answer_input, cor_right_loc, cor_wrong_loc
):
    controller = GameController(API_Handler(), Cli())
    a, b = controller.compare_guess_to_answer(guess_input, answer_input)
    assert (a, b) == (cor_right_loc, cor_wrong_loc)
