import filecmp
import re
    
class Tokenizer:
    def __init__(self, file):
        # Represent a dictionary of tokens as key and index as value
        self.str_to_int = self.create_vocabulary(file)

        # Represent a dictionary of index as key and tokens as value
        # It's the same as above but with reversed keys / tokens
        self.int_to_str = {}
        for s,i in self.str_to_int.items():
            self.int_to_str[i] = s

    # Preprocessing
    def preprocess(self, raw_text):
        # Split into tokens according to the following regex
        split = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
        # Then strip each tokens
        return [item.strip() for item in split if item.strip()]

    # Vocabulary dictionary creation
    def create_vocabulary(self, file):
        # Open the file
        with open("the-verdict.txt", "r", encoding="utf-8") as f:
            raw_text = f.read()

        # Call to the preprocessing function
        preprocessed = self.preprocess(raw_text)

        # Sort each preprocessed token
        unique_tokens = sorted(list(set(preprocessed)))

        # Create a dictionary of each preprocessed tokens
        # The token is the key and an index is used as value
        vocab = {token: i for i, token in enumerate(unique_tokens)}
        return vocab

    # Main encoding function
    def encode(self, text):
        # Preprocess text
        preprocessed = self.preprocess(text)

        # Return an array of the vector representation of each token 
        encoded = []
        for s in preprocessed:
            encoded.append(self.str_to_int[s])
        return encoded

    # Main decoding function
    def decode(self, ids):

        res = ""
        if (len(res) > 0) :
            res += self.str_to_int[0]

        # Start from the second character
        for i in ids[1:] :
            # Get the token representation of the vector
            res += " " + self.int_to_str[i]

        res = re.sub(r'\s+([,.?!"()\'])', r'\1', res)
        return res
        
