"""
==================================================
Neural Networks for Classification - animals
==================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

+-----------------------------------------------------------------------+

Python at least 3.8
To run the program, install the following Python packages (if required):
TensorFlow with some packages which should be imported in the code:
- cifar10
Keras library in Python.
- Flatten, Dense

+-----------------------------------------------------------------------+
TERMINOLOGY

Neural networks are computational systems inspired by the structure and function of the human brain.
They are comprised of interconnected nodes known as neurons, organized into layers.
Each neuron processes input data and transmits signals to neurons in the next layer.
Neural networks learn by adjusting connections between neurons based on example data.

In the provided example, we leverage the CIFAR-10 dataset, a collection of images representing various animals,
to train a neural network for classification. The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 different
classes. The neural network architecture includes convolutional layers, max-pooling, and dense layers.

The model is trained using the Adam optimizer and categorical crossentropy as the loss function.
After training, the model's performance is evaluated on the test dataset.

"""
import numpy as np
from keras.datasets import cifar10
from keras.utils import to_categorical
from keras import layers, models

# Load CIFAR-10 dataset
(X_train_cifar, y_train_cifar), (X_test_cifar, y_test_cifar) = cifar10.load_data()

# Normalize pixel values to be between 0 and 1
X_train_cifar = X_train_cifar / 255.0
X_test_cifar = X_test_cifar / 255.0

# Convert labels to categorical
y_train_categorical_cifar = to_categorical(y_train_cifar, num_classes=10)
y_test_categorical_cifar = to_categorical(y_test_cifar, num_classes=10)

# Define neural network model
model_cifar = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='tanh', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='tanh'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(150, activation='tanh'),
    layers.Dense(100, activation='tanh'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model_cifar.compile(optimizer='adam', loss='categorical_crossentropy', metrics='accuracy')

# Train the model
model_cifar.fit(X_train_cifar, y_train_categorical_cifar, validation_data=(X_test_cifar, y_test_categorical_cifar), epochs=10, verbose=1)

# Display model summary
model_cifar.summary()

loss_cifar, accuracy_cifar = model_cifar.evaluate(X_test_cifar, y_test_categorical_cifar)
print(f'Test Loss CIFAR-10: {loss_cifar}, Test Accuracy CIFAR-10: {accuracy_cifar}')

# Make predictions on a sample image from the test set
sample_image = X_test_cifar[0]
sample_image = sample_image / 255.0

sample_image = np.expand_dims(sample_image, axis=0)

predictions = model_cifar.predict(sample_image)
predicted_class = np.argmax(predictions)

print(f'\nPredicted Class: {predicted_class}')
print(f'Actual Class: {y_test_cifar[0][0]}')
