#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pyttsx3",
# ]
# ///

import sys
import pyttsx3

def main():
    if len(sys.argv) < 2:
        print("Usage: pyttsx3_tts.py <text_to_speak>", file=sys.stderr)
        sys.exit(1)
    
    text = " ".join(sys.argv[1:])
    
    try:
        engine = pyttsx3.init()
        
        # Set properties for more dramatic delivery
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate + 50)  # Slightly faster for drama
        
        volume = engine.getProperty('volume')
        engine.setProperty('volume', 1.0)  # Maximum volume
        
        # Say the text
        engine.say(text)
        engine.runAndWait()
        
    except Exception as e:
        # Fail silently - TTS is optional
        pass

if __name__ == "__main__":
    main()