# reference: https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/

from nltk.stem.wordnet import WordNetLemmatizer
import gensim
from gensim import corpora
import re
import json
from nltk.corpus import stopwords
import string
import csv

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def order(topicList):
    for i in range(len(topicList)-1):
        for j in range(len(topicList)-i-1):
            if topicList[j][1] < topicList[j+1][1]:
                topicList[j], topicList[j+1] = topicList[j+1], topicList[j]
    return topicList


def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

print('')
print('')
print('Read Twitter Data')
fname = 'data/collect_zika.json'

dates_zika = []


doc_complete = []
with open(fname, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('zika')]
        # track when the hashtag is mentioned
        # if '#zika' in terms_hash:
        #if 'zika' in terms_hash:
        doc_complete.append(tweet['text'])



stop = set(stopwords.words('english'))


exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]

# creating the term dictionary of our corpus, where very unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# LDA
Lda = gensim.models.ldamodel.LdaModel

# Running and Training LDA model on the document term matrix
ldamodel = Lda(doc_term_matrix, num_topics=7, id2word=dictionary, passes=50)

count = 0
topicList = []

for i in doc_term_matrix:
    topic_distr = ldamodel[i]

    topic_d = order(topic_distr)
    print(topic_d)
    topicList.append(topic_d)
    count += 1

with open('./data/topic.csv','w') as csvfile:
    fieldnames = ['index','topic']
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(topicList)):
        index = i
        topic = topicList[i][0][0]
        d = {'index':i, 'topic':topic}

        writer.writerow(d)
    csvfile.close()
print('#####################################################')
topicDetails = ldamodel.print_topics(num_topics=7, num_words=20)






