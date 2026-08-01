import unittest

import complib_api

class TestRowsFromComplib(unittest.TestCase):
  def setUp(self):
    self.hunt_minimus_json = [["1234","Go Original Minimus","8"],["1234","","16"],["2143","","264"],["2413","","20"],["4231","","268"],["4321","","16"],["3412","","264"],["3142","","20"],["1324","That's all; Stand","268"],["1234","","0"]]
    return super().setUp()

  def test_get_method(self):
    self.assertEqual(complib_api.get_rows(27808, "method"),self.hunt_minimus_json)


if __name__ == "__main__":
  unittest.main()