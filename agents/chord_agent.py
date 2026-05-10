# agents/chord_agent.py
CHORD_MAP = {
    'C': 'Cmaj',
    'D': 'Dm',
    'E': 'Em',
    'F': 'Fmaj',
    'G': 'Gmaj',
    'A': 'Am',
    'B': 'Bdim'
}

def generate_chords(melody):
    return [CHORD_MAP[note] for note in melody]