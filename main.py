from gtts import gTTS
import os
import platform

# Get user input
chatbotText = input("This will be the text the chatbot prints but not complete so we made it into input: ")

# Create a gTTS object
tts = gTTS(text = chatbotText, lang = 'en')

# Specify the filename for the audio file
audio_filename = "converted_text.mp3"

# Save the audio to a file
tts.save(audio_filename)

# Print a message to indicate success
print("Text converted successfully.")

# Check the platform (Windows or macOS/Linux)
if platform.system() == "Windows":
    # On Windows, you can use the default media player to play the audio
    os.system(f"start {audio_filename}")
elif platform.system() == "Darwin" or platform.system() == "Linux":
    # On macOS/Linux, you can use the default media player to play the audio
    os.system(f"xdg-open {audio_filename}")
else:
    print("Sorry, auto-play is not supported on your platform. You can manually open the audio file to listen to it.")