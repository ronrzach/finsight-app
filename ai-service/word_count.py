with open("data/sample.txt") as f:
    text = f.read()
word_count = len(text.split())
print(f"sample.txt has {word_count} words")