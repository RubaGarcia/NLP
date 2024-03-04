import math, collections

class LaplaceUnigramLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.unigramCounts = collections.defaultdict(lambda: 0) 
    self.words = set([]) # V value
    self.tokens = 0 # N value
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      for datum in sentence.data[1:-1]:
        token = datum.word
        self.words.add(token)
        self.unigramCounts[token] += 1
        self.tokens += 1

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    prob = 0.0

    for word in sentence[1:-1]:
      prob += math.log(self.probablility(word))

    return prob

  def probablility(self, word):
    return (self.unigramCounts[word] + 1) / (self.tokens + len(self.words))
