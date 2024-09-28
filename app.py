import streamlit as st
from transformers import pipeline

# Initialize translation and grammar correction pipelines
translator = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-en-ar')
grammar_corrector = pipeline('text2text-generation', model='onionLad/grammar-correction-t5-base')

# Title and input field
st.title("Language Translation & Grammar Correction")

input_text = st.text_area("Enter text:", value="", height=150)

# Dropdown for selecting task
task = st.selectbox("Choose a task", ["Translate", "Grammar Correction"])

# Button to process the input
if st.button("Submit"):
    if task == "Translate":
        if input_text.strip():
            # Call the translation pipeline
            result = translator(input_text)
            translated_text = result[0]['translation_text']
            st.write("Translated Text:", translated_text)
        else:
            st.warning("Please enter some text to translate.")
    elif task == "Grammar Correction":
        if input_text.strip():
            # Call the grammar correction pipeline
            result = grammar_corrector(input_text)
            corrected_text = result[0]['generated_text']
            st.write("Corrected Text:", corrected_text)
        else:
            st.warning("Please enter some text for grammar correction.")
