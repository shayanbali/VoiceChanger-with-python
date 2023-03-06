import pitch
import librosa


voice, sr = librosa.load("example.wav", sr=None, mono=False)
if voice.ndim > 1:
    voice = voice[0, :]




