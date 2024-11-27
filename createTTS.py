import subprocess

import numpy as np
import soundfile as sf
import os

from scipy.signal import resample


def create_tts(text, loudness_factor=1.5):  # Add loudness_factor
    os.chdir("C:\\Users\\joey5\\Downloads\\vs6")

    command = f'say -w temp.wav "{text}"'
    subprocess.run(command, shell=True, check=True)

    data, original_samplerate = sf.read("C:\\Users\\joey5\\Downloads\\vs6\\temp.wav")

    data = resample(data, int(len(data) * 8000 / original_samplerate))

    if data.ndim == 2:
        data = np.mean(data, axis=1)  # Average channels

    data = data / np.max(np.abs(data))

    data = data * loudness_factor

    data = np.clip(data, -1, 1)

    return data
