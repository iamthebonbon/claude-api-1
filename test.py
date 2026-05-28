import unittest
from main import calculate_pi_to_5_digits


class TestPiCalculation(unittest.TestCase):
    """Test cases for the pi calculation function"""
    
    def test_pi_value(self):
        """Test that pi is calculated correctly to at least 5 decimal places"""
        pi = calculate_pi_to_5_digits()
        # Expected value of pi: 3.14159...
        self.assertAlmostEqual(pi, 3.14159, places=5)
    
    def test_pi_greater_than_3(self):
        """Test that calculated pi is greater than 3"""
        pi = calculate_pi_to_5_digits()
        self.assertGreater(pi, 3)
    
    def test_pi_less_than_4(self):
        """Test that calculated pi is less than 4"""
        pi = calculate_pi_to_5_digits()
        self.assertLess(pi, 4)
    
    def test_pi_between_3_14_and_3_15(self):
        """Test that pi is between 3.14 and 3.15"""
        pi = calculate_pi_to_5_digits()
        self.assertGreater(pi, 3.14)
        self.assertLess(pi, 3.15)
    
    def test_pi_precision(self):
        """Test that pi matches known value to 5 decimal places"""
        pi = calculate_pi_to_5_digits()
        # Pi to 5 decimal places: 3.14159
        pi_str = f"{pi:.5f}"
        self.assertEqual(pi_str, "3.14159")


if __name__ == "__main__":
    unittest.main()
