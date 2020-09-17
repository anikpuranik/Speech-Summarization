Video to Text Summarization has interesting application in creating sports match highlights, summary of a video lecture, topic identification of news.
This project invloves 3 basic steps:
1. Conversion of video to audio : The conversion of video to text is very difficult as comapred to that of audio. The converison of image to text exist but 
for the number of frames present in video the task would very hugh amount of time and is not recommeded. While, working with video saves lot of time and nearly same
information can be obtained using audio.
2. Audio to Text : The audio on itself cannot be processed and we need to convert to text. Conversion of audio to text is covered below here, so we will just use 
the pre-trained google library for the conversion of audio to text.

https://github.com/anikpuranik/Voice-to-Text/tree/master/Techniques%20for%20audio%20to%20text
3. Summarization of Text : Summarization of an article is the final step in this process. Mainly, Summarization is the part of Natural Language Processing which is 
covered by the below link, so we are going to use direct function for summarization of text.

https://github.com/anikpuranik/Natural-Language-Processing/tree/master/Text%20Summarization

Challenges:
1. While the video can be converted to audio, the complete audio for longer length is difficult to convert. Thus, we break the text into different parts of audio
and than translate the text. Here, in this we have choose the size of 30 seconds.
2. Since the audio is broken, if we break the audio at the point of conversation, the system break the voice and the word predicted is mostly incorrect.
So, the point of breaking the word is of importance.
3. The conversion of file must be in the wav format. For other format, python does not allow. So, the conversion of large files may take time.
