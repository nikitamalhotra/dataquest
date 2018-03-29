import read
from collections import Counter

df = read.load_data()
headlines = [str(headline) for headline in df['headline'].tolist()]
headline_string = ' '.join(headlines)
words = [word.lower() for word in headline_string.split()]
c = Counter(words)

for word, count in c.most_common(100):
    print(word + ': ' + str(count)) 
