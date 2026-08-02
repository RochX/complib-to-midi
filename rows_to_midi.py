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

  def __init__(self,tempo,outfile,handstroke_pause=True):
    self.time = 0
    self.tempo = tempo
    self.handstroke_pause = handstroke_pause

    self.midi = MIDIFile(1)
    self.midi.addTempo(self.track, self.time, self.tempo)

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
