"""
this part i need to learn 极大似然估计 
"""
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
mnist = fetch_openml('mnist_784' )
"""
mnist is a dataset with 60000 training samples and 10000 test samples.
It contains images of handwritten digits (0-9) represented as 28x28 pixel grayscale
"""
X, y = mnist['data'], mnist['target']
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

clf = LogisticRegression(penalty='l2', solver='saga', max_iter=10, random_state=42)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print("Accuracy:", accuracy)
