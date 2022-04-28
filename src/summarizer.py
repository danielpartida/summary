# https://huggingface.co/tasks/summarization
# https://huggingface.co/docs/transformers/tasks/summarization
# https://huggingface.co/course/chapter7/5?fw=pt

from transformers import pipeline

classifier = pipeline("summarization")

file = open("../text/crypto_com_processed.txt", "r", encoding='mbcs')
text = file.read()

summary = classifier(text)
print(summary)
