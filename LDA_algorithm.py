from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import CountVectorizer

# Create a corpus of text documents
corpus = ['the quick brown fox', 'the lazy dog', 'the brown fox jumps', 'the dog sleeps']

# Create a CountVectorizer object to convert the text to a matrix of word counts
vectorizer = CountVectorizer()

# Convert the corpus to a matrix of word counts
X = vectorizer.fit_transform(corpus)

# Apply NMF to the count matrix to factorize it into non-negative components
nmf = NMF(n_components=2)
X_nmf = nmf.fit_transform(X)

print(X_nmf)