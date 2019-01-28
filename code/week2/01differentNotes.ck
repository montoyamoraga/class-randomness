// 01differentNotes.ck
// by aaron montoya-moraga
// january 2019

// oscillator, 440 Hz, 1 second long
// same oscillator, 770 Hz, 2 second long

// print message to console monitor
<<< "01differentNotes.ck" >>>;

// declare oscillator
SinOsc myOsc;

// connect osc to dac
myOsc => dac;

// assign frequency of oscillator
440 => myOsc.freq;

// assign gain of oscillator
// gain goes from 0.0 to 1.0
0.7 => myOsc.gain;

// let 1 second pass
1 :: second => now;

// change frequency
770 => myOsc.freq;

// let 2 seconds pass
2 :: second => now;