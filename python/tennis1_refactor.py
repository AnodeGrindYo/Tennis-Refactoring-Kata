class TennisTranslation:
    SCORE_NAMES = {
        'en': {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
            'Deuce': "Deuce",
            'All': "All",
            'Win for': "Win for",
            'Advantage': "Advantage",
            'Invalid player name': "Invalid player name",
            'Unknown': "Unknown"
        },
        'fr': {
            0: "Zéro",
            1: "Quinze",
            2: "Trente",
            3: "Quarante",
            'Deuce': "Égalité",
            'All': "Tous",
            'Win for': "Victoire pour",
            'Advantage': "Avantage",
            'Invalid player name': "Nom du joueur invalide",
            'Unknown': "Inconnu"
        }
    }

    def __init__(self, lang='en'):
        self.lang = lang

    def get_score_name(self, score):
        return self.SCORE_NAMES.get(self.lang, {}).get(score, "Unknown")

    def get_translated_term(self, term):
        return self.SCORE_NAMES.get(self.lang, {}).get(term, "Unknown")


class TennisGame:
    def __init__(self, player1_name, player2_name, lang='en'):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player_scores = {player1_name: 0, player2_name: 0}
        self.translation = TennisTranslation(lang)

    def won_point(self, player_name):
        if player_name not in self.player_scores:
            raise ValueError(self.translation.get_translated_term("Invalid player name"))
        self.player_scores[player_name] += 1

    def _get_score_difference(self):
        return abs(self.player_scores[self.player1_name] - self.player_scores[self.player2_name])

    def _get_lead_player(self):
        if self.player_scores[self.player1_name] > self.player_scores[self.player2_name]:
            return self.player1_name
        elif self.player_scores[self.player2_name] > self.player_scores[self.player1_name]:
            return self.player2_name
        return None

    def _is_early_game_all(self):
        return self.player_scores[self.player1_name] < 3 and self.player_scores[self.player1_name] == self.player_scores[self.player2_name]

    def _is_deuce(self):
        return self.player_scores[self.player1_name] >= 3 and self.player_scores[self.player1_name] == self.player_scores[self.player2_name]

    def _is_advantage_or_win(self):
        return self.player_scores[self.player1_name] >= 4 or self.player_scores[self.player2_name] >= 4

    def _get_regular_score(self):
        return f"{self.translation.get_score_name(self.player_scores[self.player1_name])}-{self.translation.get_score_name(self.player_scores[self.player2_name])}"

    def score(self):
        if self._is_early_game_all():
            return f"{self.translation.get_score_name(self.player_scores[self.player1_name])}-All"
        elif self._is_deuce():
            return self.translation.get_translated_term('Deuce')
        elif self._is_advantage_or_win():
            lead_player = self._get_lead_player()
            status = 'Advantage' if self._get_score_difference() == 1 else 'Win for'
            return f"{self.translation.get_translated_term(status)} {lead_player}"
        return self._get_regular_score()