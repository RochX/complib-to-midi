# complib-to-midi
This code is aimed at change ringers.
If you don't know what change ringing is, two videos I recommend are by [Tom Scott](https://youtu.be/WGia1R3xacM?si=NFDhK_3tAEsdzM4B) and [Kemp Brinson](https://youtu.be/g5ZaF8jlhGs?si=ylEXvS1IJhc4bdxo).

## What This Code Does
This code uses the `MIDIUtil` to write MIDI files from change ringing compositions.
It pulls the rows from compositions on [complib.org](complib.org) and converts them into MIDI.
Essentially one row equates to one "measure", and the numbers $1,2,3,...,n$ map to the notes of a musical scale.

## An example set of rows
See [Composition 162390](https://complib.org/composition/162390/) and its [rows](https://complib.org/composition/162390/rows) for an example.