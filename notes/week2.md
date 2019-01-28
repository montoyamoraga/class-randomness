# class-randomness-is-all-around

## Week 2: Introduction to randomness and sound with ChucK and Pure Data

### Sound art and computer music

Computers are cool for crunching numbers.

Computers were first used to control other musical instruments.

Computers were first able to synthesize and manipulate sound in an offline way, as in you had to render and hear your results afterwards.

Modern portable computers are now able to both synthesize and manipulate sound in realtime, and allow you to hear your results live. There is always latency, since computers are digital and in order to feed to speakers or headphones, it needs to be transformed to analog.

## Fourier transform

Fourier was so cool that at first it wasn't believed.

Fourier theorem/corollary

Any sound can be synthesized

Importance of sine wave: frequency, amplitude, phase

Sine waves as building blocks of any sound.

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

Importance of computers to be able to synthesize any sound


### Software for computer music

* [ChucK](http://chuck.cs.princeton.edu/)
* [CSound](https://en.wikipedia.org/wiki/Csound)
* [Max](https://en.wikipedia.org/wiki/Max_(software)), Cycling '74
* [Pure Data](https://en.wikipedia.org/wiki/Pure_Data), Miller Puckette, open-source, multiplatform, Windows
* [Sonic Pi](https://en.wikipedia.org/wiki/Sonic_Pi)
* [SuperCollider](https://en.wikipedia.org/wiki/Sonic_Pi)
* [TidalCycles](https://en.wikipedia.org/wiki/TidalCycles)

### Conferences

* [International Computer Music Conference](http://www.computermusic.org/)
* [International Conference on Live Coding](https://iclc.livecodenetwork.org/)
* [International Conference on New Interfaces for Musical Expression](http://www.nime.org/)

### Research centers

* [IRCAM](https://www.ircam.fr/)

### Famous examples

* [1-Bit Symphony](http://www.1bitsymphony.com/), by [Tristan Perich](https://en.wikipedia.org/wiki/Tristan_Perich).

* [Computer Controlled Acoustic Instruments pt2](https://en.wikipedia.org/wiki/Computer_Controlled_Acoustic_Instruments_pt2), by [Aphex Twin](https://en.wikipedia.org/wiki/Aphex_Twin).

* [Reactable](http://reactable.com/), developed at [Universitat Pompeu Fabra](https://www.upf.edu/) in Barcelona, Spain, and used by [Björk]()

* Brian Eno

* CITA, Rodrigo Cadiz and Patricio de la Cuadra.

* Radiohead, Jonny Greenwood, Max patches, thekingofgear.com, The King of Limbs.

## Places

* IRCAM
* University Pompeau Fabra

### Human sound perception

Psychoacoustics

* [20Hz to 20kHz (Human Audio Spectrum)](https://www.youtube.com/watch?v=qNf9nzvnd1k), experiment where sine wave frequency ramps exponentially from 20 Hz to 20 kHz.

Linear vs logarithm and exponentials.



Practical application: faders in mixing consoles


### ChucK

ChucK was developed by Ge Wang as part of his PhD thesis at Princeton.

ChucK is used at both the [Princeton Laptop Orchestra (PLOrk)](https://puplork.github.io/) and the [Stanford Laptop Orchestra (SLOrk)](http://slork.stanford.edu/).

To install ChucK, go to the [official website](http://chuck.cs.princeton.edu/), and install it. The software installed is called miniAudicle.

miniAudicle is an environment that lets you run a virtual machine that executes your ChucK scripts.

The most important windows of miniAudicle are:
* Console Monitor: for logging system messages.
* Virtual Machine Monitor: for starting and stopping the virtual machine, and managing the scripts being run.

### Chuck examples

* Sine wave oscillator


### Pure Data environment

Miller Puckette

Free libre open-source

Max MSP relationship.

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
