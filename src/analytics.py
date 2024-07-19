import json

class GameAnalytics:
    def __init__(self, analytics_file='analytics.json'):
        self.analytics_file = analytics_file
        self.data = self.load_analytics()

    def load_analytics(self):
        try:
            with open(self.analytics_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {'interactions': 0, 'features': {}}

    def save_analytics(self):
        with open(self.analytics_file, 'w') as file:
            json.dump(self.data, file)

    def track_interaction(self):
        self.data['interactions'] += 1
        self.save_analytics()

    def track_feature(self, feature):
        if feature not in self.data['features']:
            self.data['features'][feature] = 0
        self.data['features'][feature] += 1
        self.save_analytics()

    def record_game(self, player_name, time, moves, difficulty, won):
        game_record = {
            'player_name': player_name,
            'time': time,
            'moves': moves,
            'difficulty': difficulty,
            'won': won
        }
        self.history.append(game_record)

    def get_statistics(self):
        total_games = len(self.history)
        wins = sum(1 for game in self.history if game['won'])
        avg_time = sum(game['time'] for game in self.history) / total_games if total_games else 0
        return {'total_games': total_games, 'wins': wins, 'avg_time': avg_time}


analytics = GameAnalytics()

def user_interaction():
    analytics.track_interaction()

def use_feature(feature):
    analytics.track_feature(feature)
