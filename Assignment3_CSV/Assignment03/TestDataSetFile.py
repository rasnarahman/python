"""CST8333: Assignment 03 – Proof of Concept Delivery
   Author: Rasna Rahman
   Date: October 10, 2018
   this class testing the Data Set by Unit Testing."""

import unittest
from textwrap import dedent
from unittest.mock import mock_open,patch

from Assignment03.ReadDataSetFile import ReadDataSetFile

class TestDataSetFile(unittest.TestCase):

    DATA = dedent("""
        a,b,c
        x,y,z
        """).strip()

    @patch("builtins.open", mock_open(read_data=DATA))

    def test_open(self):

        # Due to how the patching is done, any module accessing `open' for the
        # duration of this test get access to a mock instead (not just the test
        # module).
        with open("DataSet.csv", "r") as f:
            result = f.read()

        open.assert_called_once_with("DataSet.csv", "r")
        self.assertEqual(self.DATA, result)
        self.assertEqual("a,b,c\nx,y,z", result)

        # Test 1:

    def test_csv_extension_valid(self):
        filename = 'projectData_backUp.csv'
        rd = ReadDataSetFile()
        validCsv = rd.verifyCsvFile(filename)
        assert validCsv == True

    def test_csv_extension_invalid(self):
        filename = 'projectData_backUp.txt'
        rd = ReadDataSetFile ()
        validCsv = rd.verifyCsvFile ( filename )
        assert validCsv==False
