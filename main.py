from pathlib import Path
import soundfile as sf
import pitch
import librosa

# Load our voice wih librosa
voice, sr = librosa.load("example.wav", sr=None, mono=False)
if voice.ndim > 1:
    voice = voice[0, :]

# a function that change the pitch of sound
changed_pitch_voice = pitchChanger(voice, sr)


# write final output 
filepath = Path("example.wav")
output_path = filepath.parent / (filepath.stem + "pitch_changed" + filepath.suffix)
sf.write(str(output_path), changed_pitch_voice, sr)


