# Text to Speech (TTS) Translation

This script translates English sentences into multiple languages, and uses Text to Speech (TTS) technology to convert them into audio files.

# Workflow

The script reads an input file English_Sentences.txt containing English sentences. It then iterates over each sentence, converts it to the specified target languages (Chinese, German, and Japanese), and generates TTS mp3 files for each translated sentence. It then pauses for a specific duration of time, proportional to the length of the translated sentence, before moving on to the next sentence.

# Execution

The script can be executed by running it in a Python environment with the required libraries installed. The input file English_Sentences.txt should be present in the same directory as the script. The output mp3 files will also be saved in the same directory.