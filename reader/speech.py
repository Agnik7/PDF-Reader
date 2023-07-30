from gtts import gTTS
import playsound

class Speech:

    def speech(self,text):
        """
        Speaks out the text provided

        Args: 
            text (string): The text to be spoken
        
        """
        
        tts = gTTS(text=text, lang='en', slow=False)
        audio_file = "output.mp3"
        tts.save(audio_file)
        playsound.playsound(audio_file)