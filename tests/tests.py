from pathlib import Path
import unittest

from complib_api import complib_api
from rows_to_midi import rows_to_midi

TEST_DIR = Path(__file__).parent
OUTPUT_DIR = TEST_DIR / "test_output"

class TestComplibAPI(unittest.TestCase):
  def setUp(self):
    self.hunt_minimus = ['1234','1234','2143','2413','4231','4321','3412','3142','1324','1234']
    self.hunt_minimus_json = [["1234","Go Original Minimus","8"],["1234","","16"],["2143","","264"],["2413","","20"],["4231","","268"],["4321","","16"],["3412","","264"],["3142","","20"],["1324","That's all; Stand","268"],["1234","","0"]]
    return super().setUp()

  def test_get_rows(self):
    self.assertEqual(complib_api.get_rows(27808, "method"),self.hunt_minimus_json)

  def test_get_rows_short(self):
    self.assertEqual(complib_api.get_rows_short(27808, "method"),self.hunt_minimus)

  def test_get_stage(self):
    self.assertEqual(complib_api.get_stage(27808, "method"),4)
    self.assertEqual(complib_api.get_stage(12399, "method"),7)
    self.assertEqual(complib_api.get_stage(162390, "composition"),8)

class TestRowsToMIDI(unittest.TestCase):
  def setUp(self):
    self.rounds4 = '1234'
    self.rounds5 = '12345'
    self.rounds8 = '12345678'
    self.bell_midi_map = rows_to_midi.bell_midi_map
    self.tempo = 30
    self.hunt_minimus = ['1234','1234','2143','2413','4231','4321','3412','3142','1324','1234']
    self.hunt_minimus_json = [["1234","Go Original Minimus","8"],["1234","","16"],["2143","","264"],["2413","","20"],["4231","","268"],["4321","","16"],["3412","","264"],["3142","","20"],["1324","That's all; Stand","268"],["1234","","0"]]

    OUTPUT_DIR.mkdir(exist_ok=True)
    return super().setUp()

  def test_rows_to_pitches(self):
    self.assertEqual(rows_to_midi.row_to_pitches(self.rounds4,shift=False),[81,80,78,76])
    self.assertEqual(rows_to_midi.row_to_pitches(self.rounds4,shift=True),[74,73,71,69])
    self.assertEqual(rows_to_midi.row_to_pitches(self.rounds5,shift=False),[81,80,78,76,74])
    self.assertEqual(rows_to_midi.row_to_pitches(self.rounds5,shift=True),[76,74,73,71,69])
    self.assertEqual(rows_to_midi.row_to_pitches(self.rounds8,shift=False),[81,80,78,76,74,73,71,69])
    self.assertEqual(rows_to_midi.row_to_pitches(self.rounds8,shift=True),[81,80,78,76,74,73,71,69])

  def test_rows_to_midi_no_handstroke_pause(self):
    midi_obj = rows_to_midi.RowsToMIDI(self.tempo, False)

    # todo: this test doesn't test the JSON format. when we test the call version that will test the JSON format
    midi_obj.convert(self.hunt_minimus, 4)
    midi_obj.output_midi(OUTPUT_DIR / "plain_minimus_no_pause.mid")

  def test_rows_to_midi_handstroke_pause(self):
    midi_obj = rows_to_midi.RowsToMIDI(self.tempo, True)

    # todo: this test doesn't test the JSON format. when we test the call version that will test the JSON format
    midi_obj.convert(self.hunt_minimus, 4)
    midi_obj.output_midi(OUTPUT_DIR / "plain_minimus_handstroke_pause.mid")


if __name__ == "__main__":
  unittest.main()