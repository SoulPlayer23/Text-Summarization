from summarizer import Summarizer
from input_handler import InputHandler

def main(file_path):
    input_handler = InputHandler()
    summarizer = Summarizer()

    text = input_handler.read_file(file_path)
    summary_type = input("Do you want a detailed or short summary? (Enter 'detailed' or 'short'): ").strip().lower()
    summary = summarizer.summarize(text, summary_type)

    print("Summary: \n", summary)

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    main(file_path)
