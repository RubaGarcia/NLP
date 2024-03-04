import collections, math

class KneserNeyLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.unigramCounts = collections.defaultdict(lambda: 0) # c(w)
    self.bigramCounts = collections.defaultdict(lambda: 0) # c(w_i-1, w_i)
    self.nBigramCounts = set([]) # c(w, w')
    self.nPrevCounts = collections.defaultdict(lambda: set([])) # c(., w)
    self.nNextCounts = collections.defaultdict(lambda: set([])) # c(w, .)
    self.words = set([]) # V value
    self.tokens = [] # N value
    self.d=2
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model. 
        Compute any counts or other corpus statistics in this function.
    """  
    for sentence in corpus.corpus:
      token = sentence.data[0].word
      self.unigramCounts[token] += 1
      for datum in sentence.data[1:-1]:
        nextToken = datum.word
        self.unigramCounts[nextToken] += 1
        self.bigramCounts[(token, nextToken)] += 1
        self.nBigramCounts.add((token, nextToken))
        self.nPrevCounts[nextToken].add(token)
        self.nNextCounts[token].add(nextToken)
        self.words.add(nextToken)
        self.tokens.append(nextToken)
        token = nextToken
      nextToken = sentence.data[-1].word
      self.unigramCounts[nextToken] += 1
      self.bigramCounts[(token, nextToken)] += 1
      self.nBigramCounts.add((token, nextToken))
      self.nPrevCounts[nextToken].add(token)
      self.nNextCounts[token].add(nextToken)

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the 
        sentence using your language model. Use whatever data you computed in train() here.
    """
    prob = 0.0
    
    for i in range(1, len(sentence)):
      prev_word = sentence[i-1]
      word = sentence[i]
      prob += math.log(self.probability(word,prev_word))
    return prob
  
  def probability(self,word,prev_word):
    if self.numerator(word,prev_word) > 0:
      return self.numerator(word,prev_word)/self.unigramCounts[prev_word]
    else:
      return (self.unigramCounts[word] + 1)/(len(self.tokens) + len(self.words))
  
  def numerator(self,word,prev_word):
    return max(self.bigramCounts[(prev_word,word)] - self.d, 0) + self.d * len(self.nNextCounts[prev_word]) * len(self.nPrevCounts[word]) / len(self.nBigramCounts)
