from gensim.models.word2vec import Word2Vec
model=Word2Vec()
model=model.wv.load("1.bin")
print(model.similarity("hack","decrypting"))
print(model.n_similarity(["fine","good"],["bad"]))