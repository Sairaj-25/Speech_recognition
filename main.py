# Speech recognition in python using google api

"""
To use this module - 
1] we have to install the SpeechRecognition module. 
2] There is another module called pyaudio (which is optional) Using this we can set different modes of audio.
"""

import speech_recognition as spreg

# setup sampling rate and the data size

sample_rate = 48000
data_size = 8192

recog = spreg.Recognizer()

recog.energy_threshold = 300
recog.dynamic_energy_threshold = True

with spreg.Microphone(sample_rate = sample_rate, chunk_size = data_size) as source:
    print("🎤 Calibrating microphone... Please wait") 
    recog.adjust_for_ambient_noise(source, duration=5)
    print("🎤 Tell Something (speak clearly):")
    speech = recog.listen(
        source,
        timeout=100,
        phrase_time_limit=100
    )

try:
    text = recog.recognize_google(speech, language="en-IN")
    print("You said: " + text)

except spreg.UnknownValueError:
    print('Unable to recognize the audio')
    
except spreg.RequestError as e:
    print("Request error from Google Speech Recognition service; {}".format(e))