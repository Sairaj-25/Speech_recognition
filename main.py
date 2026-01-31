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

# Better defaults
recog.energy_threshold = 400
recog.dynamic_energy_threshold = True
recog.pause_threshold = 0.8       # pause before sentence ends
recog.non_speaking_duration = 0.5


def recognize_speech():
    with spreg.Microphone() as source:
        
        recog.adjust_for_ambient_noise(source, duration=1)
        
        speech = recog.listen(
            source,
            timeout=7, # it will stop listening after pause of 7 sec !
            phrase_time_limit=20 # It is the maximum duration to take input from user
        )

    try:
        text = recog.recognize_google(speech, language="en-IN", show_all =False)
        print(f"You said: {text}")
        return f"You said: {text}"

    except spreg.UnknownValueError:
        print('Unable to recognize the audio')
        return "Unable to recognize the audio"
    
    except spreg.RequestError as e:
        print("Request error from Google Speech Recognition service; {}".format(e))
        return "Request error from Google Speech Recognition service; {}".format(e)



# Button 
if st.button("Speak 🎤"):
    # st.info("Listening...🎧 ") # This button is still visible after result show so dont use it !
    
    with st.spinner("🎧 Listening..."):
        st.subheader("Recognized Text 📝 :")
        result = recognize_speech()
        st.write(result)