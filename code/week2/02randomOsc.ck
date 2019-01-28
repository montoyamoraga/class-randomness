// 02randomOsc.ck
// by aaron montoya-moraga
// january 2019

// oscillator, random frequency, random duration

// print message to console monitor
<<< "02randomOsc.ck" >>>;

// declare oscillator
SinOsc myOsc;

// connect osc to dac
myOsc => dac;

// assign random oscillator frequency
// float number between 100 and 5,000
Std.rand2f(100, 5000) => myOsc.freq;

// assign oscillator gain
0.2 => myOsc.gain;

// let random time pass
// float number between 0.1 and 2.0 seconds
Std.rand2f(0.1, 2) :: second => now;