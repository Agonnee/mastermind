class Game:

    def play_game(self):
        
        self.game_start()

        for i in range(10):
            self.turn()

        self.game_end()

    def game_start(self):
        pass

    def turn(self):
        pass

    def game_end(self):
        pass
