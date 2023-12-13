"""
==================================================
Neural Networks for Classification - Clothes
==================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

+-----------------------------------------------------------------------+

Python at least 3.8
To run the program, install the following Python packages (if required):
TensorFlow with some packages which should be imported in the code:
- fashion_mnist dataset
Keras library in Python:
- Flatten, Dense
- Sequential model

+-----------------------------------------------------------------------+
TERMINOLOGY

Neural networks are computational systems inspired by the structure and function of the human brain.
They are comprised of interconnected nodes known as neurons, organized into layers.
Each neuron processes input data and transmits signals to neurons in the next layer.
Neural networks learn by adjusting connections between neurons based on example data.

In the provided example, we analyze photos of clothing. This code illustrates the entire pipeline of training a neural
network, evaluating its performance, visualizing the confusion matrix, and making predictions for
specific records in the Fashion-MNIST dataset.
The model is trained using the Adam optimizer and categorical crossentropy as the loss function.

"""
from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.src.layers import Dropout

from methods import *

# load data
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# map class to real names
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# prepare model A and learn
model_A = Sequential()
model_A.add(Flatten(input_shape=(28, 28)))
model_A.add(Dense(128, activation='relu'))
model_A.add(Dense(10, activation='softmax'))

# compile model A
model_A.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# fitting model A
model_A.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=128, verbose=1)

# prepare model B and learn
model_B = Sequential()
model_B.add(Flatten(input_shape=(28, 28)))
model_B.add(Dense(256, activation='relu'))
model_B.add(Dense(128, activation='relu'))
model_B.add(Dense(32, activation='relu'))
model_B.add(Dense(10, activation='softmax'))

# compile model B
model_B.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# fitting model B
model_B.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=128, verbose=1)

# prepare model BN and learn
model_BN = Sequential()
model_BN.add(Flatten(input_shape=(28, 28)))
model_BN.add(Dense(256, activation='relu'))
model_BN.add(Dense(128, activation='relu'))
model_BN.add(Dense(32, activation='relu'))
model_BN.add(Dropout(0.6))
model_BN.add(Dense(10, activation='softmax'))

# compile model BN
model_BN.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# fitting model BN
model_BN.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=128, verbose=1)

# print clothes images
print_all_images_in_dataset(X_test, class_names, y_test)

# check model A
predicted_class_modelA = model_predict_check(model_A, X_test, y_test, 1, "model A")
print_metrics(model_A, X_test, y_test, "model A")
print_metrics_extend(model_A, X_test, y_test, "Model A")

# check model B
predicted_class_modelB = model_predict_check(model_B, X_test, y_test, 1, "model B")
print_metrics(model_B, X_test, y_test, "model B")
print_metrics_extend(model_B, X_test, y_test, "Model B")


# check model BN
predicted_class_modelBN = model_predict_check(model_B, X_test, y_test, 1, "model BN")
print_metrics(model_BN, X_test, y_test, "model BN")
print_metrics_extend(model_BN, X_test, y_test, "Model BN")


# print predicted image
print_image(X_test, y_test, 1, predicted_class_modelA)

# visualise confusion matrix
create_confusion_matrix(model_A, X_test, y_test, "Model A", 10)
create_confusion_matrix(model_B, X_test, y_test, "Model B", 10)
create_confusion_matrix(model_BN, X_test, y_test, "with normalization, Model BN", 10)


