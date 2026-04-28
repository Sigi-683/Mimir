from src.tokenizer.tokenizer import Tokenizer

t = Tokenizer("the-verdict.txt")

text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""

ids = t.encode(text)
print(ids)
print(len(ids))
print(t.decode(ids))

