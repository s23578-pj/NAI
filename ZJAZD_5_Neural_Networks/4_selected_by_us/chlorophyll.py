"""
==================================================
Neural Network for Chlorophyll Levels Classification
==================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

+-----------------------------------------------------------------------+

Python at least 3.8
To run the program, install the following Python packages (if required):
- pandas
- keras

+-----------------------------------------------------------------------+
DATASET

The dataset used in this script is loaded from the "chlorophyll_a_b_levels.csv" file.
It contains information about various features related to chlorophyll levels.

TERMINOLOGY

Neural networks are computational systems inspired by the structure and function of the human brain.
They are comprised of interconnected nodes known as neurons, organized into layers.
Each neuron processes input data and transmits signals to neurons in the next layer.
Neural networks learn by adjusting connections between neurons based on example data.

In this example, we are using a neural network for the classification of chlorophyll levels into two classes.
"""
import pandas as pd
from keras.utils import to_categorical
from keras import layers, models
from methods import *

from sklearn.model_selection import train_test_split

chlorophyll_ds = pd.read_csv("chlorophyll_a_b_levels.csv", sep=",")

X, y = chlorophyll_ds.iloc[:, 0:-1], chlorophyll_ds.iloc[:, -1]

# Separate input data into two classes based on labels
class_1 = np.array(X[y == 1.0])
class_2 = np.array(X[y == 2.0])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

# Transformed labels into category
y_train_categorical = to_categorical(y_train - 1)
y_test_categorical = to_categorical(y_test - 1)


model = models.Sequential([
    layers.Flatten(),
    layers.Dense(150, activation='tanh'),
    layers.Dense(100, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(2, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics='accuracy')

model.fit(X_train, y_train_categorical, validation_data=(X_test, y_test_categorical), epochs=50, verbose=1)

model.summary()

predict = model.predict(X_test[1:])
print(f'Real class: {y_test_categorical[1, -1]}')
print(f'Predicted class: {np.argmax(predict[0])}')
