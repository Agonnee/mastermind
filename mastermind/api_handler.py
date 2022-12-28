""" from dotenv import load_dotenv
import os """
import requests

""" 
load_dotenv()

API_KEY = os.getenv("API_KEY") or "" """


class API_Handler:

    def get_code(self) -> str:
        response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")
        secret_code = response.text.strip().replace("\n","")
        return secret_code