from pathlib import Path

import parselmouth
import soundfile as sf
import pitch
import librosa
import numpy as np


def genderRecgnition(file_path):
    # Load a speech file and extract its pitch contour
    file_path = file_path
    snd = parselmouth.Sound(file_path)
    pitch = snd.to_pitch()

    # Calculate some basic statistics of the pitch contour
    mean_pitch = np.mean(pitch.selected_array['frequency'])
    median_pitch = np.median(pitch.selected_array['frequency'])
    pitch_range = np.max(pitch.selected_array['frequency']) - np.min(pitch.selected_array['frequency'])

    # Use the statistics to predict the gender of the speaker
    if mean_pitch > 150 and pitch_range > 50:
        predicted_gender = 'female'
    elif mean_pitch < 150 and pitch_range > 50:
        predicted_gender = 'male'
    else:
        predicted_gender = 'unknown'

    print('Predicted gender:', predicted_gender)


def pitchChanger(v, sr, filepath1):
    v_third = librosa.effects.pitch_shift(v, sr=sr, n_steps=1, bins_per_octave=2)
    genderRecgnition(filepath1)

    return v_third


# Load our voice wih librosa
voice, sr = librosa.load("example.wav", sr=None, mono=False)
if voice.ndim > 1:
    voice = voice[0, :]

filepath = Path("example.wav")

# a function that change the pitch of sound
changed_pitch_voice = pitchChanger(voice, sr, "example.wav")

# write final output
output_path = filepath.parent / (filepath.stem + "pitch_changed" + filepath.suffix)
sf.write(str(output_path), changed_pitch_voice, sr)
