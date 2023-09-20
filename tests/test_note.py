
import unittest
from src.bot.commands import note

class TestNote(unittest.TestCase):

    def setUp(self):
        self.note = note.Note()

    def test_add_note(self):
        self.note.add_note("Test note")
        self.assertEqual(self.note.get_notes(), ["Test note"])

    def test_remove_note(self):
        self.note.add_note("Test note")
        self.note.remove_note("Test note")
        self.assertEqual(self.note.get_notes(), [])

    def test_clear_notes(self):
        self.note.add_note("Test note")
        self.note.clear_notes()
        self.assertEqual(self.note.get_notes(), [])

if __name__ == '__main__':
    unittest.main()

