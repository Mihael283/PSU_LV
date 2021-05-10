import numpy as np
from sklearn.datasets import fetch_openml
import joblib
import pickle
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix

X,y = fetch_openml('mnist_784', version=1,return_X_y=True,as_frame=False)

pixels = X[:1].reshape((28, 28))
plt.imshow(pixels, cmap='gray')
plt.show()

# skaliraj podatke, train/test split
X = X / 255.
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


# TODO: izgradite vlastitu mrezu pomocu sckitlearn MPLClassifier 
mlp = MLPClassifier(hidden_layer_sizes=(300,), max_iter=15, alpha=1e-4,solver='sgd', verbose=10, random_state=1, learning_rate_init=.1)
                        
mlp.fit(X_train,y_train)
# TODO: evaluirajte izgradenu mrezu
print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))

confusion_matrix(X_train, y_train)
confusion_matrix(X_test, y_test)
# spremi mrezu na disk
filename = "NN_model.sav"
joblib.dump(mlp, filename)

