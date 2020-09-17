#importing libraries
import speech_recognition as sr
import googletrans as t
import pyttsx3

# define recognizer, translator, engine
r = sr.Recognizer()
p = t.Translator()
engine = pyttsx3.init()

# setting the mic 
print(sr.Microphone().list_microphone_names())
mic = sr.Microphone(device_index=0)

# setting output voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[32].id)
#engine.setProperty('language', 'hi')

# recording the audio
def recording_audio(mic, recognizer):
    print("Listening...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
    return audio

# loading translator
def translate(translator, text, to_language='en'):
    k = translator.translate(text, dest=to_language)
    translated = str(k.text)
    return translated

# text to speech
def text_to_speech(engine, text):
    engine.say(text)
    engine.runAndWait()

# target language
text_language = 'hi'
voice_language = 'hi'

translated_text = "Welcome Sir!"
while True:
    text_to_speech(engine, translated_text)
    try:
        audio = recording_audio(mic, r)
        result = r.recognize_google(audio, language='en')
        translated_text = translate(p, result, text_language)
        print(translated_text)
        if "bye" in translated_text:
            translated_text = "Okay, GoodBye"
            break
    except:
        translated_text = "Sorry, I didn't understood"
text_to_speech(engine, translated_text)
