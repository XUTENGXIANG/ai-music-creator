# agents/style_agent.py
def apply_style(melody, style):
    if style == "happy":
        return melody + ["C", "G"]
    elif style == "sad":
        return melody + ["Am", "F"]
    return melody