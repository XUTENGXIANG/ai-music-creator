# agents/melody_agent.py
import random

NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

def generate_melody(length=8):
    return [random.choice(NOTES) for _ in range(length)]