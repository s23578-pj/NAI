"""
==================================================
Wheat Seed Dataset with Decision Tree
==================================================

Authors:
Alicja Szczypior
Krzysztof Szczypior

+-----------------------------------------------------------------------+

To run the program, install the following Python packages (if required):
pip3 install NumPy
pip3 install matplotlib.pyplot
pip3 install scikit-learn

+-----------------------------------------------------------------------+

Decision trees serve as a widely adopted supervised learning technique in machine learning, applicable to both
classification and regression tasks. They structure data into a tree-like format, where internal nodes signify
distinct features, each branch represents a decision based on those features, and each leaf node encapsulates
a final outcome or prediction. The essence lies in recursively dividing the dataset along features,
strategically selecting the most informative ones at each step to optimize the uniformity of resulting subsets.

In this specific context, we delve into the examination of wheat seed data, classified into three distinct categories.
The training and testing phases utilize 80% and 20% of the dataset, respectively. The decision tree's maximum
depth is set to 8. Subsequent to training the algorithm and evaluating its performance on the testing data,
precision metrics provide valuable insights.

Please ensure that your data is stored in a txt file ('wheat_seed.txt')

"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from tools import drawPlotThreeClassesComparison, draw_decision_tree

# Set options to print whole lists
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

# Data injection from txt file
wheat_ds = np.loadtxt('wheat_seeds.txt', delimiter='\t', )

headers = ["Area", "Perimeter", "Compactness", "Length of kernel", "Width of kernel", "Asymmetry coefficient",
           "Length of kernel groove"]

# Training data and classification separation
X, y = wheat_ds[:, :-1], wheat_ds[:, -1]

# Separate input data into two classes based on labels
class_1 = np.array(X[y == 1])
class_2 = np.array(X[y == 2])
class_3 = np.array(X[y == 3])

# Visualize input data na podstawie dwóch pierwszych kolumn
drawPlotThreeClassesComparison(class_1, class_2, class_3, 0, 1, "Area", "Perimeter")
drawPlotThreeClassesComparison(class_1, class_2, class_3, 0, 2, "Area", "Compactness")
drawPlotThreeClassesComparison(class_1, class_2, class_3, 0, 3, "Area", "Length of kernel")
drawPlotThreeClassesComparison(class_1, class_2, class_3, 0, 4, "Area", "Width of kernel")
drawPlotThreeClassesComparison(class_1, class_2, class_3, 0, 5, "Area", "Asymmetry coefficient")
drawPlotThreeClassesComparison(class_1, class_2, class_3, 0, 6, "Area", "Length of kernel groove")
drawPlotThreeClassesComparison(class_1, class_2, class_3, 3, 4, "Length of kernel", "Width of kernel")

# Split data into training and testing datasets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=5)

# Decision Tree classifier
classifier = DecisionTreeClassifier(random_state=0, max_depth=8)
decision_tree_classifier = DecisionTreeClassifier()

# Teaching the model
decision_tree_classifier.fit(X_train, y_train)

# Calculating predict values for test dataset
y_test_pred = decision_tree_classifier.predict(X_test)

# Draw decision_tree
draw_decision_tree(decision_tree_classifier, headers, ['1', '2', '3'], "Decision Tree For Wheat Seeds Data")

# Metrics related to the quality of the classification
print('accuracy tree', accuracy_score(y_test, y_test_pred))
class_names = ['Class-1', 'Class-2', 'Class-3']
print("\n" + "+" * 120)
print(
    "\nMetrics related to the quality of the classification of wheat seeds support decission tree classifier on training dataset\n")
print(classification_report(y_train, decision_tree_classifier.predict(X_train), target_names=class_names))
print("+" * 120)
print(
    "\nMetrics related to the quality of the classification of wheat seeds support decission tree classifier on test dataset\n")
print(classification_report(y_test, y_test_pred, target_names=class_names))
print("+" * 120 + "\n")

plt.show()
