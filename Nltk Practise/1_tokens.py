from nltk.tokenize import word_tokenize, sent_tokenize

example_text = "Hello there Mr. Smith, how are you today. You shouldn't eat cardboard."

for sentence in sent_tokenize(example_text):
    print(sentence)

for word in word_tokenize(example_text):
    print(word)
