import unittest
import Util

"""unittest is created by Rasna Rahman"""


class TestUtil (unittest.TestCase):
    # Testing the calculation for base price.
    def test_getBasePrice(self):
        result = Util.getBasePrice(0, 0)
        assert result == 0
        result = Util.getBasePrice(1, 0)
        assert result == 1
        result = Util.getBasePrice(0, 1)
        assert result == 0.75

    # Testing the calculation for Combo price.
    def test_getComboPrice(self):
        result = Util.getComboPrice(1, 1)
        assert result == 1.5
        result = Util.getComboPrice(2, 1)
        assert result == 2.5
        result = Util.getComboPrice(1, 2)
        assert result == 2.25

    # Testing if the programme can count the Combo
    def test_isCombo(self):
        result = Util.isCombo(1, 0)
        assert result == False
        result = Util.isCombo(1, 1)
        assert result == True
