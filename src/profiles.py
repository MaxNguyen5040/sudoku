class UserProfile:
    def __init__(self, username):
        self.username = username
        self.statistics = {
            'puzzles_solved': 0,
            'hints_used': 0,
            'total_time_spent': 0
        }

    def increment_stat(self, stat_name):
        if stat_name in self.statistics:
            self.statistics[stat_name] += 1

    def add_time(self, time_spent):
        self.statistics['total_time_spent'] += time_spent
