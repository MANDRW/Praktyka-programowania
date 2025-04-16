class TennisGame1:
    SCORE_POINTS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if self.player1_points == self.player2_points:
            return self._equal_score()
        elif self.player1_points >= 4 or self.player2_points >= 4:
            return self._endgame_score()
        else:
            return self._regular_score()

    def _equal_score(self):
        if self.player1_points >= 3:
            return "Deuce"
        return f"{self.SCORE_POINTS[self.player1_points]}-All"

    def _endgame_score(self):
        diff = self.player1_points - self.player2_points
        if diff == 1:
            return f"Advantage {self.player1_name}"
        elif diff == -1:
            return f"Advantage {self.player2_name}"
        elif diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _regular_score(self):
        return f"{self.SCORE_POINTS[self.player1_points]}-{self.SCORE_POINTS[self.player2_points]}"
