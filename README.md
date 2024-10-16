# Text Summarization

## Introduction

This application will be able to summarize any text document, research paper, or conversation (JSON format). Here we are using Hugging Face transformers model (facebook/bart-large-cnn used here) to summarize the text input.

## Local Setup

1. Create virtual environment:
    ```bash
    python -m venv venv
    ```
2. Activate virtual environment:
    ```bash
    venv\Scripts\activate
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python src/app.py
    ```
5. Deactivate virtual environment:
    ```bash
    deactivate
    ```

## Note:

- This project could be done by importing a transformer model directly but we opted not to do that as it takes significant space for caching.
