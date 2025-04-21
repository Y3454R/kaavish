import librosa
import numpy as np
from pydub import AudioSegment

NOTE_NAMES = ["S", "r", "R", "g", "G", "M", "M#", "P", "d", "D", "n", "N"]
# These are relative notes (from Sa) — using 12-tone for approximation


def hz_to_note(frequency, sa_freq):
    if frequency <= 0:
        return None
    ratio = frequency / sa_freq
    semitones = round(12 * np.log2(ratio)) % 12
    return NOTE_NAMES[semitones]


def extract_notes_from_audio(mp3_path, sa_freq=261.63):  # Sa = C4 (middle C)
    # Convert to wav
    sound = AudioSegment.from_mp3(mp3_path)
    wav_path = mp3_path.replace(".mp3", ".wav")
    sound.export(wav_path, format="wav")

    # Load with librosa
    y, sr = librosa.load(wav_path)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    detected_notes = set()

    for t in range(pitches.shape[1]):
        index = magnitudes[:, t].argmax()
        pitch = pitches[index, t]
        note = hz_to_note(pitch, sa_freq)
        if note:
            detected_notes.add(note)

    return sorted(detected_notes)
