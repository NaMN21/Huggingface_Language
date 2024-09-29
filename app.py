# Initialize translation and grammar correction pipelines
from transformers import pipeline
import streamlit as st
#translatorer = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")  
#translatorre = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
#translatorce = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")   
#translatorec = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
#translatorea = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-en-ar')
#translatorae = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-ar-en')


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
                translatorae = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-ar-en')
                result = translatorae(input_text)


            elif lan4 == "English" and lan2 == "Arabic":
                translatorea = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-en-ar')
                result=translatorea(input_text)


            elif lan4 == "English" and lan2 == "Russian":
                translatorer = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")
                result=translatorer(input_text)


            elif lan4 == "Russian" and lan2 == "English":
                translatorre = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
                result=translatorre(input_text)


            elif lan4 == "English" and lan2 == "Chinese":
                translatorec = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
                result = translatorec(input_text)


            elif lan4 == "Chinese" and lan2 == "English":
                translatorce = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
                result = translatorce(input_text)


            elif lan4 == "Arabic" and lan2 == "Chinese":
                translatorae = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-ar-en')
                translatorec = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
                result = translatorae(input_text)
                result = translatorec(result[0]['translation_text'])


            elif lan4 == "Chinese" and lan2 == "Arabic":
                translatorce = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en") 
                translatorea = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-en-ar')
                result = translatorce(input_text)
                result = translatorea(result[0]['translation_text'])


            elif lan4 == "Chinese" and lan2 == "Russian":
                translatorce = pipeline("translation", model="Helsinki-NLP/opus-mt-zh-en")
                translatorer = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru") 
                result = translatorce(input_text)
                result = translatorer(result[0]['translation_text'])


            elif lan4 == "Russian" and lan2 == "Chinese":
                translatorre = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
                translatorec = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
                result = translatorre(input_text)
                result = translatorec(result[0]['translation_text'])


            elif lan4 == "Arabic" and lan2 == "Russian":
                translatorae = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-ar-en')
                translatorer = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru") 
                result = translatorae(input_text)
                result = translatorer(result[0]['translation_text'])


            elif lan4 == "Russian" and lan2 == "Arabic":
                translatorre = pipeline("translation", model="Helsinki-NLP/opus-mt-ru-en")
                translatorea = pipeline('translation_en_to_ar', model='Helsinki-NLP/opus-mt-en-ar')
                result = translatorre(input_text)
                result = translatorea(result[0]['translation_text'])

                
            else:
                st.warning("Please enter some text to translate.")
        
            
            translated_text = result[0]['translation_text']
            st.write("Translated Text:", translated_text)

    elif task == "Grammar Correction":
        # grammar_corrector = pipeline('text2text-generation', model='onionLad/grammar-correction-t5-base')
        # Load model directly
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        tokenizer = AutoTokenizer.from_pretrained("onionLad/grammar-correction-t5-base")
        grammar_corrector = AutoModelForSeq2SeqLM.from_pretrained("onionLad/grammar-correction-t5-base")        
        if input_text.strip():
    # Tokenize the input text
            inputs = tokenizer(input_text, return_tensors="pt")

            # Call the grammar correction model
            outputs = grammar_corrector.generate(**inputs)

            # Decode the output tokens to get the corrected text
            corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Display the corrected text
            st.write("Corrected Text:", corrected_text)       
        else:
            st.warning("Please enter some text for grammar correction.")
