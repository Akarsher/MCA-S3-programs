#given text:The data set given satisfies the requirement for model generation.This is used in Data Science Lab

#1) perform word and sentence tokenization.
from nltk import word_tokenize, sent_tokenize

sent = "The data set given satisfies the requirement for model generation.\
This is used in Data Science Lab"
print("word and sentence tokenization")
print(word_tokenize(sent))
print(sent_tokenize(sent))
print()

#2) Remove the stop words from the given text
from nltk.corpus import stopwords
text = "The data set given satisfies the requirement for model generation. This is used in Data Science Lab"
stop_words = set(stopwords.words('english'))
tokens = word_tokenize(text.lower())

filtered = [word for word in tokens if word not in stop_words]
print("Stop words removed")
print("Original:", tokens)
print("Filtered:", filtered)
print()

#3) Perform Part of Speech tagging
from nltk import pos_tag

tokenized_text = word_tokenize(text)
tags = pos_tag(tokenized_text)
print("POS Tags:",tags)
print()

#4) create n-grams for different values of n=2,4.
from nltk import ngrams
print("N-grams :")
bigrams=list(ngrams(tokenized_text,2))
print("Bigrams : ",bigrams)

fourgrams=list(ngrams(tokenized_text,4))
print("Fourgrams : ",fourgrams)

