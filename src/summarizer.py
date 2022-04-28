from transformers import pipeline

classifier = pipeline("summarization")

file = open("../text/crypto_com_processed.txt", "r")
text = file.read()
print(text)
