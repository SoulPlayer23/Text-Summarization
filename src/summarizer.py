from transformers import BartTokenizer, BartForConditionalGeneration

class Summarizer:
    def __init__(self):
        self.model_name = "facebook/bart-large-cnn"
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name)

    def summarize(self, text, summary_type="short"):
        if summary_type == "detailed":
            max_len = 300
            min_len = 100
        else:
            max_len = 150
            min_len = 50
        inputs = self.tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(inputs['input_ids'], max_length=max_len, min_length=min_len, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary










# import requests

# def set_model(text_type):
#     model_mapping = {
#         "paragraph": "facebook/bart-large-cnn",  # Good for short summaries
#         "article": "google/pegasus-xsum",       # Suitable for articles
#         "research_paper": "facebook/bart-large", # Good for longer documents
#         "conversation": "microsoft/DialoGPT-small" # Suitable for conversations
#     }
#     return model_mapping.get(text_type, "facebook/bart-large-cnn")  # Default to BART if type not recognized

# def summarize(text, text_type):
#     model = set_model(text_type)
#     print("Model used: ", model)
#     api_url = f"https://api-inference.huggingface.co/models/{model}"
#     headers = {"Authorization": f"Bearer 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"}
#     payload = {"inputs": text}

#     response = requests.post(api_url, headers=headers, json=payload)

#     if response.status_code == 200:
#         summary = response.json()[0]['summary_text']
#         return summary
#     else:
#         return f"Error: {response.status_code}, {response.text}"
