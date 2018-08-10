"""Test the foldercompare.py module."""

import filecmp
import os
import shutil
import tempfile
import unittest
from os import path
import dircompare


class TestDiComparison(unittest.TestCase):
    """Test the _recursive_dircmp function."""

    def setUp(self):
        # Create a temporary directory
        self.test_dir1 = tempfile.mkdtemp()
        self.test_dir2 = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir1)
        shutil.rmtree(self.test_dir2)

    def test_same_name_diff_content(self):
        # Create a file in the temporary directory
        file1 = path.join(self.test_dir1, 'test.txt')
        with open(file1, 'w') as file:
            file.write('To be or not to be')

        file2 = path.join(self.test_dir2, 'test.txt')
        with open(file2, 'w') as file:
            file.write('To be or not to be.')

        report = dircompare.dir_compare(self.test_dir1, self.test_dir2)
        expected = {'same_name_diff_content': ['./test.txt'],
                    'only_dir1': [], 'only_dir2': [], 'same_name_same_content': []}
        self.assertEqual(report, expected)

    def test_same_name_same_content(self):
        # Create a file in the temporary directory
        file1 = path.join(self.test_dir1, 'test.txt')
        with open(file1, 'w') as file:
            file.write('To be or not to be')

        file2 = path.join(self.test_dir2, 'test.txt')
        with open(file2, 'w') as file:
            file.write('To be or not to be')

        report = dircompare.dir_compare(self.test_dir1, self.test_dir2)
        expected = {'same_name_same_content': ['./test.txt'],
                    'only_dir1': [], 'only_dir2': [], 'same_name_diff_content': []}
        self.assertEqual(report, expected)

    def test_file_in_dir1_only(self):
        # Create a file in the temporary directory
        file1 = path.join(self.test_dir1, 'test.txt')
        with open(file1, 'w') as file:
            file.write('To be or not to be')

        report = dircompare.dir_compare(self.test_dir1, self.test_dir2)
        expected = {'same_name_same_content': [],
                    'only_dir1': ['./test.txt'], 'only_dir2': [], 'same_name_diff_content': []}
        self.assertEqual(report, expected)

    def test_different_files_both(self):
        # Create a file in the temporary directory
        file1 = path.join(self.test_dir1, 'test.txt')
        with open(file1, 'w') as file:
            file.write('To be or not to be')

        file2 = path.join(self.test_dir1, 'test1.txt')
        with open(file2, 'w') as file:
            file.write('To be or not to be.')

        file3 = path.join(self.test_dir2, 'test.txt')
        with open(file3, 'w') as file:
            file.write('To be or not to be.')

        file4 = path.join(self.test_dir2, 'test.py')
        with open(file4, 'w') as file:
            file.write('sick of txt files')

        report = dircompare.dir_compare(self.test_dir1, self.test_dir2)
        expected = {'same_name_same_content': [],
                    'only_dir1': ['./test1.txt'], 'only_dir2': ['./test.py'], 'same_name_diff_content': ['./test.txt']}
        self.assertEqual(report, expected)

    def test_updated_file_same_content(self):
        # Create a file in the temporary directory
        file1 = path.join(self.test_dir1, 'test.txt')
        with open(file1, 'w') as file:
            file.write('To be or not to be')

        file2 = path.join(self.test_dir2, 'test.txt')
        with open(file2, 'w') as file:
            file.write('To be or not to be')

        report = dircompare.dir_compare(self.test_dir1, self.test_dir2)
        expected = {'same_name_same_content': ['./test.txt'],
                    'only_dir1': [], 'only_dir2': [], 'same_name_diff_content': []}
        self.assertEqual(report, expected)

        with open(file1, 'w') as file:
            file.write('To be or not to be updated')

        report = dircompare.dir_compare(self.test_dir1, self.test_dir2)
        expected = {'same_name_same_content': [],
                    'only_dir1': [], 'only_dir2': [], 'same_name_diff_content': ['./test.txt']}
        self.assertEqual(report, expected)

        with open(file1, 'w') as file:
            file.write('To be or not to be')

        report = dircompare.dir_compare(self.test_dir1, self.test_dir2)
        expected = {'same_name_same_content': ['./test.txt'],
                    'only_dir1': [], 'only_dir2': [], 'same_name_diff_content': []}
        self.assertEqual(report, expected)

if __name__ == '__main__':
    unittest.main()
