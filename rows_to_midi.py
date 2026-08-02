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

def row_to_pitches(row):
  pitches = []
  for b in row:
    pitches.append(bell_midi_map[int(b)])

  return pitches

class RowsToMIDI():
  track = 0
  channel = 0

  def __init__(self,tempo,outfile,handstroke_pause=True):
    self.tempo = tempo
    self.handstroke_pause = handstroke_pause


"""
Example midiutil code.

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
