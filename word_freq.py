def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w,0)+1
    return frequency