import subprocess

input_file = "demo.mp4"
output_file = "output.wav"

cmd = [
    "ffmpeg", "-i", input_file,
    "-ac", "1",  # mono audio
    "-ar", "16000",  # 16kHz sample rate
    "-acodec", "pcm_s16le",  # WAV format
    output_file
]

subprocess.run(cmd, check=True)
