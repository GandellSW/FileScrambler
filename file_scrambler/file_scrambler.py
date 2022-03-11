from collections import defaultdict
from datetime import datetime

import random
import shutil
import copy
import sys
import os

# logging
import logging

FILENAME = "log.log"
LEVEL = logging.DEBUG

# logging.basicConfig(filename=FILENAME, level=LEVEL, format="%(asctime)s %(levelname)s: %(message)s")


class FileScrambler:
    """
    """

    def __init__(self):
        pass

    def __call__(self, dir_path, file_type=None):
        """
        Scramble files with new name to a new dir from input dir
        """

        output_dir = self._build_output_dir()

        # get list of files
        file_list = self._get_file_list(dir_path, file_type)
        # scramble list of files
        scramble_file_list = self._scramble_list(file_list)
        # change name of files
        new_file_list = self._rename_list(scramble_file_list)
        # create list of pairs or original file - new name file
        pair_files_list = self._create_pairs_list(scramble_file_list, new_file_list, output_dir)

        # create output dir
        logging.debug(f"Create dir: {output_dir}")
        os.mkdir(output_dir)

        # save to txt the combination of files and new names
        self._write_pairs_list(pair_files_list, output_dir)

        # save new files
        self._copy_files(pair_files_list)

    @classmethod
    def _build_output_dir(cls):
        """
        """

        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(__file__)

        script_dir = application_path
        now = datetime.now().strftime("%Y%m%d%H%M%S")

        return os.path.join(script_dir, now)

    def _write_pairs_list(self, pair_files_list, output_dir):
        """
        Write the txt file with old names and new names pair

        :param List[(os.path, os.path)] pair_files_list: list of pairs of old and new files
        :param os.path output_dir: new path for the new files
        :return None
        """

        with open(os.path.join(output_dir, "pairs.txt"), "w") as pairs_file:
            pairs_file.write(f"Original path:{os.path.dirname(pair_files_list[0][0])}\n")
            pairs_file.write(f"Rename path:{os.path.dirname(pair_files_list[0][1])}\n")

            logging.debug(f"Original path:{os.path.dirname(pair_files_list[0][0])}\n")
            logging.debug(f"Rename path:{os.path.dirname(pair_files_list[0][1])}\n")

            pairs_file.write("\nOriginal\tRename\n")
            for pair in pair_files_list:
                pairs_file.write(f"{os.path.basename(pair[0])}\t{os.path.basename(pair[1])}\n")

    def _get_file_list(self, path, file_type=None):
        """
        Get list of files present in path

        :param str path: path to the directory to get list of files
        :param str file_type: file type to get (default: None, get all files type)
        :return List[os.path]: list of files inside dir
        """

        files_list = []
        elements_in_path = os.listdir(path)

        for element in elements_in_path:
            element_full_path = os.path.join(path, element)
            if os.path.isfile(element_full_path):
                if not file_type:
                    files_list.append(element_full_path)
                elif element_full_path.endswith(file_type):
                    files_list.append(element_full_path)

        return files_list

    def _scramble_list(self, file_list):
        """
        Scramble list

        :param List[os.path] path: list to be scrambled
        :return List[os.path]: list scrambled
        """

        random_list = copy.copy(file_list)

        while random_list == file_list:
            random.shuffle(random_list)

        return random_list

    def _rename_list(self, scramble_file_list):
        """
        Rename list names considering the type

        :param List[os.path] path: list to be renamed
        :return List[os.path]: list renamed
        """

        renamed_list = []
        file_types = defaultdict(lambda: 1)

        for element in scramble_file_list:
            name, extension = os.path.splitext(element)
            name = os.path.basename(element)

            new_element = str(element).replace(name, f"{file_types[extension]}{extension}")
            file_types[extension] += 1

            renamed_list.append(os.path.normpath(new_element))

        return renamed_list

    def _create_pairs_list(self, list_names, list_new_names, new_path):
        """
        Create a tuple list of names and change dir of the new names

        :param List[os.path] list_names: list to of scrambled names
        :param List[os.path] list_new_names: list new names
        :param str new_path: new path for the new names
        :return List[(os.path, os.path)]: list of tuples
        """

        pair_files_list = []

        for f1, f2 in zip(list_names, list_new_names):
            # change new files dir to output dir
            f2 = os.path.join(new_path, os.path.basename(f2))
            pair_files_list.append((f1, f2))

        return pair_files_list

    def _copy_files(self, files_list):
        """
        Copy files from old name to new name

        :param List[(os.path, os.path)] files_list: list of tuple of files from old to new name
        :return None
        """

        for pair in files_list:
            # copy file from old name to new name
            shutil.copyfile(pair[0], pair[1])


if __name__ == "__main__":

    scram = FileScrambler()

    # call object
    scram(sys.argv[1])
