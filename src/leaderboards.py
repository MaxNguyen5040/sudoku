class Leaderboard:
    def __init__(self):
        self.scores = []

    def add_score(self, player_name, time, difficulty):
        self.scores.append({'name': player_name, 'time': time, 'difficulty': difficulty})
        self.scores = sorted(self.scores, key=lambda x: x['time'])

    def get_top_scores(self, top_n=10):
        return self.scores[:top_n]


leaderboard = Leaderboard()

def complete_game(player_name, time, difficulty):
    leaderboard.add_score(player_name, time, difficulty)
    top_scores = leaderboard.get_top_scores()

