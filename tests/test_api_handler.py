import pytest
import requests
import requests_mock
from src.api_handler import API_Handler


def test_get_req():
    """Expect to raise a RequestException"""

    test_handler = API_Handler()

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, exc=requests.exceptions.RequestException)

        with pytest.raises(requests.exceptions.RequestException) as exc:
            test_handler.get_code()


def test_get_code_http_err():
    """Expect to raise an HTTPError"""

    test_handler = API_Handler()

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, exc=requests.exceptions.HTTPError)
        with pytest.raises(requests.exceptions.HTTPError):
            test_handler.get_code()


def test_get_code_con_err():
    """Expect to raise a ConnectionError"""

    test_handler = API_Handler()

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, exc=requests.exceptions.ConnectionError)

        with pytest.raises(requests.exceptions.ConnectionError) as exc:
            test_handler.get_code()


def test_get_code_timeout():
    """Expect to raise a Timeout"""

    test_handler = API_Handler()

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, exc=requests.exceptions.Timeout)

        with pytest.raises(requests.exceptions.Timeout) as exc:
            test_handler.get_code()


def test_get_code_correct():
    """Expect to Return a 4-digit string."""

    test_handler = API_Handler()

    API_URL = "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"

    body_text = "0\n0\n0\n1\n\n"

    with requests_mock.Mocker() as mocker:
        mocker.get(API_URL, status_code=200, text=body_text)
        response = test_handler.get_code()

    assert response == "0001"
