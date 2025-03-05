# -*- coding: utf-8 -*-


import pickle

# Unpickle the file
with open(r"C:\Users\HP\Desktop\face Detection\face Detection\data\images.p", "rb") as f:
  images = pickle.load(f)

with open(r"C:\Users\HP\Desktop\face Detection\face Detection\data\labels.p", "rb") as f:
  labels = pickle.load(f)

print(images.shape)
print(labels.shape)

set(labels)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = le.fit_transform(labels)

set(labels)

import numpy as np
n_persons = len(set(labels))
print("Number of persons: ", n_persons)
label_mapping = le.inverse_transform(np.arange(n_persons))
for i in range(len(label_mapping)):
  print(i, "-->", label_mapping[i])

import matplotlib.pyplot as plt

plt.imshow(images[1], cmap=plt.get_cmap("gray"))
plt.show()

import cv2
def preprocessing(img):
  img = cv2.equalizeHist(img)
  img = img.reshape(100, 100, 1)
  img = img/255
  return img

images = np.array(list(map(preprocessing, images)))
print("Shape of Input: ", images.shape)

from tensorflow.keras.utils import to_categorical

labels = to_categorical(labels)

categories = labels.shape[1]
print(categories)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
# import convolution layer
from tensorflow.keras.layers import Conv2D
# import pooling layer
from tensorflow.keras.layers import MaxPooling2D
# import faltten layer
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import RMSprop

from tensorflow.keras.layers import BatchNormalization
from keras.layers import Dense,Dropout

model = Sequential()
model.add(Conv2D(32, (3,3), input_shape=(100, 100, 1), activation="relu"))
model.add(Conv2D(32, (5,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(64, (5,3), activation="relu"))
model.add(Conv2D(64, (4,3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(4096, activation="relu"))

model.add(Dense(4, activation="softmax"))
model.compile(RMSprop(learning_rate=0.0001), loss="categorical_crossentropy", metrics=['accuracy'])

model.summary()

h=model.fit(images,labels,validation_split=0.02,batch_size=50,epochs=10,verbose=1)



model.save('fac.h5')

help('keywords')

