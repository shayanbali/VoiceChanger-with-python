from pathlib import Path
import soundfile as sf
import pitch
import librosa
import numpy as np
from numpy import fft
from scipy.io import wavfile
import matplotlib.pyplot as plt

# find the max point with fourier series
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



def plotPitch(my_file1):
    # Load audio file
    y, sr = librosa.load(my_file1)

    # Calculate pitch using the YIN algorithm
    pitch, _ = librosa.piptrack(y=y, sr=sr, fmin=50, fmax=2000)

    # Plot pitch values over time
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(pitch, y_axis='linear', x_axis='time', sr=sr, hop_length=512)
    plt.colorbar()
    plt.title('Pitch contour of ' + my_file1)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Time (s)')
    plt.tight_layout()
    plt.show()


# recognize the gender according to the result
def genderRecognition(address):
    if findMax(address) < 180:
        label = "male"
    else:
        label = "female"

    print("Predicted gender: ", label)
    return label


# a function that change the pitch according to gender
def pitchChanger(v, sr, filepath1):
    gender = genderRecognition(filepath1)
    # change the pitch according to gender
    if gender == "male":
        v = librosa.effects.pitch_shift(v, sr=sr, n_steps=5)
    elif gender == "female":
        v = librosa.effects.pitch_shift(v, sr=sr, n_steps=-5)

    return v


# Load a speech wih librosa
my_file = input("please enter your file name: ")
voice, sr = librosa.load(my_file, sr=None, mono=False)
if voice.ndim > 1:
    voice = voice[0, :]

filepath = Path(my_file)

# a function that change the pitch of sound
changed_pitch_voice = pitchChanger(voice, sr, my_file)

# write final output
output_path = filepath.parent / (filepath.stem + "_pitch_changed" + filepath.suffix)
sf.write(str(output_path), changed_pitch_voice, sr)


plotPitch(my_file)
plotPitch(filepath.stem + "pitch_changed" + filepath.suffix)




