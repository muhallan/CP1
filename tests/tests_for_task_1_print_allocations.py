import unittest

from dojo.dojo import Dojo


class TestsForTask1PrintAllocations(unittest.TestCase):
    """Test cases for the print_allocations method and functionality
    """

    def setUp(self):
        """Set up the test case class"""
        self.dojo = Dojo()

    def test_if_filename_is_too_short(self):
        """Tests to see if the file name passed to be written is to short to be a valid txt file
        """
        file_name_entered = self.dojo.print_allocations("txt")
        self.assertEqual(file_name_entered, "short", msg="The file name entered is too short to be valid")

    def test_if_filename_does_not_end_with_txt(self):
        """
        Tests if a file name entered is not a valid text file since it doesn't end with .txt
        :return:
        """
        another_file_name = self.dojo.print_allocations("plain_text")
        self.assertEqual(another_file_name, "not txt file", msg="The file name entered doesn't end with .txt")

    def test_if_a_valid_file_name_is_used(self):
        """
        Tests to see if a valid text file name is recognized and written to. check if the right assignments are returned
        :return:
        """
        self.dojo.create_room("office", "red")
        self.dojo.add_person("allan", "muhwezi", "fellow", "y")

        valid_file = self.dojo.print_allocations("valid_file.txt")
        expected_string = "valid_file.txt" + ":" + "RED" + "\n" + "----------------------------------------------\n" + "allan muhwezi" + "\n\n"
        self.assertMultiLineEqual(valid_file, expected_string)

    def test_if_no_file_name_runs_successfully(self):
        """
        Tests to see if when argument is provided, the function runs successfully but doesn't create a file. check to
        see if the correct assignments are retrieved
        :return:
        """
        self.dojo.create_room("office", "red")
        self.dojo.add_person("allan", "muhwezi", "fellow", "y")

        valid_file = self.dojo.print_allocations()
        expected_string = "none:" + "RED" + "\n" + "----------------------------------------------\n" + "allan muhwezi" + "\n\n"
        self.assertMultiLineEqual(valid_file, expected_string)

        """TODO test like in print_room - same as - unallocated - load_people - add people to the text file. save_state: save and retrieve happen well."""
        """Spread some functionality across the classes"""
