import json
import random
import streamlit as st
import os
import pygame
import torch
from tts import Tacotron2
from tts.text import Language
from tts.speaker import Speaker

# Initialize pygame
pygame.mixer.init()

# Specify the absolute path to the intent.json file
intent_file_path = './intent.json'  # Replace with the actual path

# Load the intent.json file
with open(intent_file_path, 'r') as intent_file:
    intents = json.load(intent_file)

# Load the pretrained Tacotron2 model
tacotron2 = Tacotron2()
tacotron2.load("path/to/your/tacotron2/model")  # Replace with the actual model path

# Create a speaker with the language and voice you want
language = Language.from_file("path/to/your/language.json")  # Replace with language file
voice = Speaker(tacotron2, language)

# Function to recognize intent
def recognize_intent(user_input):
    user_input = user_input.lower()
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input:
                return intent
    return None

# Function to get a random response for an intent
def get_response(intent):
    responses = intent['responses']
    return random.choice(responses)

# Function to generate synthetic voice from text using Tacotron2 and play it using pygame
def text_to_audio(text):
    audio = voice.say(text)
    
    # Save the synthesized audio to a temporary file
    with open("synthesized_audio.wav", "wb") as audio_file:
        audio_file.write(audio.to_wav().to_buffer())
    
    # Play the synthesized audio using pygame
    pygame.mixer.music.load("synthesized_audio.wav")
    pygame.mixer.music.play()

# Streamlit UI
st.title("Voice Assistant Chatbot")

user_input = st.text_input("You (Voice):")

if st.button("Submit"):
    if user_input.lower() == 'exit':
        st.text("Bot: Goodbye!")
    else:
        try:
            matched_intent = recognize_intent(user_input)
            if matched_intent:
                response = get_response(matched_intent)
                st.text(f"Bot: {response}")
                text_to_audio(response)
            else:
                st.text("Bot: I'm sorry, I didn't understand that. Please ask another question.")

        except Exception as e:
            st.text(f"Bot: An error occurred: {str(e)}")
