from midiutil import MIDIFile

bell_midi_map = {
  1: 81,
  2: 80,
  3: 78,
  4: 76,
  5: 74,
  6: 73,
  7: 71,
  8: 69
}

def row_to_pitches(row,shift=True):
  """
  Turns rows into pitches.

  Parameters:
    row: the input row
    shift: if true, sets the highest number to the lowest pitch. For ringers, this is equivalent to ringing on the back $n$ bells.  
  """
  pitches = []

  biggest_bell = 0
  for b in row:
    biggest_bell = max(biggest_bell,int(b))

  # when using the current 8 bell midi map:
  # list(bell_midi_map.keys()[-1]) == 8
  offset = list(bell_midi_map.keys())[-1] - biggest_bell

  for b in row:
    if shift:
      pitches.append(bell_midi_map[int(b)+offset])
    else:
      pitches.append(bell_midi_map[int(b)])

  return pitches

class RowsToMIDI():
  track = 0
  channel = 0
  volume = 100

  def __init__(self,tempo,handstroke_pause=True):
    """
    Parameters:
      tempo: Measured in changes per minute. Thus one entire beat is exactly one row
    """
    self.time = 0
    self.tempo = tempo
    self.handstroke_pause = handstroke_pause

    self.midi = MIDIFile(1)
    self.midi.addTempo(self.track, self.time, self.tempo)

  def output_midi(self, outfile):
    """
    Outputs the MIDI object to the desired file.
    """
    with open(outfile,'wb') as f:
      self.midi.writeFile(f)

  def convert(self, api_input_rows, stage):
    """
    The main function of this class. Takes the rows, turns it into the MIDI

    Parameters:
      api_input_rows: the rows of the method/composition from the complib api
      stage: how many bells are in the method/composition
    """

    # determines whether api_input_rows is full JSON or just the short version.
    short = True
    if len(api_input_rows[0]) > 1:
      short = False

    # puts the results from api into two separate lists
    rows = []
    calls = []
    for token in api_input_rows:
      if short:
        rows.append(token)
        calls.append('')
      else:
        rows.append(token[0])
        calls.append(token[1])

    # sets up the time increment based on hand stroke pause
    # see `design_doc.md` for more info on how these are chosen
    if self.handstroke_pause:
      self.time_step = 2/(2*stage+1)
    else:
      self.time_step = 1/stage

    # primary part, takes each row, writes to midi object
    assert len(rows) == len(calls)
    assert len(rows[0]) == stage
    for n, (row, call) in enumerate(zip(rows,calls)):
      # write each row
      for i, p in enumerate(row_to_pitches(row)):
        self.midi.addNote(self.track, self.channel, p, self.time, self.time_step, self.volume)
        self.time += self.time_step

      # on the odd numbered rows, we add a handstroke pause if applicable
      if self.handstroke_pause and n % 2 == 1:
        self.time += self.time_step

"""
Example midiutil code.

from midiutil import MIDIFile

degrees  = [69, 71, 73, 74, 76, 78, 80, 81]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i, pitch in enumerate(degrees):
    MyMIDI.addNote(track, channel, pitch, time + i/2, duration, volume)

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
"""
