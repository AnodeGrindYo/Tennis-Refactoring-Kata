# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name  # TODO: Variable de classe séparée pour chaque joueur - Envisager l'utilisation d'une structure de données pour les joueurs.
        self.player2Name = player2Name
        self.p1points = 0  # TODO: Variable de classe séparée pour les points de chaque joueur - Envisager l'utilisation d'une structure de données pour les points.
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == "player1":  # TODO: Chaînes de caractères littérales - Utiliser des constantes ou des énumérations au lieu de chaînes en dur.
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        result = ""
        tempScore = 0
        if self.p1points == self.p2points:
            # TODO: Utilisation de nombres magiques - Remplacer par des constantes nommées pour une meilleure clarté.
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")  # TODO: Utilisation possible de dictionnaires - Utiliser un dictionnaire à un niveau plus élevé pour éviter les déclarations en dur.
        elif self.p1points >= 4 or self.p2points >= 4:
            minusResult = self.p1points - self.p2points
            # TODO: Méthode trop complexe - Ce bloc pourrait être simplifié en décomposant la logique en sous-fonctions.
            if minusResult == 1:
                result = "Advantage player1"
            elif minusResult == -1:
                result = "Advantage player2"
            elif minusResult >= 2:
                result = "Win for player1"
            else:
                result = "Win for player2"
        else:
            for i in range(1, 3):
                # TODO: Duplication de code - Envisager une méthode pour gérer la logique de score.
                if i == 1:
                    tempScore = self.p1points
                else:
                    result += "-"
                    tempScore = self.p2points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[tempScore]  # TODO: Duplication du dictionnaire de score - Envisager une meilleure gestion des scores.
        return result


