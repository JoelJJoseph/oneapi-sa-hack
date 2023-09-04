import streamlit as st
from multiapp import MultiApp
import home,drug,first
import base64
from PIL import Image
import keras
from PIL import Image, ImageOps
import numpy as np

app = MultiApp()

new_title = '<p style="font-family:sans-serif; color:White; font-size: 52px;"><b>MediCare</b></p>'
st.markdown(new_title, unsafe_allow_html=True)


# Add all your application here
app.add_app("⚕️MediCare", home.app)
app.add_app("💊Drug Recommendation",drug.app)
app.add_app("🚑First aid", first.app)

app.run()