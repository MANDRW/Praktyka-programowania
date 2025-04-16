class TennisGame2:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            return self._equal_score()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self._advantage_or_win_score()
        else:
            return self._regular_score()

    def _equal_score(self):
        if self.p1points >= 3:
            return "Deuce"
        return f"{self.SCORE_NAMES[self.p1points]}-All"

    def _advantage_or_win_score(self):
        diff = self.p1points - self.p2points
        if diff == 1:
            return f"Advantage {self.player1_name}"
        elif diff == -1:
            return f"Advantage {self.player2_name}"
        elif diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _regular_score(self):
        return f"{self.SCORE_NAMES[self.p1points]}-{self.SCORE_NAMES[self.p2points]}"

    def set_p1_score(self, number):
        self.p1points = number

    def set_p2_score(self, number):
        self.p2points = number