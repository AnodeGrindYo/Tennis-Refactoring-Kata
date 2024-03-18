import unittest
from tennis1 import TennisGame1 as OriginalTennisGame
from tennis1_refactor import TennisGame as RefactoredTennisGame

def play_match(GameClass, p1_points, p2_points):
    game = GameClass("player1", "player2")
    for _ in range(p1_points):
        game.won_point("player1")
    for _ in range(p2_points):
        game.won_point("player2")
    return game.score()
    
class GoldenMasterTest(unittest.TestCase):
    report_filename = "comparison_report.txt"

    def test_golden_master(self):
        differences = []
        for p1_points in range(36): # Ce sont de très longs matchs !!
            for p2_points in range(36):
                original_score = play_match(OriginalTennisGame, p1_points, p2_points)
                refactored_score = play_match(RefactoredTennisGame, p1_points, p2_points)
                
                if original_score != refactored_score:
                    differences.append(f"Points: {p1_points}-{p2_points}, Original: {original_score}, Refactored: {refactored_score}")
        
        if differences:
            with open(self.report_filename, "w") as report_file:
                report_file.write("\n".join(differences))
            self.fail(f"Differences found in scores. See 'comparison_report.txt' for details.")

    def test_player_name_independence(self):
        # Ce test vérifie si les scores sont cohérents malgré le changement des noms des joueurs.
        # Ce test est effectué que pour mettre en évidence le problème sur la version non refactorisée.
        for p1_points in range(17):
            for p2_points in range(17):
                original_game_with_standard_names = OriginalTennisGame("player1", "player2")
                original_game_with_different_names = OriginalTennisGame("p1", "p2")
                
                for _ in range(p1_points):
                    original_game_with_standard_names.won_point("player1")
                    original_game_with_different_names.won_point("p1")

                for _ in range(p2_points):
                    original_game_with_standard_names.won_point("player2")
                    original_game_with_different_names.won_point("p2")

                original_score_with_standard_names = original_game_with_standard_names.score()
                original_score_with_different_names = original_game_with_different_names.score()

                self.assertEqual(original_score_with_standard_names, original_score_with_different_names, 
                                f"Scores on the original version do not match for games with different player names. "
                                f"With 'player1' and 'player2': {original_score_with_standard_names}. "
                                f"With 'p1' and 'p2': {original_score_with_different_names}.")


if __name__ == '__main__':
    unittest.main()