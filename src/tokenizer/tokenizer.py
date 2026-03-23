import re

def preprocess(raw_text):
    split = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
    preprocessed = []
    for item in split:
        preprocessed.append(item.strip())
    return preprocessed


def create_vocabulary(file):
    with open("the-verdict.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()
    
    preprocessed = preprocess(raw_text)

    vocab = {  }
    index = 0

    for c in raw_text.split() :
        if (not c in vocab.values()):
            vocab[index] = c
            index+=1

    return vocab

    
def tokenize():
    vocab = create_vocabulary("the-verdict.txt")

    stop = 0
    for item in range(len(vocab)):
        print(vocab[item], ": ", item)
        stop+=1
        if (stop >= 50):
            break
