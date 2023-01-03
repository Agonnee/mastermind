import requests


class API_Handler:
    def get_code(self, code_length: int = 4, digit_max: int = 7) -> str:
        """
        Takes Secret Code Length (default 4, 4-8), and Max value of a digit (default 7, 7-9)
        Returns a str of the secret code.
        """

        try:
            response = requests.get(
                f"https://www.random.org/integers/?num={code_length}&min=0&max={digit_max}&col=1&base=10&format=plain&rnd=new"
            )
            response.raise_for_status()
            secret_code = response.text.strip().replace("\n", "")
            return secret_code
        except requests.exceptions.HTTPError as err_http:
            print("An HTTP error has occurred: ", err_http)
            raise
        except requests.exceptions.ConnectionError as err_con:
            print("Network connection error: ", err_con)
            raise
        except requests.exceptions.Timeout as err_time:
            print("Timeout Error has occurred: ", err_time)
            raise
        except requests.exceptions.RequestException as err:
            print("An error has occurred: ", err)
            raise
