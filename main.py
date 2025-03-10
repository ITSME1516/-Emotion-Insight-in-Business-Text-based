import streamlit as st 
import pickle as pkl
import base64

with open("model.pkl","rb") as file:
    model = pkl.load(file)

st.title("Emotion Insight in Business (Text-based)")

st.write("""
This project, "Emotion Insight," aims to leverage machine learning to detect emotions from text data such as customer reviews, emails, and social media posts. The goal is to utilize this technology to enhance business intelligence across different sectors. By understanding the emotional states of customers, employees, and users, businesses can make more informed decisions and improve their services.
""")

color = dict(zip(['fear', 'sad', 'love', 'joy', 'suprise', 'anger'], [["800080","😨"], ["0000FF","🥺"], ["FF0000", "💘"], ["FFFF00","😃"] ,["FFA500", "🤯"] ,["8B0000","😡"]]))

msg = st.text_area("Enter Message:")

a,b,c = st.columns([3.5,2,3.5])

if b.button("Predict",type="primary"):
    op = model.predict([msg])[0]
    c1,c2,c3 = st.columns([1,8,1])
    file_ = open(f"gifs//{op}.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    c2.markdown(f"<b><p style='font-size:50px;text-align: center;color: #{color[op][0]}'>{op} {color[op][1]}</p></b>", unsafe_allow_html=True)
    c2.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="gif" style="width:70vh;border-radius: 50%; border: 5px solid #{color[op][0]};">', unsafe_allow_html=True)
    
st.divider()
st.write("Sample Data:")
st.write("""
- **Fear:** She felt scared when the lights went out suddenly.

- **Sad:** He was sad when his ice cream fell on the ground.

- **Love:** She loved playing with her puppy.

- **Joy:** He was very happy when he got a new toy.

- **Surprise:** She was surprised when her friends threw a party for her.

- **Anger:** He was angry when someone broke his favorite toy.
         """)