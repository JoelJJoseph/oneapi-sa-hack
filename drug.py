import joblib
import pandas as pd
import re
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import streamlit as st
from PIL import Image

def app():
        
    tokenizer_path = 'medicine/model/count_vectorizer.pkl'
    model_path = 'medicine/model/pass_agg_model.pkl'
    data_path = 'medicine/data/drugsComTrain_raw.csv'

    vectorizer = joblib.load(tokenizer_path)
    model = joblib.load(model_path)
    dataset = pd.read_csv(data_path)

    stop = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()

    def clean_text(raw_review):
        review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
        letters_only = re.sub('[^a-zA-Z]', ' ', review_text)
        words = letters_only.lower().split()
        meaningful_words = [w for w in words if not w in stop]
        lemmitize_words = [lemmatizer.lemmatize(w) for w in meaningful_words]
        return ' '.join(lemmitize_words)

    def get_top_3_drugs(diagnosed_disease):
        df_top = dataset[(dataset['rating'] >= 9) & (dataset['usefulCount'] >= 100)].sort_values(by=['rating', 'usefulCount'], ascending=[False, False])
        drug_lst = df_top[df_top['condition'] == diagnosed_disease]['drugName'].head(3).tolist()
        return drug_lst

    st.title("Drug Review Predictor")

    image_path = "images/pain.jpg"
    image = Image.open(image_path)

    st.image(image)
    st.markdown("## Enter your problem:")

    raw_text = st.text_area("", "")

    if st.button("Predict"):
        if raw_text != "":
            cleaned_text = clean_text(raw_text)
            clean_lst = [cleaned_text]

            vectors = vectorizer.transform(clean_lst)
            prediction = model.predict(vectors)
            predicted_cond = prediction[0]
            top_drugs = get_top_3_drugs(predicted_cond)

            st.write("Diagnosed Condition: ", predicted_cond)
            st.write("Top 3 Recommended Drugs: ")
            for i, drug in enumerate(top_drugs, start=1):
                st.write(f"{i}. {drug}")
        else:
            st.write("There is no text to analyze.")

