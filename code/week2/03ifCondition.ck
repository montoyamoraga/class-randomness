// 03ifCondition.ck
// by aaron montoya-moraga
// january 2019

// oscillator, random frequency, random duration

// print message to console monitor
<<< "03ifCondition.ck" >>>;

// declare triangular oscillator
TriOsc myOsc;

// connect osc to dac
myOsc => dac;

// declare variable for coin flip
int coinFlip;

// declare two possible frequencies
1000 => float highFreq;
700 => float lowFreq;

// declare variable for variation
10 => int delta;

// flip coin
Std.rand2(0,1) => coinFlip;

// print result
<<< "tossCoin: " + coinFlip >>>;

// if coinFlip is 0, lo freq + tiny variation
// if coinFlip is 1, hi freq + tiny variation
if (coinFlip == 0) {
    lowFreq + Std.rand2(-delta, delta) => myOsc.freq;
}
else {
    highFreq + Std.rand2(-delta, delta) => myOsc.freq;
}

// set gain
0.2 => myOsc.gain;

// let 0.1 minute pass
0.1 :: minute => now;