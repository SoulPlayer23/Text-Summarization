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

- This project imports transformers from Hugging face and would require to cache tensors locally. So please allocate sufficient space in your disks.
