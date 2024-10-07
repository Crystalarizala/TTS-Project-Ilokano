# Bidirectional Natural Language Processing for Cross-Linguistic Text-to-Speech Generation in the Tagalog-Ilocano Language

## Overview
This project aims to enhance the text-to-speech (TTS) system for low-resourced languages, specifically focusing on the Tagalog and Ilocano languages. The proposed method utilizes bidirectional natural language processing techniques to improve the generation of synthetic speech for these languages.

## Objective
The main objective of this research is to develop a TTS model that can generate high-quality speech for Ilocano, leveraging textual-only data. By doing so, we aim to address the challenges faced by low-resourced languages in the field of speech synthesis.

## Methodology
- Data Collection: Collect paired audio and text data for Tagalog and Ilocano.
- Preprocessing: Align audio and text, and convert audio into a suitable format for training.
- Model Trainin Train the TTS model using textual-only data for Ilocano, adapting the framework to accommodate the unique characteristics of low-resourced languages.
- Evaluation Metrics: Evaluate the model's performance using metrics such as Mel-Cepstral Distortion (MCD) and Character Error Rate (CER).

## Metrics
- Character Error Rate (CER): Measures the accuracy of the synthesized speech compared to the original text.
- Mel-Cepstral Distortion (MCD): Evaluates the quality of the synthesized audio.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/crystalarizala/TTS-Framework.git
   cd TTS-Framework
