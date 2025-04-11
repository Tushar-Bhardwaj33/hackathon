import whisper
import sys
import io
import os

# Fix UnicodeEncodeError in Windows terminal
if os.name == 'nt':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load Whisper model
model = whisper.load_model("base")

# Transcribe the audio file
result = model.transcribe("output.wav")

# Save transcript to a text file
with open("transcript.txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        # print(segment["text"])       # Show in terminal
        f.write(segment["text"] + "\n")  # Write to file

# Confirmation message (no emoji to avoid encoding errors)
print("[✓] Transcript saved to 'transcript.txt' successfully!")
