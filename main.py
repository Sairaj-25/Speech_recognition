# Speech recognition in python using google api

"""
To use this module - 
1] we have to install the SpeechRecognition module. 
2] There is another module called pyaudio (which is optional) Using this we can set different modes of audio.
"""

import speech_recognition as spreg
import streamlit as st


st.set_page_config(page_title='Speech Recognition', page_icon='🎤')
st.title("Speech Recognition app")
st.write("Click the button and speak. Your voice will be converted to text.")

recog = spreg.Recognizer()

recog.energy_threshold = 300
recog.dynamic_energy_threshold = True


def recognize_speech():
    with spreg.Microphone() as source:
        print("🎤 Calibrating microphone... Please wait") 
        recog.adjust_for_ambient_noise(source, duration=0)
        print("🎤 Tell Something (speak clearly):")
        speech = recog.listen(
            source,
            timeout=5,
            phrase_time_limit=7
        )

    try:
        text = recog.recognize_google(speech, language="en-IN")
        print("you said: ",text)
        return "You said: ",text

    except spreg.UnknownValueError:
        print('Unable to recognize the audio')
        return "Unable to recognize the audio"
    
    except spreg.RequestError as e:
        print("Request error from Google Speech Recognition service; {}".format(e))
        return "Request error from Google Speech Recognition service; {}".format(e)



# Button 
if st.button("Click & Speak"):
    result = recognize_speech()
    st.subheader("📝 Recognized Text:")
    st.write(result)