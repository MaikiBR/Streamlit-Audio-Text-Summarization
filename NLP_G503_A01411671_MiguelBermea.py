import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="APIKEY")


def transcribe_audio(file_path):
  with open(file_path, "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      response_format="text"
    )
  return transcript


def CustomChatGPT(temperature, user_input):
  response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      temperature=temperature,
      messages=[{
          "role": "system",
          "content": "You are an office administer, summarize the text in key points"
      }, {
          "role": "user",
          "content": user_input
      }])
  return response.choices[0].message.content


# Interfaz de Streamlit
st.title('Transcripción y Resumen de Voz')
st.header('Miguel Ángel Bermea Rodríguez | A01411671', divider='rainbow')
uploaded_file = st.file_uploader("Elige un archivo de audio", type=['m4a'])

if uploaded_file is not None:
  file_path = uploaded_file.name
  transcription = transcribe_audio(file_path)
  st.subheader('Transcripción:', divider='rainbow')
  st.write(transcription)
  summary = CustomChatGPT(0, transcription)
  st.subheader('Resumen:', divider='rainbow')
  st.write(summary)
