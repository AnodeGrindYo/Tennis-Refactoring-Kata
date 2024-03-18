import unittest
from tennis1 import TennisGame1 as OriginalTennisGame
from tennis1_refactor import TennisGame as RefactoredTennisGame




DIR = ".\\golden-master\\"

def play_match(GameClass, p1_points, p2_points):
    game = GameClass("player1", "player2")
    for _ in range(p1_points):
        game.won_point("player1")
    for _ in range(p2_points):
        game.won_point("player2")
    return game.score()
    
class GoldenMasterTest(unittest.TestCase):
    report_filename = "comparison_report.txt"

    test_cases = [
            (0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
            (1, 0), (0, 1), (2, 0), (0, 2), (2, 1), (1, 2), (3, 0), (0, 3), (4, 0), (0, 4),
            (3, 2), (2, 3), (4, 1), (1, 4), (4, 2), (2, 4), (4, 3), (3, 4), (5, 4), (4, 5), (15, 14), (14, 15),
            (6, 4), (4, 6), (16, 14), (14, 16)
        ]

    def test_golden_master(self):
        
        differences = []
        
        for p1_points, p2_points in self.test_cases:
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
        game_with_standard_names = OriginalTennisGame("player1", "player2")
        game_with_different_names = OriginalTennisGame("p1", "p2")
        refactored_game_with_standard_names = RefactoredTennisGame("player1", "player2")
        refactored_game_with_different_names = RefactoredTennisGame("p1", "p2")

        for p1_points, p2_points in self.test_cases:
            for _ in range(p1_points):
                game_with_standard_names.won_point("player1")
                game_with_different_names.won_point("p1")
                refactored_game_with_standard_names.won_point("player1")
                refactored_game_with_different_names.won_point("p1")
            for _ in range(p2_points):
                game_with_standard_names.won_point("player2")
                game_with_different_names.won_point("p2")
                refactored_game_with_standard_names.won_point("player2")
                refactored_game_with_different_names.won_point("p2")

            score_with_standard_names = game_with_standard_names.score()
            score_with_different_names = game_with_different_names.score()
            refactored_score_with_standard_names = refactored_game_with_standard_names.score()
            refactored_score_with_different_names = refactored_game_with_different_names.score()

            self.assertEqual(score_with_standard_names, score_with_different_names, 
                                f"Scores on the original version do not match for games with different player names. "
                                f"With 'player1' and 'player2': {score_with_standard_names}. "
                                f"With 'p1' and 'p2': {score_with_different_names}.")
            self.assertEqual(refactored_score_with_standard_names, refactored_score_with_different_names,
                                f"Scores on the refactored version do not match for games with different player names. "
                                f"With 'player1' and 'player2': {refactored_score_with_standard_names}. "
                                f"With 'p1' and 'p2': {refactored_score_with_different_names}.")


if __name__ == '__main__':
    unittest.main()

