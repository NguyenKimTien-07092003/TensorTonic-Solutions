import numpy as np

def bag_of_words_vector(tokens, vocab):
    # Tạo dict để lookup index O(1) thay vì dùng .index() O(n)
    vocab_index = {word: i for i, word in enumerate(vocab)}
    
    vector = np.zeros(len(vocab), dtype=int)
    
    for token in tokens:
        if token in vocab_index:
            vector[vocab_index[token]] += 1
    
    return vector