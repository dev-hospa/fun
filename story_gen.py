import streamlit as st
import openai

st.title('JOKE GENERATOR')
st.subheader('Keep smiling!')

title = st.text_input('Tell me a joke about...', key="text")
prompt = (f"Tell me a joke about {title}")

openai.api_key = st.secrets["AI_TOKEN"]
if title:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.4,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    st.markdown(body=response.choices[0].text)

