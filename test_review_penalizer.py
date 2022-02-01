import unittest
import pandas as pd

test_df = {'title': ['A remény rabjai', 'A keresztapa'],
           'aggregateRating': [9.3, 9.2],
           'ratingNumber': [2537184, 1746143],
           'Oscar': [0, 3],
           'rank': [1, 2]}
test_df = pd.DataFrame(test_df)

test_df_2 = {'title': ['A remény rabjai', 'A keresztapa'],
             'aggregateRating': [9.3, 9.2],
             'ratingNumber': [2537184, 1746143],
             'Oscar': [0, 3],
             'rank': [1, 2],
             'pen_rating': [9.3, 8.5]}
test_df_2 = pd.DataFrame(test_df_2, index = [0, 1])

class TestReview_Penalizer(unittest.TestCase):
    def test_review_penalizer(self):
        from review_penalizer import review_penalizer
        self.assertEqual(review_penalizer(test_df), test_df_2)

if __name__ == '__main__':
    unittest.main()