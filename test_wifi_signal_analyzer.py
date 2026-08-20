import unittest
from wifi_signal_analyzer import classify_signal


class TestWiFiSignalAnalyzer(unittest.TestCase):

    def test_excellent_signal(self):
        self.assertEqual(classify_signal(-40), "Excellent")

    def test_good_signal(self):
        self.assertEqual(classify_signal(-55), "Good")

    def test_fair_signal(self):
        self.assertEqual(classify_signal(-65), "Fair")

    def test_weak_signal(self):
        self.assertEqual(classify_signal(-80), "Weak")

    def test_boundary_50(self):
        self.assertEqual(classify_signal(-50), "Excellent")

    def test_boundary_60(self):
        self.assertEqual(classify_signal(-60), "Good")

    def test_boundary_70(self):
        self.assertEqual(classify_signal(-70), "Fair")


if __name__ == "__main__":
    unittest.main()
