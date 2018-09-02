# stop words are words that are insignificant
# words like a, an, the, if etc.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = "This is an example showing off stop word filtration. I'm am the nicest person in the world, don't forget to mention that."
stop_words = set(stopwords.words("english"))
words = word_tokenize(example_text)

filtered_sentence = [n for n in words if n not in stop_words]

print(filtered_sentence)