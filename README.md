# Erick Voice Assistant

## Overview
**Erick Voice Assistant** is a Python-based voice-activated assistant capable of performing various tasks such as playing music, telling the time and date, retrieving information from Wikipedia, and more. Erick listens for the wake word "Erick" and then responds to the user's instructions.

## Features
- **Play Music:** Instruct Erick to play a song from YouTube.
- **Tell Time:** Get the current time.
- **Tell Date:** Get today's date.
- **Answer Queries:** Ask Erick "Who is [Person/Entity]?" and receive a brief summary from Wikipedia.
- **Basic Conversations:** Erick can respond to simple questions like "How are you?" or "What is your name?"

## Requirements
Ensure the following Python libraries are installed:

- `speech_recognition`: For capturing and recognizing voice commands.
- `pyttsx3`: For converting text to speech.
- `pywhatkit`: For playing songs on YouTube.
- `wikipedia`: For retrieving information from Wikipedia.
- `datetime`: (Built-in) For retrieving current time and date.

You can install the required packages using pip:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia
