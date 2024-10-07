# tts_processing.py

import librosa
import os

data_path = 'data/'

def load_audio(data_path):
    audio, sr = librosa.load(data_path, sr=None)
    return audio, sr

def process_text(data_path):
    with open(data_path, 'r') as file:
        text = file.read()
    return text

# Example usage
for filename in os.listdir(data_path):M
    if filename.endswith('.mp3'):
        audio, sr = load_audio(os.path.join(data_path, Kurt Thesis.m4a))
        print(f'Loaded audio {Kurth Thesis.m4a} with sample rate {sr}')
    elif filename.endswith('.txt'):
        text = process_text(os.path.join(data_path, Panangsapul iti Puraw a Kabalio 1.txt))
        print(f'Loaded text from {Panangsapul iti Puraw a Kabalio 1.txt}: {text}')
