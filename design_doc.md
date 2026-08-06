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
Handles combining the rows and configuration settings.

### Tempo
Change ringing isn't measured in traditional beats per minute.
It is typically measured in "peal time" aka "peal speed", which is how long it takes to ring a standard length peal (5040) at that speed.
We can also measure in changes per minute, which is what we will use for this program.
Thus the `tempo` parameter measures changes per minute (CPM), and so one beat in MIDI should equal one change.
All of the notes for a row should fit in exactly one beat.

#### Handstroke Pause
Traditionally ringing is rung with a "handstroke pause".
Ringers will describe this as there being an extra beat in the rhythm of ringing.
Thus on $n$ bells, the handstroke/backstroke sequence is thought of as $2n+1$ notes, with the final note being silent.

In the implementation, there are two choices that could be made here:
1. Two rows are done strictly at the CPM, then an additional beat of silence is added. This means two rows will take up $2 + f$ beats where $f$ is some fraction of a beat.
    - Downside of this approach is that CPM is no longer true, as the beat of silence stretches out every row by fractions of a second. But over the course of thousands of changes, that adds up quickly. 
    - Upside is that the code is easier to implement.
2. Condense the timing of the MIDI notes such that the two rows and the beat of silence takes up exactly $2$ beats.
    - Downside of this approach is that the implementation and timing may be tricker to debug, especially when switching between the options of no handstroke pause and yes handstroke pause. The `time` variable for writing MIDI notes will always be an odd fractional value. I.e. the `time` where bells will be struck will look like $t = \frac{k}{2n+1}$ where $k \in \N$.
    - Additional downside is that at the same tempo/CPM, the version with a handstroke pause will sound "faster" due to one extra silent note being squeezed into the same amount of time.
    - Upside is that CPM will be exactly correct, at a given CPM there will be exactly that many changes per minute, with or without a handstroke pause.

#### Implementation
For the sake of producing files where the length accurately lines up with the CPM, option 2 will be implemented.

The number for which the time is incremented by will be $o = \frac{1}{2n+1}$ where $n$ is the number of bells being rung.
Thus in the main loop for note writing, we will be having `time += o`.

## MIDI to Audio File
This final optional step uses `fluidsynth` to take the MIDI and turn it into an audio file.

# File Structure
Each of these steps starts as its own Python file.
As each file bloats, create folders for them.

The steps are independent from each other beyond their sequential nature.