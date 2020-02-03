class Game:
    def __init__(self, score, time):
        self.score = score
        self.time = time

    def get_score(self):
        return self.score

    def get_time(self):
        return self.time

    def set_score(self, altitude):
        self.score = altitude

    def set_time(self, time):
        self.time = time
