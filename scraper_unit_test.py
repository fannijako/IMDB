import unittest
import pandas as pd

test_df = {'title': ['A remény rabjai', 'A keresztapa'],
           'aggregateRating': [9.3, 9.2],
           'ratingNumber': [2537184, 1746143],
           'Oscar': [0, 3],
           'rank': [1, 2]}
test_df = pd.DataFrame(test_df)

class TestScraper(unittest.TestCase):
    def test_scraper(self):
        from scraper import scraper
        self.assertEqual(scraper(2), test_df)


if __name__ == '__main__':
    unittest.main()
