<<< "hello world!" >>>;

SinOsc myOsc => dac;

440 => myOsc.freq;

0.5 => myOsc.gain;

1 :: second => now;