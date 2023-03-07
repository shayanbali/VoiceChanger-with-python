from pathlib import Path

import parselmouth
import soundfile as sf
import pitch
import librosa
import numpy as np

# def genderRecgnition(file_path):
#     # Load a speech file and extract its pitch contour
#     file_path = file_path
#     snd = parselmouth.Sound(file_path)
#     pitch = snd.to_pitch()
#
#     # Calculate some basic statistics of the pitch contour
#     mean_pitch = np.mean(pitch.selected_array['frequency'])
#     median_pitch = np.median(pitch.selected_array['frequency'])
#     pitch_range = np.max(pitch.selected_array['frequency']) - np.min(pitch.selected_array['frequency'])
#
#     # Use the statistics to predict the gender of the speaker
#     if mean_pitch > 180 and pitch_range > 50:
#         predicted_gender = 'female'
#     elif mean_pitch < 180 and pitch_range > 50:
#         predicted_gender = 'male'
#     else:
#         predicted_gender = 'unknown'
#
#     print('Predicted gender:', predicted_gender)
#     print(mean_pitch)
#     return predicted_gender
from numpy import fft
from scipy.io import wavfile


def findMax(address):
    sampling_rate, signal = wavfile.read(address)
    if signal.ndim > 1:
        signal = signal.sum(axis=1)
    fourier_transform = np.fft.rfft(signal)

    abs_fourier_transform = np.abs(fourier_transform)

    power_spectrum = np.square(abs_fourier_transform)
    frequency = fft.fftfreq(len(signal), 1 / sampling_rate)[:len(power_spectrum)]
    max_value = max(power_spectrum)
    power_spectrum = list(power_spectrum)
    max_index = power_spectrum.index(max_value)
    return frequency[max_index]




# a function that change the pitch according to gender
def pitchChanger(v, sr, filepath1):
    gender = genderRecognition(filepath1)
    # change the pitch according to gender
    if gender == "male":
        v = librosa.effects.pitch_shift(v, sr=sr, n_steps=6)
    elif gender == "female":
        v = librosa.effects.pitch_shift(v, sr=sr, n_steps=-6)

    return v


# Load a speech wih librosa

my_file = "qdoz5-ijl21.wav"
voice, sr = librosa.load(my_file, sr=None, mono=False)
if voice.ndim > 1:
    voice = voice[0, :]

filepath = Path(my_file)

# a function that change the pitch of sound
changed_pitch_voice = pitchChanger(voice, sr, my_file)

# write final output
output_path = filepath.parent / (filepath.stem + "pitch_changed" + filepath.suffix)
sf.write(str(output_path), changed_pitch_voice, sr)
