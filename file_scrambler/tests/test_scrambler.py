# libs
from unittest.mock import patch, call

import unittest
import shutil
import os


# lib to be tested
import file_scrambler.file_scrambler as scrambler

# logging
import logging

FILENAME = "log.log"
LEVEL = logging.DEBUG

# logging.basicConfig(filename=FILENAME, level=LEVEL, format="UNITTEST %(asctime)s %(levelname)s: %(message)s")


class TestFileScrambler(unittest.TestCase):

    test_script_dir = os.path.dirname(os.path.realpath(__file__))
    test_input_objects_dir = os.path.join(test_script_dir, "test_files", "data")

    output_results = os.path.join(test_script_dir, "test_files", "output")

    def setUp(self) -> None:
        if os.path.isdir(self.output_results):
            shutil.rmtree(self.output_results)

    def tearDown(self) -> None:
        pass

    def test_create_object(self):
        # create  object
        scrambler.FileScrambler()

    def test_get_file_list(self):
        """
        """

        # expected file list
        expected_file_list = [
            os.path.join(self.test_input_objects_dir, "file_1.txt"),
            os.path.join(self.test_input_objects_dir, "file_2.txt"),
            os.path.join(self.test_input_objects_dir, "file_3.txt"),
            os.path.join(self.test_input_objects_dir, "file_1.ini"),
            os.path.join(self.test_input_objects_dir, "file_2.ini"),
            os.path.join(self.test_input_objects_dir, "file_3.ini"),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        # call function to be tested
        file_list = scram._get_file_list(self.test_input_objects_dir)

        self.assertEqual(len(expected_file_list), len(file_list), "Wrong number of file")
        self.assertEqual(expected_file_list.sort(), file_list.sort(), "List of files not correct")

    def test_get_file_list_txt_type(self):
        """
        """

        # expected file list
        expected_file_list = [
            os.path.join(self.test_input_objects_dir, "file_1.txt"),
            os.path.join(self.test_input_objects_dir, "file_2.txt"),
            os.path.join(self.test_input_objects_dir, "file_3.txt"),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        # call function to be tested
        file_list = scram._get_file_list(self.test_input_objects_dir, "txt")

        self.assertEqual(len(expected_file_list), len(file_list), "Wrong number of file")
        self.assertEqual(expected_file_list.sort(), file_list.sort(), "List of files not correct")

    def test_get_file_list_ini_type(self):
        """
        """

        # expected file list
        expected_file_list = [
            os.path.join(self.test_input_objects_dir, "file_1.ini"),
            os.path.join(self.test_input_objects_dir, "file_2.ini"),
            os.path.join(self.test_input_objects_dir, "file_3.ini"),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        # call function to be tested
        file_list = scram._get_file_list(self.test_input_objects_dir, "ini")

        self.assertEqual(len(expected_file_list), len(file_list), "Wrong number of file")
        self.assertEqual(expected_file_list.sort(), file_list.sort(), "List of files not correct")

    def test_scramble_files_list(self):
        """
        """

        # create  object
        scram = scrambler.FileScrambler()

        file_list = scram._get_file_list(self.test_input_objects_dir)

        # call function to be tested
        new_file_list = scram._scramble_list(file_list)

        self.assertEqual(len(file_list), len(new_file_list), "Wrong number of files")
        self.assertNotEqual(file_list, new_file_list, "List of files not scrambled")
        self.assertEqual(file_list.sort(), new_file_list.sort(), "List of files not equal")

    def test_scramble_txt_files_list(self):
        """
        """

        # create  object
        scram = scrambler.FileScrambler()

        file_list = scram._get_file_list(self.test_input_objects_dir, "txt")

        # call function to be tested
        new_file_list = scram._scramble_list(file_list)

        self.assertEqual(len(file_list), len(new_file_list), "Wrong number of files")
        self.assertNotEqual(file_list, new_file_list, "List of files not scrambled")
        self.assertEqual(file_list.sort(), new_file_list.sort(), "List of files not equal")

    def test_scramble_ini_files_list(self):
        """
        """

        # create  object
        scram = scrambler.FileScrambler()

        file_list = scram._get_file_list(self.test_input_objects_dir, "ini")

        # call function to be tested
        new_file_list = scram._scramble_list(file_list)

        self.assertEqual(len(file_list), len(new_file_list), "Wrong number of files")
        self.assertNotEqual(file_list, new_file_list, "List of files not scrambled")
        self.assertEqual(file_list.sort(), new_file_list.sort(), "List of files not equal")

    def test_rename_files_list(self):
        """
        """

        # expected file list
        expected_file_list = [
            os.path.join(self.test_input_objects_dir, "1.txt"),
            os.path.join(self.test_input_objects_dir, "2.txt"),
            os.path.join(self.test_input_objects_dir, "3.txt"),
            os.path.join(self.test_input_objects_dir, "1.ini"),
            os.path.join(self.test_input_objects_dir, "2.ini"),
            os.path.join(self.test_input_objects_dir, "3.ini"),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        file_list = scram._get_file_list(self.test_input_objects_dir)
        scramble_file_list = scram._scramble_list(file_list)

        # call function to be tested
        new_file_list = scram._rename_list(scramble_file_list)

        self.assertEqual(len(file_list), len(new_file_list), "Wrong number of files")
        self.assertEqual(expected_file_list.sort(), new_file_list.sort(), "List of files not equal")

    def test_rename_txt_files_list(self):
        """
        """

        # expected file list
        expected_file_list = [
            os.path.join(self.test_input_objects_dir, "1.txt"),
            os.path.join(self.test_input_objects_dir, "2.txt"),
            os.path.join(self.test_input_objects_dir, "3.txt"),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        file_list = scram._get_file_list(self.test_input_objects_dir, "txt")
        scramble_file_list = scram._scramble_list(file_list)

        # call function to be tested
        new_file_list = scram._rename_list(scramble_file_list)

        self.assertEqual(len(file_list), len(new_file_list), "Wrong number of files")
        self.assertEqual(expected_file_list.sort(), new_file_list.sort(), "List of files not equal")

    def test_rename_ini_files_list(self):
        """
        """

        # expected file list
        expected_file_list = [
            os.path.join(self.test_input_objects_dir, "1.ini"),
            os.path.join(self.test_input_objects_dir, "2.ini"),
            os.path.join(self.test_input_objects_dir, "3.ini"),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        file_list = scram._get_file_list(self.test_input_objects_dir, "ini")
        scramble_file_list = scram._scramble_list(file_list)

        # call function to be tested
        new_file_list = scram._rename_list(scramble_file_list)

        self.assertEqual(len(file_list), len(new_file_list), "Wrong number of files")
        self.assertEqual(expected_file_list.sort(), new_file_list.sort(), "List of files not equal")

    def test_create_pairs_list(self):
        """
        """

        # input list
        scramble_file_list = [
            os.path.join(self.test_input_objects_dir, "3.txt"),
            os.path.join(self.test_input_objects_dir, "1.txt"),
            os.path.join(self.test_input_objects_dir, "2.txt"),
        ]

        # expected file list
        expected_file_list = [
            (os.path.join(self.test_input_objects_dir, "3.txt"), os.path.join("", "1.txt")),
            (os.path.join(self.test_input_objects_dir, "1.txt"), os.path.join("", "2.txt")),
            (os.path.join(self.test_input_objects_dir, "2.txt"), os.path.join("", "3.txt")),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        new_file_list = scram._rename_list(scramble_file_list)

        # call function to be tested
        list_of_pairs = scram._create_pairs_list(scramble_file_list, new_file_list, "")

        self.assertEqual(len(scramble_file_list), len(list_of_pairs), "Wrong number of files")
        self.assertEqual(expected_file_list, list_of_pairs, "Result is different")

    def test_copy(self):
        """
        """

        file_list = [
            ("file_1.txt", "2.txt"),
            ("file_2.txt", "4.txt"),
            ("file_3.txt", "6.txt"),
            ("file_4.txt", "3.txt"),
            ("file_5.txt", "1.txt"),
            ("file_6.txt", "5.txt"),
        ]

        # create  object
        scram = scrambler.FileScrambler()

        with patch("file_scrambler.file_scrambler.shutil.copyfile") as cp:
            # call function to be tested
            scram._copy_files(file_list)

            for num, pair in enumerate(file_list):
                assert cp.call_args_list[num] == call(pair[0], pair[1])

    def test_object_call(self):
        """
        """

        # create  object
        scram = scrambler.FileScrambler()

        # mock the _build_output_dir func
        scram._build_output_dir = unittest.mock.MagicMock()
        scram._build_output_dir.return_value = self.output_results

        # call object
        scram(self.test_input_objects_dir)

        scram._build_output_dir.assert_called_once()
