import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
# stop_words = stopwords.words('vietnamese')


stop_words = ViStopWords()

text = "Đây là một ví dụ về cách xóa stop word trong dữ liệu tiếng Việt"
words = text.split()
filtered_words = [word for word in words if word.lower() not in stop_words]

print(filtered_words)