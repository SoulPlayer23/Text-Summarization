import json
import fitz

class InputHandler:
    def read_file(self, file_path):
        if file_path.endswith('.json'):
            with open(file_path, 'r') as file:
                data = json.load(file)
                return ' '.join(data.get('Conversations', []))
        elif file_path.endswith('.txt'):
            with open(file_path, 'r') as file:
                return file.read()
        elif file_path.endswith('.pdf'):
            return self.read_pdf(file_path)
        else:
            raise ValueError("Unsupported file format")
    
    def read_pdf(self, file_path):
        doc = fitz.open(file_path)
        text = ""

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        
        return text