from src.api_handler import API_Handler
from src.cli import Cli
from src.scoreboard import Scorekeeper
from src.gamecontroller import GameController
from pytest import MonkeyPatch

import requests_mock
import pytest

def test_main_menu(monkeypatch: MonkeyPatch, tmp_path) -> None:
    controller = GameController(API_Handler(), Cli(), Scorekeeper(save_path=tmp_path))
    input_values = ["1", ""]
    selections_list = [1, 2, 3]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    monkeypatch.setattr(Cli, "display_menu", lambda _: selections_list.pop(0))
    monkeypatch.setattr(GameController, "play_game", lambda _: False)
    controller.main_menu()
    controller.main_menu()
    with pytest.raises(SystemExit):
        controller.main_menu()



def test_game_start(monkeypatch: MonkeyPatch, tmp_path) -> None:
    controller = GameController(API_Handler(), Cli(), Scorekeeper(save_path=tmp_path))

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    body_text = "0\n0\n0\n1\n\n"

    input_values = ["1", "1", "Test_Name"]
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, status_code=200, text=body_text)
        answer, _ = controller.game_start()

    assert answer == "0001"


def test_play_game_win(monkeypatch: MonkeyPatch, tmp_path) -> None:

    input_values = ["1", "1", "Test_Name", "9999", "n", "n"]
    test_answer = "9999"
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    monkeypatch.setattr(API_Handler, "get_code", lambda _, __, ___: test_answer)

    controller = GameController(API_Handler(), Cli(), Scorekeeper(save_path=tmp_path))
    controller.play_game()


def test_play_game_lose(monkeypatch: MonkeyPatch, tmp_path) -> None:
    input_values = [
        "1",
        "1",
        "Test_Name",
        "9998",
        "9998",
        "9998",
        "9998",
        "9998",
        "9998",
        "9998",
        "9998",
        "9998",
        "9998",
        "y",
        "",
        "n",
    ]
    test_answer = "9999"
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))
    monkeypatch.setattr(API_Handler, "get_code", lambda _, __, ___: test_answer)

    controller = GameController(API_Handler(), Cli(), Scorekeeper(save_path=tmp_path))
    controller.play_game()


def test_turn_match(monkeypatch: MonkeyPatch, tmp_path) -> None:
    input_value = "0000"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler(), Cli(), Scorekeeper(save_path=tmp_path))
    assert controller.turn(1, "0000") == True


def test_turn_wrong(monkeypatch: MonkeyPatch, tmp_path) -> None:
    input_value = "0000"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    controller = GameController(API_Handler(), Cli(), Scorekeeper(save_path=tmp_path))
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
    guess_input, answer_input, cor_right_loc, cor_wrong_loc, tmp_path
):
    controller = GameController(API_Handler(), Cli(), Scorekeeper(save_path=tmp_path))
    a, b = controller.compare_guess_to_answer(guess_input, answer_input)
    assert (a, b) == (cor_right_loc, cor_wrong_loc)
