# Working, Challenges and Improvement of Speech Translator

When you travel to a new unfamiliar place sometimes communication becomes tricky and problematic. You need a good translator for exchange of convesation. 
This, is the basic idea for creating Speech Translation. It lets you have easier exchange both via text and voice which has been implemented here.

Speech Translation is developed in three steps:
1. Recoding the speech: At first step user provides input for the message he wasnts to convey. It is recorded using SpeechRecognition library. Multiple API are inbuilt
but google module (recognize_google) is used here.
2. Translating to text: Second stage process the recorded audio into text. googletrans which is python package for neural machine translate of google is used.
Instead of googletrans we can also use TextBlob, which enables to perform operations on the text so obtained.
3. Text to Audio: Last stage is the conversion of text to audio. Here, we use pyttsx3 library for conversion. It gives us the option of selecting voice and accent 
i.e. the voice output of text in french is better implemented by french accent instead of german accent.

Challenges:
1. Although we are training the model using very powerful libraries, we often have to tune the background noise, time of audio and threshold for voice in this
2. It doesnot work on all the languages and cannot be used as universal translator. Although, it now include major languages but cannot convert every language.
3. This is not a real time speech translation system. Here, we record audio than translate and provide output which makes it slower.
4. If more than one person speak at a time, than detection becomes even difficult to catch and understand and translate. 

Improvements:
1. Here, we have one side conversion. We can extend it to record two audios and dual conversion from french to japanese and japanese to french.
2. Google translate does not support offline. So, instead we can use CMU Sphinx which does provide offline support, although it is not as accurate.
