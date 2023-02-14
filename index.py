import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('audio.wav') as source:
    audio = r.record(source)

try:
    text = r.recognize_google(audio, language='fa-IR')
    print(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
