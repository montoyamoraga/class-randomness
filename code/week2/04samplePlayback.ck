// 04samplePlayback.ck
// by aaron montoya-moraga
// january 2019

// sample playback

// declare sound buffers
// for loading and playing samples
SndBuf clap;
SndBuf cowbell;
SndBuf hihat;
SndBuf kick;
SndBuf snare;

// declare gain and connect to dac;
Gain masterGain => dac;

// gain starts max volume
1.0 => masterGain.gain;

// connect each sound buffer to gain and then to dac;
clap    => masterGain;
cowbell => masterGain;
hihat   => masterGain;
kick    => masterGain;
snare   => masterGain;

// load files
me.dir() + "/samples/clap.wav"    => clap.read;
me.dir() + "/samples/cowbell.wav" => cowbell.read;
me.dir() + "/samples/hihat.wav"   => hihat.read;
me.dir() + "/samples/kick.wav"    => kick.read;
me.dir() + "/samples/snare.wav"   => snare.read;

// fast forward samples to the end
clap.samples()    => clap.pos;
cowbell.samples() => cowbell.pos;
hihat.samples()   => hihat.pos;
kick.samples()    => kick.pos;
snare.samples()   => snare.pos;

// step counter
0 => int currentStep;
// number of steps
8 => int maxStep;

// tempo in beats per minute
200 => float bpm;
// go from beats per minute to ms per step
60 * 1000 / bpm => float msPerStep;

// print to console
<<< "msPerStep: " + msPerStep >>>;

// infinite loop
while(true) {
  // step sequencer
  for (0 => currentStep; currentStep < maxStep; currentStep++) {

        if (currentStep == 0) {
            // 0 => clap.pos;
            // 0 => cowbell.pos;
            // 0 => hihat.pos;
            0 => kick.pos;
            // 0 => snare.pos;
        }
        else if (currentStep == 1) {
            // 0 => clap.pos;
            // 0 => cowbell.pos;
            // 0 => hihat.pos;
            // 0 => kick.pos;
            // 0 => snare.pos;
        }
        else if (currentStep == 2) {
            // 0 => clap.pos;
            // 0 => cowbell.pos;
            0 => hihat.pos;
            // 0 => kick.pos;
            // 0 => snare.pos;
        }
        else if (currentStep == 3) {
            // 0 => clap.pos;
            // 0 => cowbell.pos;
            // 0 => hihat.pos;
            // 0 => kick.pos;
            0 => snare.pos;
        }
        else if (currentStep == 4) {
            // 0 => clap.pos;
            // 0 => cowbell.pos;
            // 0 => hihat.pos;
            // 0 => kick.pos;
            // 0 => snare.pos;
        }
        else if (currentStep == 5) {
            // 0 => clap.pos;
            // 0 => cowbell.pos;
             0 => hihat.pos;
            // 0 => kick.pos;
            // 0 => snare.pos;
        }
        else if (currentStep == 6) {
            // 0 => clap.pos;
            // 0 => cowbell.pos;
            // 0 => hihat.pos;
            // 0 => kick.pos;
            // 0 => snare.pos;
        }
        else if (currentStep == 7) {
            // 0 => clap.pos;
            0 => cowbell.pos;
            // 0 => hihat.pos;
            // 0 => kick.pos;
            // 0 => snare.pos;
        }
        // let time flow
        msPerStep :: ms => now;
    }
}
