import unittest
import Util

class TestUtil(unittest.TestCase):

    def test_getBasePrice(self):
        result = Util.getBasePrice(0, 0)
        assert result == 0
        result = Util.getBasePrice(1, 0)
        assert result == 1
        result = Util.getBasePrice(0, 1)
        assert result == 0.75

    def test_getComboPrice(self):
        result = Util.getComboPrice(1, 1)
        assert result == 1.5
        result = Util.getComboPrice(2, 1)
        assert result == 2.5
        result = Util.getComboPrice(1, 2)
        assert result == 2.25

    def test_isCombo(self):
        result = Util.isCombo(1, 0)
        assert result == False
        result = Util.isCombo(1, 1)
        assert result == True