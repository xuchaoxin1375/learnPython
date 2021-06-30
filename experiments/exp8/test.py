from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
corpus = [
    'This is the first document.',
    'This document is the second  aa bb cc.',
    'And this is the third one.',
    'Is this the first document?',
    
]
    
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())

# array=np.array(X)
print(type(X))#<class 'scipy.sparse.csr.csr_matrix'>

array=X.toarray()#get the corresponding ndarray
print(type(array))#ndarray

print(array)
print(X.shape)