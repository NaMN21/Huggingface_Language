from transformers import pipeline

translatorce = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")   
  # Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-zh-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-zh-en")

# Use a pipeline as a high-level helper
from transformers import pipeline

translatorre = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ru-en")
from transformers import pipeline

translatorec = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-zh")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-ar-en")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-ar-en")
# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ar")
import streamlit as st
from transformers import pipeline
# Use a pipeline as a high-level helper
from transformers import pipeline

translatorer = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")   
  # Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ru")
# Initialize translation and grammar correction pipelines
translatorea = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-en-ar')
translatorae = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-ar-en')
grammar_corrector = pipeline('text2text-generation', model='onionLad/grammar-correction-t5-base')

# Title and input field
st.title("Language Translation & Grammar Correction")

input_text = st.text_area("Enter text:", value="", height=150)

# Dropdown for selecting task
task = st.selectbox("Choose a task", ["Translate", "Grammar Correction"])
lan4 = st.selectbox("from", ["Arabic", "English","Russian","Chinese"])
lan2 = st.selectbox("Choose a language", ["Arabic", "English","Russian","Chinese"])
# Button to process the input
if st.button("Submit"):
    if task == "Translate":
        if input_text.strip():
            # Call the translation pipeline
            if lan4 == "Arabic" and lan2 == "English":
                result = translatorae(input_text)
            elif lan4 == "English" and lan2 == "Arabic":
                result=translatorea(input_text)
            elif lan4 == "English" and lan2 == "Russian":
                result=translatorer(input_text)
            elif lan4 == "Russian" and lan2 == "English":
                result=translatorre(input_text)
            elif lan4 == "English" and lan2 == "Chinese":
                result = translatorec(input_text)
            elif lan4 == "Chinese" and lan2 == "English":
                result = translatorce(input_text)
            elif lan4 == "Arabic" and lan2 == "Chinese":
                result = translatorae(input_text)
                result = translatorec(result[0]['translation_text'])
            elif lan4 == "Chinese" and lan2 == "Arabic":
                result = translatorce(input_text)
                result = translatorea(result[0]['translation_text'])
            elif lan4 == "Chinese" and lan2 == "Russian":
                result = translatorce(input_text)
                result = translatorer(result[0]['translation_text'])
            elif lan4 == "Russian" and lan2 == "Chinese":
                result = translatorre(input_text)
                result = translatorec(result[0]['translation_text'])
            elif lan4 == "Arabic" and lan2 == "Russian":
                result = translatorae(input_text)
                result = translatorer(result[0]['translation_text'])
            elif lan4 == "Russian" and lan2 == "Arabic":
                result = translatorre(input_text)
                result = translatorea(result[0]['translation_text'])
                
        
            st.warning("Please enter some text to translate.")
            translated_text = result[0]['translation_text']
            st.write("Translated Text:", translated_text)

    elif task == "Grammar Correction":
        if input_text.strip():
            # Call the grammar correction pipeline
            result = grammar_corrector(input_text)
            corrected_text = result[0]['generated_text']
            st.write("Corrected Text:", corrected_text)
        else:
            st.warning("Please enter some text for grammar correction.")