class TennisGame3:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1Name, player2Name):
        self.p1 = 0
        self.p2 = 0
        self.p1_n = player1Name
        self.p2_n = player2Name

    def won_point(self, name):
        if name == self.p1_n:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if self.p1 == self.p2:
            return self._equal_score()
        elif self.p1 >= 4 or self.p2 >= 4:
            return self._advantage_or_win()
        else:
            return self._standard_score()

    def _equal_score(self):
        if self.p1 >= 3:
            return "Deuce"
        return f"{self.SCORE_NAMES[self.p1]}-All"

    def _advantage_or_win(self):
        diff = self.p1 - self.p2
        if diff == 1:
            return f"Advantage {self.p1_n}"
        elif diff == -1:
            return f"Advantage {self.p2_n}"
        elif diff >= 2:
            return f"Win for {self.p1_n}"
        else:
            return f"Win for {self.p2_n}"

    def _standard_score(self):
        return f"{self.SCORE_NAMES[self.p1]}-{self.SCORE_NAMES[self.p2]}"

    def _leading_player(self):
        if self.p1 > self.p2:
            return self.p1_n
        else: return self.p2_n
