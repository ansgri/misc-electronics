import math
import time
from machine import Pin, PWM

signal_pin = Pin(21, Pin.OUT)
signal_pwm = PWM(signal_pin, freq=200000, duty_u16=32000)


def waveform(wave_frequency=500, steps=16, kind="saw"):
    # Parameters for the sawtooth wave
    step_delay = 1000000 // (wave_frequency * steps)  # Delay between steps

    # calibration for cycle time overhead
    # here, cycle time for (f=1000,s=20) was 1.420 ms
    # without adjustment, so we subtract 420/20
    step_delay -= 420 // 20

    if kind == "saw":
        duty_cycles = [int(65535 * i / steps) for i in range(steps)]
    elif kind == "sin":
        duty_cycles = [
            int(32767 * (1 + math.sin(2 * math.pi * i / steps))) for i in range(steps)
        ]
    else:
        raise RuntimeError("Unknown waveform")

    # Generate the sawtooth wave
    while True:
        for duty in duty_cycles:
            cur_ticks = time.ticks_us()
            signal_pwm.duty_u16(duty)
            time.sleep_us(step_delay)


waveform(1500, kind="sin", steps=16)
