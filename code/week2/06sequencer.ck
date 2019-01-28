// 06sequencer.ck
// by aaron montoya-moraga
// january 2019

// 8 step sequencer

// array of notes
[ 41,  42,  43,  44,  45,  46,  47,  48] @=> int note[];
// array of velocities
[127, 100,  90,  100, 80, 127,  95,  40] @=> int velocity[];

// beats per minute
120 => float bpm;
// milliseconds per beat
60 * 1000 / bpm => float msPerBeat;

// print tempo information
<<< "msPerBeat: " + msPerBeat >>>;

// declare new MidiIn variable
MidiOut outputMidi;

// declare new MidiMsg variable
MidiMsg msg;

// declare variable for MIDI port
int portMidi;

// assign MIDI port
1 => portMidi;

// try to open the MIDI port
if (!outputMidi.open(portMidi)) {
    //print error message
    <<< "cannot open MIDI port" >>>;
    //exit the shred
    me.exit();
}

// infinite loop
while (true) {
    // go through every step
    for (0 => int step; step < note.cap(); step++) {
        // go through every step
        <<< "step: " + step >>>;
        // fill the message with data
        // a MIDI message has three bytes
        // 144 is note on, channel 1
        144 => msg.data1;
        // retrieve the corresponding note number
        note[step] => msg.data2;
        // retrieve the corresponding note velocity
        velocity[step] => msg.data3;
        // send MIDI out
        outputMidi.send(msg);
        // let time flow
        msPerBeat :: ms => now;
        // send note off
        0 => msg.data3;
        outputMidi.send(msg);
    }
}