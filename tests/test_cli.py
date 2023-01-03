from src.cli import Cli
from src.difficulty import Difficulty
from pytest import MonkeyPatch


import pytest


def test_pick_play_name(monkeypatch: MonkeyPatch) -> None:
    test_cli = Cli()
    input_name = "Test_Name"
    monkeypatch.setattr("builtins.input", lambda _: input_name)
    username = test_cli.pick_player_name()
    assert username == "Test_Name"


def test_guess_input(monkeypatch: MonkeyPatch) -> None:
    test_cli = Cli()
    input_value = "9999"
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    assert test_cli.guess_input(1, 4) == "9999"


@pytest.mark.parametrize(
    "prompt_input", ["y", "yes", "yeah", "Y", "Yes", "Yeah", "YES", "YEAH"]
)
def test_prompt_play_again_true(prompt_input, monkeypatch: MonkeyPatch) -> None:
    test_cli = Cli()
    input_value = prompt_input
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    assert test_cli.prompt_play_again() == True


@pytest.mark.parametrize("prompt_input", ["n", "no", "nah", "N", "NO", "NAH", "", "1"])
def test_prompt_play_again_false(prompt_input, monkeypatch: MonkeyPatch) -> None:
    test_cli = Cli()
    input_value = prompt_input
    monkeypatch.setattr("builtins.input", lambda _: input_value)
    assert test_cli.prompt_play_again() == False
