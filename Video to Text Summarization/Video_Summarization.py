# importing libraries
import speech_recognition as sr
import moviepy.editor as mp

# loading the video file
video_file = "/Users/aayushpuranik/.spyder-py3/dataset/isro_no_music.mp4"
clip = mp.VideoFileClip(video_file)
clip.audio.write_audiofile("/Users/aayushpuranik/.spyder-py3/dataset/isro_no_music.wav")

# speech recognition
r = sr.Recognizer()
audio = sr.AudioFile("/Users/aayushpuranik/.spyder-py3/dataset/isro_no_music.wav")

text = ''

try:
    with audio as source:
        for i in range(10):
            audio_file = r.record(source, duration=10, offset=None)
            converted = r.recognize_google(audio_file)
            print(converted)
            text += converted
except:
    print("No word detected in this duration, try changing offset and duration time")
    
print(text)

# summarize the article
