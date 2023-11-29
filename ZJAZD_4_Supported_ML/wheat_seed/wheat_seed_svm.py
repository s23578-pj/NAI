"""
======================================================
Wheat Seed Dataset with Support Vector Machines (SVM)
======================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

+-----------------------------------------------------------------------+

To run the program, install the following Python packages (if required):
pip3 install NumPy
pip3 install matplotlib.pyplot
pip3 install scikit-learn

+-----------------------------------------------------------------------+

Support Vector Machines (SVMs) as a supervised machine learning algorithm primarily employed for classification tasks.
These models excel at identifying an optimal decision boundary or hyperplane, effectively segregating data points into
distinct classes while maximizing the margin between them. SVMs demonstrate versatility in handling both linear and
non-linear data patterns, achieved through the application of diverse kernel functions.

In the provided example, our focus lies in the analysis of seed data categorized into three classes. The training and
testing phases utilize 80% and 20% of the dataset, respectively. Notably, linear kernel is managed by the SVM algorithm.
Post-learning the algorithm and assessing its performance on the testing data, we obtain valuable insights into
the precision of the algorithm.

Please ensure that your data is stored in a txt file ('wheat_seed.txt')

"""

import numpy as np
from sklearn import svm
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Set options to print whole lists
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

# Data injection from txt file
wheat_ds = np.loadtxt('wheat_seeds.txt', delimiter='\t', )

headers = ["Area", "Perimeter", "Compactness", "Length of kernel", "Width of kernel", "Asymmetry coefficient", "Length of kernel groove"]

# Training data and classification separation
X, y = wheat_ds[:, :-1], wheat_ds[:, -1]

# Separate input data into two classes based on labels
class_1 = np.array(X[y == 1])
class_2 = np.array(X[y == 2])
class_3 = np.array(X[y == 3])

# Split data into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

# Support Vector classifier
svm_model = svm.SVC(kernel='linear')

# Teaching the model
svm_model.fit(X_train, y_train)

# Calculating predict values for test dataset
y_test_pred = svm_model.predict(X_test)

sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

svc = SVC(kernel='rbf', C=1, gamma=2)
svc.fit(X_train_std, y_train)
svc_y_pred = svc.predict(X_test_std)

# Metrics related to the quality of the classification
print('accuracy tree', accuracy_score(y_test, y_test_pred))
class_names = ['Class-1', 'Class-2', 'Class-3']
print("\n" + "+"*120)
print("\nMetrics related to the quality of the classification of wheat seeds support vector classifier model on training dataset\n")
print(classification_report(y_train, svm_model.predict(X_train), target_names=class_names))
print("+"*120)
print("\nMetrics related to the quality of the classification of wheat seeds support vector classifier model on training dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("+"*120 + "\n")
