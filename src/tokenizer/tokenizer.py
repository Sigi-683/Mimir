import re
    
class Tokenizer:
    def __init__(self, file):
        self.str_to_int = self.create_vocabulary(file)
        self.int_to_str = {}
        for s,i in self.str_to_int.items():
            self.int_to_str[i] = s

    def preprocess(self, raw_text):
        split = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
        return [item.strip() for item in split if item.strip()]

    def create_vocabulary(self, file):
        with open("the-verdict.txt", "r", encoding="utf-8") as f:
            raw_text = f.read()

        preprocessed = self.preprocess(raw_text)

        unique_tokens = sorted(list(set(preprocessed)))

        vocab = {token: i for i, token in enumerate(unique_tokens)}
        return vocab

    def encode(self, text):
        preprocessed = self.preprocess(text)
        encoded = []
        for s in preprocessed:
            encoded.append(self.str_to_int[s])
        return encoded
