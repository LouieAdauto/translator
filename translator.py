import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./credentials.json"
import speech_recognition as recon
    # Library to recognize the speech through the microphone of out computers
from langdetect import detect
    # Library useful to detect the language the person is speaking in
from google_trans_new import google_translator
from deep_translator import GoogleTranslator
    # Official library from google API to translate several languages for free (it has a limit tho)
import pyttsx3    

# Let us instantiate the speech recognizer
recognizer = recon.Recognizer()
# Instantiate translator
translator = google_translator()
# Instantiate tts
tts = pyttsx3.init()

while True:
    with recon.Microphone() as source:
        print("Empieza a hablar por favor")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(text)
            input_language = detect(text)
            print(f"Detected Language: {input_language}")
            if input_language == "es":
                translation = GoogleTranslator(source='auto', target='en').translate(text=text)
                print(f"Translated to english: {translation}")
                tts.say(translation)
                tts.runAndWait()
            elif input_language == "en":
                translation = GoogleTranslator(source='auto', target='es').translate(text=text)
                print(f"Translated to spanish: {translation}")
                tts.say(translation)
                tts.runAndWait()
            else:
                print("I don't know that language, sorry")
        except recon.UnknownValueError:
            print("Google Speech recognition API could not identify the language")
        except recon.RequestError as error:
            print(f"There was a Request Error from the Google API server: {error}")







