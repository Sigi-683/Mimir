from tokenizer import Tokenizer

t = Tokenizer("the-verdict.txt")

text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""

ids = t.encode(text)
print(len(ids))
print(ids == [1, 56, 2, 850, 988, 602, 533, 746, 5, 1126, 596, 5, 1, 67, 7, 38, 851, 1108, 754, 793, 7])
print(t.decode(ids) == " It' s the last he painted, you know,\" Mrs. Gisburn said with pardonable pride.")
