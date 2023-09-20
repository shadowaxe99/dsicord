
import unittest
from src.bot.commands import info_retrieval

class TestInfoRetrieval(unittest.TestCase):

    def setUp(self):
        self.info_retrieval = info_retrieval.InfoRetrieval()

    def test_retrieve_info(self):
        query = "Python programming"
        result = self.info_retrieval.retrieve_info(query)
        self.assertIsNotNone(result)

    def test_invalid_query(self):
        query = ""
        with self.assertRaises(ValueError):
            self.info_retrieval.retrieve_info(query)

if __name__ == '__main__':
    unittest.main()
