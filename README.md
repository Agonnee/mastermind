# Mastermind
Mastermind Game created for the LinkedIn REACH Apprenticeship Program.

Thank you to the REACH team and anyone else for taking the time to review this project, it has been rewarding to create. Learning to code has been one of the most exciting journeys I've had since I made the jump into working in technology. Transitioning from writing scripts for automation of simple tasks to building a project that can be iterated upon and extended makes me excited to see where my journey goes from here, and I thank you for the opportunity to be considered for the LinkedIn REACH apprenticeship program.

Created By: Hunter Moffitt

## About
Mastermind is a command line game in which you attempt to guess the secret code. 
After each guess you will be given feedback on how many digits you got correct, and how many were correct but in the wrong location.
Use this information to hone your answer and to crack the code!
After 10 guesses, if you haven't cracked the code, you have lost and the code will be revealed.

## To Play on Your Computer:

### Python installation
1. If you already have Python installed on your device, you can skip to the Initial Setup
   (Note: This program and many others require Python 3 or higher, if you're unsure of what version, choose the latest)
2. To install Python visit https://www.python.org/ and select downloads and install Python for your operating system.
   (Note: During installation, when prompted, add Python to Path) 
3. If you would like further specifics for Python installation, visit https://wiki.python.org/moin/BeginnersGuide/Download 

### Initial Setup
1. Create a new directory. 
2. In the terminal change directory into your new repo directory (Enter your directory's path)
   ```bash
   cd path/to/repo_dir
   ```
3. Clone this repo into the directory into the new directory.
   ```bash
   git clone https://github.com/Agonnee/mastermind.git
   ```
4. Create a virtual environment to contain the packages associated with this repository
   ```bash
   python -m venv env
   ```
5. Active the virtual environment by running the activate script from the .\env\Scripts\ subdirectory:

   - Windows cmd.exe
     ```bash
     .\env\Scripts\activate.bat
     ```
   - Powershell:
     ```bash
     .\env\Scripts\Activate.ps1
     ```
   - bash/zsh:
     ```bash
     .\env\Scripts\activate
     ```
6. Now that the virtual environment is activated, install the required libraries into the environment.
   ```bash
   python -m pip install -r requirements.txt
   ```
### Playing the Game

1. To start the gameL from the main repo directory, run mastermind.py
   ```bash
   python mastermind.py
   ```
   (Note: To run the game you will need to activate the virtual environment as shown in inital setup step 5 if not currently active.)
2. Following the prompts, choose a difficulty setting and enter your player name.
3. You will then be prompted for your first guess, enter your first guess and hit enter.
4. The Game will give you feed back on your guess.
5. Using the feedback given, continue to make guesses until you win, or the game is over.
6. Once the game is over, and you are done replaying, you can deactivate the virtual environment.
   ```bash
   deactivate
   ```


## Development Process and Tools

### Libraries Used
- Requests
- Requests-mock
- Pytest
- Pytest-coverage

### Building the Game
Starting out, the goal was to create the base system of being able to retrieve a secret code via the Random.org API and then compare guesses against that code. After reviewing the Random.org documentation for interger generation at https://www.random.org/clients/http/api/ and verifying that my requests returned a valid code, I started working on the guess checking system.

To go along with the Guess and Check system, I needed the command line interface to work for the prompts to be easy to understand. To facilitate this I started to build up the GameController class to handle the game's logic and progression.

Once I got the initial structure built up, I decided it was time to start writing the tests for the project. This would both allow me to check what I miss or break as I refactor or build more features without having to manually play through the game over and over. I needed to start making sure errors were handled along the way. The most likely cause of an error would be from the API call, so I wrote tests and added error handling into the API_Handler class.

I decided that having the CLI print statements and prompting for input was causing a lot of unnecessary complexity to the Gamecontroller's logic. I created a separate CLI class and UI protocol in order to separate out the front end of the game. I used the UI Protocol class in order to build the project in a way so that the CLI class wouldn't be the only option. It allows for the possibility of extension of the game to different UIs or even for localization of the UI through creating multiple different CLI classes. In the future I would like to provide an example of this in the project.

### Additional Features and Settings

As an additional feature, I wanted to add a difficulty setting. The difficulty setting would change the number of digits in the code and the range of numbers possible for each digit. In order to make this modular I created the Difficulty Enum so that difficulties could be added or modified without much effort by editing the values of difficulty.

I added a scoring system to track the local user scores for the game at each difficulty. The system saves to the data directory in the repo into a file named scores.json. The first time the game is played, the file will be created and saved. For unplayed difficulties, the unreachable score of 11 turns is stored, and the UI will not display scores above 10 when the leaderboard is shown.

