import numpy as np

def generate_sine_tone(frequency, duration_ms, sample_rate=44100):
    duration_s = duration_ms / 1000  # Convert ms to seconds
    t = np.linspace(0, duration_s, int(sample_rate * duration_s), endpoint=False)  # Time vector
    sine_wave = np.sin(2 * np.pi * frequency * t)  # Generate sine wave
    return sine_wave

def string_to_binary(string):
    return ''.join(format(ord(char), '08b') for char in string)

def string_to_eas(string, header=True):
    tones = []
    binary_data = string_to_binary(string)
    if header:
        binary_data = ("10101011" * 16) + binary_data

    for i in range(0, len(binary_data)):
        if binary_data[i] == '0':
            tones.append(generate_sine_tone(1562.5, 1.92, 8000))
        elif binary_data[i] == '1':
            tones.append(generate_sine_tone(2083.3, 1.92, 8000))

    return np.concatenate(tones)