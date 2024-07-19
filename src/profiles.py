class UserProfile:
    def __init__(self, username):
        self.username = username
        self.stats = {'games_played': 0, 'games_won': 0, 'total_time': 0}

    def update_stats(self, won, time_spent):
        self.stats['games_played'] += 1
        if won:
            self.stats['games_won'] += 1
        self.stats['total_time'] += time_spent

users = {}

def create_user(username):
    if username not in users:
        users[username] = UserProfile(username)
    return users[username]

def update_user_stats(username, won, time_spent):
    if username in users:
        users[username].update_stats(won, time_spent)