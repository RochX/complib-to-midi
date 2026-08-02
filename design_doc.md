# Design Doc
To ensure my code files don't get super bloated.

## complib_to_midi.py
Contains `main`.
Does the following:
1. Configuration
  - What scale?
  - What soundfont?
  - What tempo?
  - Add the calls?
2. Grabs the rows from complib
  - Takes user input for which composition
  - Method vs Composition
3. Exports rows to MIDI
  - Uses the configuration from step 1
4. MIDI to audio file
  - Uses `fluidsynth`
  - Ex. `fluidsynth -F output.wav -ni kzooBells.sf2 major-scale.mid`.

## Configuration
Should be its own folder

## Grabbing rows from complib
Just one file should be plenty.
- User input
- Grabbing the rows is in theory just a `curl`.
- There is also an API described at [complib API docs](https://complib.org/api)
  - THIS is certainly the right option over just running a `curl`.

## Export rows to MIDI
Handles combining the rows and configuration settings

## MIDI to Audio File
This final optional step uses `fluidsynth` to take the MIDI and turn it into an audio file.

# File Structure
Each of the three steps starts as its own file.
As each file bloats, create folders for them.

The steps are independent beyond the last one taking in the previous two steps as input.