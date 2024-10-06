# Worst Pico-Based Waveform Generator

Simplest and probably worst Arbitrary Waveform Generator (AWG).

AWG outputs voltage according to some arbitrary mathematical function. So, we need a function and ability to output voltage, run in a loop, done.

The problem is, we don't have DAC to output voltage programmatically. So we crudely simulate DAC via PWM and a low-pass filter. This has very low effective bandwidth, but works.

## Schematic

![schematic](./worst_awg.png?raw=true)

## Results

Sine wave:

![sine wave](./results/out_sine.png?raw=true)

Triangle (sawtooth):

![sine wave](./results/out_saw.png?raw=true)

On the necessity of second filter stage:

![after first filter stage, the voltage is still noisy](./results/filter.png?raw=true)
