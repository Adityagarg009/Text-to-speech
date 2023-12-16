from gtts import gTTS
import os

# Text to be converted to speech
text = "WOW Bots"

# Create a gTTS object
tts = gTTS(text=text, lang='en', slow=False)

# Save the generated speech to an audio file
tts.save("output.mp3")

# Play the generated audio file (requires a media player)
os.system("start output.mp3")


