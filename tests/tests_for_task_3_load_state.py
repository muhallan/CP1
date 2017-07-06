import unittest

from dojo.dojo import Dojo


class TestsForTask3LoadState(unittest.TestCase):
    """
    Test cases for load_state functionality and method
    """

    def setUp(self):
        """Set up the test case class"""
        self.dojo = Dojo()

    def test_if_filename_is_too_short(self):
        """Tests to see if the file name passed to be written is to short to be a valid txt file
        """
        file_name_entered = self.dojo.load_state("sql")
        self.assertEqual(file_name_entered, "short", msg="The file name entered is too short to be valid")

    def test_if_filename_does_not_end_with_sqlite(self):
        """
        Tests if a file name entered is not a valid text file since it doesn't end with .txt
        :return:
        """
        another_file_name = self.dojo.load_state("plain_text")
        self.assertEqual(another_file_name, "not sqlite file", msg="The file name entered doesn't end with .sqlite")

    def test_if_a_valid_file_name_is_used(self):
        """
        Tests to see if a valid text file name is recognized and written to
        :return:
        """
        valid_file = self.dojo.load_state("valid_db.sqlite")
        self.assertEqual(valid_file, "valid_db.sqlite")

    def test_if_people_are_actually_retrieved_from_the_database(self):
        """
        Tests retrieving people from the database and seeing if they are added back to the system
        :return:
        """
        self.dojo.load_people("test_load_people.txt")
        initial_people_count = len(self.dojo.all_people)  # shd return 7

        self.dojo.save_state("test_sqlite_db.sqlite")
        self.dojo.all_rooms.clear()
        self.dojo.all_people.clear()

        self.dojo.load_state("test_sqlite_db.sqlite")
        new_people_count = len(self.dojo.all_people)  # shd return same 7

        self.assertEqual(new_people_count, initial_people_count)
