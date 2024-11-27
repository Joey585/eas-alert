import os
from scipy.io.wavfile import write
import soundfile as sf
from createTTS import create_tts
import numpy as np
import us
from string_to_eas import string_to_eas, generate_sine_tone

def create_eas(origin, event_type, counties, message, expire, time, station, file_name):
    full_message = []
    eas_message = f"ZCZC-{origin}-{event_type}-"

    for index, county in enumerate(counties):
        eas_message += county
        if index != len(counties) - 1:
            eas_message += "-"

    eas_message += "+" + expire + "-"
    eas_message += time + "-"
    eas_message += station + "-"

    print(eas_message)

    original_dir = os.getcwd()

    header_tones = string_to_eas(eas_message)

    for i in range(3):
        full_message.append(header_tones)
        full_message.append(np.zeros(int(8000)))  # silence 1 second

    attention_signal1 = generate_sine_tone(853, 8000, 8000)
    attention_signal2 = generate_sine_tone(960, 8000, 8000)

    attention_signal = attention_signal1 + attention_signal2
    attention_signal = attention_signal / np.max(np.abs(attention_signal))

    full_message.append(attention_signal)
    full_message.append(np.zeros(int(8000)))  # silence 1 second

    tts_message = create_tts(f"[:dv ap 120] [:dv pr 50] [:dv g5 100] [:dv sm 60] [:dv as 85] [:dv qu 55] {message}")

    full_message.append(tts_message)

    for i in range(3):
        full_message.append(string_to_eas("NNNN"))
        full_message.append(np.zeros(int(8000)))  # silence 1 second

    full_message = np.concatenate([np.asarray(part) for part in full_message])

    full_message = (full_message * 32767).astype(np.int16)
    os.chdir(original_dir)
    write(file_name, 8000, full_message)
