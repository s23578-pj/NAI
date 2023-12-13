"""
======================================================
Neural Networks for Classification - Methods
======================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

+-----------------------------------------------------------------------+

Python at least 3.8
To run the program, install the following Python packages (if required):
- seaborn package
- numpy package
- pyplot from matplotlib

+-----------------------------------------------------------------------+
TERMINOLOGY

Neural networks are computational systems inspired by the structure and function of the human brain.
They are comprised of interconnected nodes known as neurons, organized into layers.
Each neuron processes input data and transmits signals to neurons in the next layer.
Neural networks learn by adjusting connections between neurons based on example data.

In the provided example, we are creating methods for various tasks related to the neural network,
including displaying images from the dataset, checking model predictions, printing evaluation metrics,
visualizing confusion matrices, and more.

"""
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score
from tensorflow.python.ops.confusion_matrix import confusion_matrix


def print_all_images_in_dataset(X_test, class_names, y_test):
    """
    Display a grid of images from the dataset along with their corresponding class names.

    Parameters:
    - X_test (numpy.ndarray): Test dataset containing images.
    - class_names (list): List of class names corresponding to the image labels.
    - y_test (numpy.ndarray): Array containing true labels of the images.
    """
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(X_test[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[y_test[i]])
    plt.show()


def model_predict_check(model, X, y, index, model_name):
    """
    Check and print the predicted class and actual class for a specific index using the given model.

    Parameters:
    - model: Trained neural network model.
    - X (numpy.ndarray): Input data for prediction.
    - y (numpy.ndarray): True labels of the input data.
    - index (int): Index of the specific record to check.
    - model_name (str): Name or identifier for the model.

    Returns:
    - predicted_class (int): Predicted class for the specified index.
    """
    sample_image = X[index]
    sample_image = np.expand_dims(sample_image, axis=0)

    predictions = model.predict(sample_image)
    predicted_class = np.argmax(predictions)

    print('\n\n+---------------------------------------------------------------------+')
    print(f'\nPredicted Class {model_name}: {predicted_class}')
    print(f'Actual Class {model_name}: {y[index]}')

    return predicted_class


def print_metrics(model, X, y, model_name):
    """
    Print the test loss, accuracy, and precision for the given model.

    Parameters:
    - model: Trained neural network model.
    - X (numpy.ndarray): Test dataset.
    - y (numpy.ndarray): True labels of the test dataset.
    - model_name (str): Name or identifier for the model.
    """
    loss, accuracy = model.evaluate(X, y)
    print(f'\n\nTest Loss {model_name}: {loss}, \nTest Accuracy {model_name}: {accuracy}\n\n')


def print_image(X, y, index, predicted_class):
    """
    Display a single image from the dataset with predicted and actual class labels.

    Parameters:
    - X (numpy.ndarray): Dataset containing images.
    - y (numpy.ndarray): True labels of the dataset.
    - index (int): Index of the specific record to display.
    - predicted_class (int): Predicted class for the specified index.
    """
    plt.imshow(X[index], cmap='gray')
    plt.title(f'Przewidziana klasa: {predicted_class}, \nPrawdziwa klasa: {y[index]}')
    plt.show()


def create_confusion_matrix(model, X, y, model_name, size):
    """
    Evaluate the model, create a confusion matrix, and visualize it using seaborn.

    Parameters:
    - model: Trained neural network model.
    - X (numpy.ndarray): Test dataset.
    - y (numpy.ndarray): True labels of the test dataset.
    - model_name (str): Name or identifier for the model.
    """
    # evaluate model
    model_score = model.evaluate(X, y, verbose=1)
    print(f"Test loss {model_name}:", model_score[0])
    print(f"Test accuracy {model_name}:", model_score[1])

    # creating prediction for whole test sub dataset from model A
    predictions = model.predict(X)
    predicted_labels = np.argmax(predictions, axis=1)

    # create confusion matrix
    confusion_matrix_created = confusion_matrix(y, predicted_labels)

    # plot and show confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(confusion_matrix_created, annot=True, fmt='d', cmap='magma', xticklabels=range(size),
                yticklabels=range(size))
    plt.xlabel('Predicted labels')
    plt.ylabel('Real labels')
    plt.title(f'Confusion Matrix {model_name}')
    plt.show()


def print_metrics_extend(model, X, y, model_name):
    """
    Prints extended classification metrics for a given model.

    Parameters:
    - model (tensorflow.keras.Model): Trained neural network model.
    - X (numpy.ndarray): Input data for prediction.
    - y (numpy.ndarray): True labels for the input data.
    - model_name (str): Name or identifier of the model.

    Returns:
    None

    Prints:
    - Accuracy: Ratio of correctly predicted instances.
    - Precision: Weighted average precision for each class.
    - Recall: Weighted average recall for each class.
    """
    predictions = model.predict(X)
    predicted_labels = np.argmax(predictions, axis=1)

    accuracy = accuracy_score(y, predicted_labels)
    print(f'Accuracy {model_name}: {accuracy}')

    precision = precision_score(y, predicted_labels, average='weighted')
    print(f'Precision  {model_name}: {precision}')

    recall = recall_score(y, predicted_labels, average='weighted')
    print(f'Recall {model_name}: {recall}')






