import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import keras
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, Normalizer
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import KFold
dataset = pd.read_csv("./humoment2.csv")
X = dataset.iloc[:,:6].values #5 vector ~ S1 -> S5
# X = dataset.iloc[:,:8].values #7 vector ~ S1 -> S7
y = dataset.iloc[:,6].values #5 vector ~ S1 -> S5
# y = dataset.iloc[:,8].values #7 vector ~ S1 -> S7
print(X)
print(y)
labelencoder_X_1 = LabelEncoder()
X[:,0] = labelencoder_X_1.fit_transform(X[:, 0])
print(X[:,0])
columnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [1])],     remainder='passthrough')
X=np.array(columnTransformer.fit_transform(X),dtype=np.str)
X = X[:, 1:]
kfold = KFold(n_splits=5, shuffle=True, random_state=10)
kf = kfold.get_n_splits(X)
for train, test in kfold.split(X, y):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
#train split 80%, test 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from keras.callbacks import TensorBoard

history_dict = {}
# TensorBoard Callback
cb = TensorBoard()

classifier = Sequential()
classifier.add(Dense(10, activation = 'relu')) #1 lớp ẩn sử dụng 10 neuron
# classifier.add(Dense(15, activation = 'relu')) #1 lớp ẩn sử dụng 15 neuron
classifier.add(Dense(1, activation = 'sigmoid')) #1 output layer
optimizer = keras.optimizers.SGD(lr=0.1)
classifier.compile(optimizer = optimizer, loss = 'binary_crossentropy', metrics = ['accuracy'])
history = classifier.fit(X_train, y_train, batch_size = 5, epochs = 50, verbose=0,
                                 validation_data=(X_test, y_test),
                                 callbacks=[cb])
y_pred = classifier.predict(X_test)
# y_pred = (y_pred > 0.5)
print(y_pred)
plt.plot(history.history['accuracy'], label='Train',c='green')
plt.plot(history.history['val_accuracy'], label='Test')
plt.title('Accuracy')
plt.legend()
plt.show()
plt.plot(history.history['loss'], label='Train',c='green')
plt.plot(history.history['val_loss'], label='Test')
plt.title('Loss')
plt.legend()
plt.show()
