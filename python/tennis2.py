# -*- coding: utf-8 -*-

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        # TODO: Duplication de code - Envisager de fusionner les informations des joueurs et leurs points dans une structure unique.
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        # TODO: Duplication de code - Envisager une approche plus générique pour incrémenter les points afin de réduire la duplication.
        if playerName == "player1":
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        # TODO: Méthode trop longue - Découper cette méthode en sous-méthodes plus petites.
        # TODO: Utilisation de nombres magiques - Remplacer par des constantes nommées pour améliorer la lisibilité.
        # TODO: Conditions complexes - Simplifier ou réorganiser les conditions pour améliorer la clarté.
        # TODO: Duplication de code - Centraliser la logique de formatage des scores pour éviter la répétition.
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points==0):
                result = "Love"
            if (self.p1points==1):
                result = "Fifteen"
            if (self.p1points==2):
                result = "Thirty"
            result += "-All"
        if (self.p1points==self.p2points and self.p1points>2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points==0):
            if (self.p1points==1):
                P1res = "Fifteen"
            if (self.p1points==2):
                P1res = "Thirty"
            if (self.p1points==3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points==0):
            if (self.p2points==1):
                P2res = "Fifteen"
            if (self.p2points==2):
                P2res = "Thirty"
            if (self.p2points==3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res


        if (self.p1points>self.p2points and self.p1points < 4):
            if (self.p1points==2):
                P1res="Thirty"
            if (self.p1points==3):
                P1res="Forty"
            if (self.p2points==1):
                P2res="Fifteen"
            if (self.p2points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.p2points>self.p1points and self.p2points < 4):
            if (self.p2points==2):
                P2res="Thirty"
            if (self.p2points==3):
                P2res="Forty"
            if (self.p1points==1):
                P1res="Fifteen"
            if (self.p1points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage player1"

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage player2"

        if (self.p1points>=4 and self.p2points>=0 and (self.p1points-self.p2points)>=2):
            result = "Win for player1"
        if (self.p2points>=4 and self.p1points>=0 and (self.p2points-self.p1points)>=2):
            result = "Win for player2"
        return result

    def SetP1Score(self, number):
        # TODO: Duplication de code et Noms de méthodes non conventionnels - Unifier SetP1Score et SetP2Score en une seule méthode avec un paramètre pour le joueur.
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        # TODO: Manque d'encapsulation - Les modifications directes des attributs de score devraient être gérées par une méthode dédiée pour améliorer l'encapsulation.
        self.p1points +=1

    def P2Score(self):
        self.p2points +=1
