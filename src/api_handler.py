import requests


class API_Handler:
    def get_code(self) -> str:

        try:
            response = requests.get(
                "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new"
            )
            response.raise_for_status()
            secret_code = response.text.strip().replace("\n", "")
            return secret_code
        except requests.exceptions.RequestException as err:
            print("An error has occurred: ", err)
            raise
        except requests.exceptions.HTTPError as err_http:
            print("An HTTP error has occurred: ", err_http)
            raise
        except requests.exceptions.ConnectionError as err_con:
            print("Network connection error: ", err_con)
            raise
        except requests.exceptions.Timeout as err_time:
            print("Timeout Error has occurred: ", err_time)
            raise
