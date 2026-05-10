# app.py
import streamlit as st
from agents.melody_agent import generate_melody
from agents.chord_agent import generate_chords
from agents.style_agent import apply_style
from music.generator import melody_to_audio

st.title("🎵 AI Music Creator")

style = st.selectbox("选择风格", ["happy", "sad", "normal"])

if st.button("生成音乐"):
    melody = generate_melody()
    melody = apply_style(melody, style)
    chords = generate_chords(melody)

    st.write("🎼 Melody:", melody)
    st.write("🎹 Chords:", chords)

    audio = melody_to_audio(melody)
    audio.export("output.wav", format="wav")

    st.audio("output.wav")