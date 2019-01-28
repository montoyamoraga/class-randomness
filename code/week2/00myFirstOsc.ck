// 00myFirstOsc.ck
// by aaron montoya-moraga
// january 2019

// oscillator, 440 Hz, 1 second long

// print message to console monitor
<<< "00myFirstOsc.ck" >>>;

// declare oscillator
SinOsc myOsc;

// connect osc to dac
myOsc => dac;

// assign oscillator frequency
// frequency range [20, 20k] Hz
440 => myOsc.freq;

// assign oscillator gain
// gain range [0.0, 1.0]
0.7 => myOsc.gain;

// let one second pass
// units of time should be unambiguous
// samp, ms, second, minute, hour, day, week
// time multiplier is double colon ::
1 :: second => now;
