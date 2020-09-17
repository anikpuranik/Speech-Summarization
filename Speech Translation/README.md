When you travel to a new unfamiliar place sometimes communication becomes tricky and problematic. You need a good translator for exchange of convesation. 
This, is the basic idea for creating Speech Translation. It lets you have easier exchange both via text and voice which has been implemented here.

Speech Translation is developed in three steps:
1. Recoding the speech: At first step user provides input for the message he wasnts to convey. It is recorded using SpeechRecognition library. Multiple API are inbuilt
but google module (recognize_google) is used here.
2. Translating to text: Second stage process the recorded audio into text. googletrans which is python package for neural machine translate of google is used.
Instead of googletrans we can also use TextBlob, which enables to perform operations on the text so obtained.
3. Text to Audio: Last stage is the conversion of text to audio. Here, we use pyttsx3 library for conversion. It gives us the option of selecting voice and accent 
i.e. the voice output of text in french is better implemented by french accent instead of german accent.
