import matplotlib.pyplot as plt
''''''
def lexical_richness(text):
    if len(text) < 1:
        return 0
    return len(set(text)) / len(text)  
''''''
# def percentage(word, text):
#     return 100 * text.count(word) / len(text)

def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    import pylab
    word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

def displayWordFreq(freqDist, commons, human):
    
    freqDist = freqDist.most_common(commons)

    plt.figure(figsize=(10, 6))
    plt.bar(range(len(freqDist)), [count for word, count in freqDist], align='center')
    plt.xticks(range(len(freqDist)), [word for word, count in freqDist], rotation=90)
    # plt.bar(range(len(fdist_human)), [count for word, count in fdist_human.items()], align='center')
    # plt.xticks(range(len(fdist_human)), [word for word, count in fdist_human.items()], rotation=90)
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    if human==True:
        plt.title('Frequency Distribution of Human Variable')
    else:
        plt.title('Frequency Distribution of AI Variable')
    
    plt.show()  