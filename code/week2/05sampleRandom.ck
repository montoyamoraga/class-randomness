// 05sampleRandom.ck
// by aaron montoya-moraga
// january 2019

// sample playback with randomness

// declare sound buffers
// for loading and playing samples
SndBuf clap;
SndBuf cowbell;
SndBuf hihat;
SndBuf kick;
SndBuf snare;

// declare gain and connect to dac;
Gain masterGain => dac;

// gain starts at maximum volume
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

10 => float maxRate;

// random playback rates
Math.random2f(-maxRate, maxRate)   => clap.rate;
Math.random2f(-maxRate, maxRate) => cowbell.rate;
Math.random2f(-maxRate, maxRate)   => hihat.rate;
Math.random2f(-maxRate, maxRate)    => kick.rate;
Math.random2f(-maxRate, maxRate)   => snare.rate;

// rate 0 is pause
// rate 1 is normal speed
// between 0 and 1 is slower
// more than 1 is faster
// less than 0 is backwards and everything else applies


// step counter
0 => int currentStep;
// number of steps
8 => int maxStep;

// tempo in beats per minute
Math.random2f(60, 600) => float bpm;
// go from beats per minute to ms per step
60 * 1000 / bpm => float msPerStep;
<<< "msPerStep: " + msPerStep >>>;
// delta for variation
msPerStep/2 => float delta;

while(true) {
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
            0 => clap.pos;
            // 0 => cowbell.pos;
            // 0 => hihat.pos;
            // 0 => kick.pos;
            // 0 => snare.pos;
        }
        //let time flow
        (msPerStep + Math.random2f(-delta, delta)) :: ms => now;
    }
}
