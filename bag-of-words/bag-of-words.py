import numpy as np

def bag_of_words_vector(tokens, vocab):
    vector = np.zeros(len(vocab), dtype=int)

    for i, word in enumerate(vocab):
        count = 0
        for token in tokens:
            if token == word:
                count += 1
        vector[i] = count
    return vector