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