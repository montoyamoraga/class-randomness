# class-randomness-is-all-around

## Week 2: Introduction to randomness and sound with ChucK and Pure Data

### Sound art and computer music

Computers are cool for crunching numbers.

Computers were first used to control other musical instruments.

Computers were first able to synthesize and manipulate sound in an offline way, as in you had to render and hear your results afterwards.

Modern portable computers are now able to both synthesize and manipulate sound in realtime, and allow you to hear your results live. There is always latency, since computers are digital and in order to feed to speakers or headphones, it needs to be transformed to analog.

## Fourier series and Fourier transform

Fourier was so cool that at first it wasn't believed.

Fourier lets us think of sine waves as the building blocks of any possible sound ever.

[Fourier series](https://en.wikipedia.org/wiki/Fourier_series) can describe any periodic signal as a weighted sum of sine waves.

[Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform) can describe any signal as a sum of sine waves that make it up. It results in the frequency domain representation of the original time-based signal.

Sine waves are cool because they can be identified without ambiguity with just 3 parameters:

* Frequency
* Amplitude
* Phase

* [An Interactive Introduction to Fourier Transforms](http://www.jezzamon.com/fourier/index.html), by [Jez Swanson](https://github.com/Jezzamonn).

### Psychoacoustics

Psychoacoustics studies how humans perceive sound.

The physical parameters of sound waves are correlated with perceptual parameters:

|Physical world|Human perception|
|Frequency     |Pitch           |
|Amplitude     |Volume          |
|Phase         |None            |

Importance of computers to be able to synthesize any sound.

## Sound as an analog wave

Sound is pressure waves that we feel with our ears.

Since sound is a physical real-world wave, it is an analog signal, as in, we can plot it as a value in time, and:

* In any moment in time, sound has a real value.
* Sound can be any value, with infinite resolution.

## Analog and digital conversions

If we want to manipulate sound in our computer, we need to first convert it to digital. For achieving this we use an [Analog-to-digital converter (ADC)](https://en.wikipedia.org/wiki/Analog-to-digital_converter).

If we render digital audio in our computer and we want to hear it, we must convert it to analog in order to hear it. For achieving this we use a [Digital-to-analog converter](https://en.wikipedia.org/wiki/Digital-to-analog_converter).

## Digital audio

In order to convert an analog real-world sound to digital, we need to make it go through two processes:

* Sampling
* Quantizing

## Sampling

In [sampling](https://en.wikipedia.org/wiki/Sampling_(signal_processing)), we start with an analog signal with infinite values, and we periodically take samples at a certain rate from it and just end up with these values. These rate is called sampling frequency or rate.

Sampling allows us to represent a signal, which originally has infinite values, with only a finite number of values from it.

The [Nyquist–Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) states that if you are sampling a signal with a frequency content with a maximum of x Hz, the sampling frequency should be more than 2*x Hz, in order to not lose information and being able to restore the original signal.

For us humans, we roughly hear a maximum frequency of 20 kHz. So in order to sample audio for humans, you need to use a sampling rate of at least 40 kHz.

CDs use a 44.1 kHz sampling rate, more than enough yay.

## Quantization

[Quantization](https://en.wikipedia.org/wiki/Quantization_(signal_processing)) rounds a signal to a finite set of values. The size of the ending set of values depends on the resolution, which can be measured in bits.

If we apply quantization to the sampled signal, we end up with a resulting signal with a finite number of values, and a finite resolution. Quantization is a destructive process, there is no way back to the original signal.

We need quantization in order to work with audio, because computers have a finite memory, and even one tiny speck of analog audio has a value with infinite decimals, so we need to approximate it in order to store it.

CDs use a sampling rate of 44.1 kHz and a quantization resolution of 16 bits, so that 1 second of mono audio is comprised of 44,1000 values, each one 16 bits long, for  total of 705,600 bits for one second of mono audio.


### Software for computer music

* [ChucK](http://chuck.cs.princeton.edu/)
* [CSound](https://en.wikipedia.org/wiki/Csound)
* [Max](https://en.wikipedia.org/wiki/Max_(software)), Cycling '74
* [Pure Data](https://en.wikipedia.org/wiki/Pure_Data), Miller Puckette, open-source, multiplatform, Windows
* [Sonic Pi](https://en.wikipedia.org/wiki/Sonic_Pi)
* [SuperCollider](https://en.wikipedia.org/wiki/Sonic_Pi)
* [TidalCycles](https://en.wikipedia.org/wiki/TidalCycles)

### Conferences

* [Algorithmic Art Assembly](https://aaassembly.org/)
* [International Computer Music Conference](http://www.computermusic.org/)
* [International Conference on Live Coding](https://iclc.livecodenetwork.org/)
* [International Conference on New Interfaces for Musical Expression](http://www.nime.org/)

### Famous examples

* [1-Bit Symphony](http://www.1bitsymphony.com/), by [Tristan Perich](https://en.wikipedia.org/wiki/Tristan_Perich).

* [Computer Controlled Acoustic Instruments pt2](https://en.wikipedia.org/wiki/Computer_Controlled_Acoustic_Instruments_pt2), by [Aphex Twin](https://en.wikipedia.org/wiki/Aphex_Twin).

* [Reactable](http://reactable.com/), developed at [Universitat Pompeu Fabra](https://www.upf.edu/) in Barcelona, Spain, and used by [Björk]()

* [Brian Eno + Peter Chilvers](http://www.generativemusic.com/)

* Radiohead's Jonny Greenwood heavily uses Max patches both in studio and live. In particular, in the solo of the song [Go To Sleep](https://www.youtube.com/watch?v=AWppYBhEeVU) Jonny uses a random stutterer. For more details check out [thekingofgear.com](http://thekingofgear.com/).

## Places

* [IRCAM](https://www.ircam.fr/)
* [University Pompeau Fabra](https://www.upf.edu/)

### Human sound perception


* [20Hz to 20kHz (Human Audio Spectrum)](https://www.youtube.com/watch?v=qNf9nzvnd1k), experiment where sine wave frequency ramps exponentially from 20 Hz to 20 kHz.

[Faders](https://en.wikipedia.org/wiki/Fade_(audio_engineering)) are an example of physical world versus sensorial world: in order to feel a linear change of volume, we need to logarithmically change the amplitude.

### ChucK

ChucK was developed by Ge Wang as part of his PhD thesis at Princeton.

ChucK is used at both the [Princeton Laptop Orchestra (PLOrk)](https://puplork.github.io/) and the [Stanford Laptop Orchestra (SLOrk)](http://slork.stanford.edu/).

To install ChucK, go to the [official website](http://chuck.cs.princeton.edu/), and install it. The software installed is called miniAudicle.

miniAudicle is an environment that lets you run a virtual machine that executes your ChucK scripts.

The most important windows of miniAudicle are:
* Console Monitor: for logging system messages.
* Virtual Machine Monitor: for starting and stopping the virtual machine, and managing the scripts being run.

### Chuck examples

* 00myFirstOsc.ck
* 01differentNotes.ck
* 02randomOsc.ck
* 03ifCondition.ck
* 04samplePlayback
* 05sampleRandom.ck
* 06sequencer.ck

### Pure Data environment

Miller Puckette wrote Pure Data.

It is FLOSS and can run on computers with Linux, Mac, or Windows.

It is a close relative of Max.

### Oscillators

Common waveforms: sine, triangle, square, sawtooth

Common control parameters: amplitude, frequency.

### Noise

random object in Pure Data

### Sequencers

Korg SQ-1

Make Noise René: cartesian

### Parameters for a one-voice synthesizer

|Module|Parameter|Control                |
|VCO   |Waveform |Choose modulation type |
|LFO   |Frequency|Choose modulation rate |
|LFO   |Amplitude|Choose modulation depth|
|VCO   |Waveform |Choose timbre          |
|VCO   |Frequency|Choose pitch           |
|VCO   |Amplitude|Choose volume          |
|VCF   |Type     |Choose LPF, HPF, BPF   |
|VCF   |Frequency|Choose cutoff frequency|
|VCF   |Resonance|Choose feedback        |
|VCA   |
|VCA   |
|VCA   |
|VCA   |


### Sampling

Use of samples

Akai MPC

Add patch for samples
