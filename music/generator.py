# music/generator.py
from pydub.generators import Sine
from pydub import AudioSegment

NOTE_FREQ = {
    'C': 261, 'D': 294, 'E': 329,
    'F': 349, 'G': 392, 'A': 440, 'B': 493
}

def melody_to_audio(melody):
    song = AudioSegment.silent(duration=0)
    for note in melody:
        freq = NOTE_FREQ.get(note, 440)
        tone = Sine(freq).to_audio_segment(duration=400)
        song += tone
    return song