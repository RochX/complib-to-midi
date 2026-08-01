import unittest

import rows_from_complib

class TestRowsFromComplib(unittest.TestCase):
  def setUp(self):
    self.hunt_minimus = ['1234','2143','2413','4231','4321','3412','3142','1324','1234']
    return super().setUp()

  def test_get_method(self):
    self.assertEqual(rows_from_complib.get_rows(27808, "method"),self.hunt_minimus)


if __name__ == "__main__":
  unittest.main()