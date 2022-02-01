import unittest
import pandas as pd

test_df = {'title': ['A remény rabjai', 'A keresztapa'],
           'aggregateRating': [9.3, 9.2],
           'ratingNumber': [2537184, 1746143],
           'Oscar': [0, 3],
           'rank': [1, 2]}
test_df = pd.DataFrame(test_df)

test_df_2 = {'title': ['A keresztapa', 'A remény rabjai'],
             'aggregateRating': [9.2, 9.3],
             'ratingNumber': [1746143, 2537184],
             'Oscar': [3, 0],
             'rank': [2, 1],
             'oscar_rating': [9.7, 9.3]}
test_df_2 = pd.DataFrame(test_df_2, index = [1, 0])

class TestOscar_calculator(unittest.TestCase):
    def test_oscar(self):
        from oscar_calculator import oscar_calculator
        self.assertEqual(oscar_calculator(test_df), test_df_2)

if __name__ == '__main__':
    unittest.main()