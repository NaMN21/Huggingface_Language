# Language Translation & Grammar Correction App

This is a Streamlit application for language translation and grammar correction using Hugging Face's Transformers library. The app allows users to translate text between multiple languages and correct grammar in English sentences.

## Features

- Translate text between Arabic, English, Russian, and Chinese.
- Correct grammatical errors in English text.
- User-friendly interface with dropdown menus for language selection.

## Technologies Used

- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)
- [ngrok](https://ngrok.com/) (for tunneling)

## Requirements

To run this application, you need to install the required packages. You can do this by running:

```bash
pip install -r requirements.txt
```
## How to Run

    Clone the repository:

```bash

git clone https://github.com/NaMN21/Huggingface_Language.git
cd Huggingface_Language
```
## Run the Streamlit app:

```bash

streamlit run app.py
```
## If using ngrok, start ngrok to tunnel the app:

```bash

    ngrok http 8501
```
Access the app using the provided ngrok URL.

## Usage

    Enter text in the input field.
    Select the task (Translation or Grammar Correction).
    Choose the source and target languages for translation.
    Click the "Submit" button to see the results.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License 
