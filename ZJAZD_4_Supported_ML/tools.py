from matplotlib import pyplot as plt
from sklearn.tree import plot_tree

"""
   Visualizes the distribution of input data based on two specified (first) parameters for three classes.

   Parameters:
   - class_1, class_2, class_3: numpy arrays, input data for each class.
   - parameterA, parameterB: int, indices of the parameters to be visualized.
   - parameterAName, parameterBName: str, names of the parameters for labeling.

   Returns:
   None
   """


def drawPlotThreeClassesComparison(class_1, class_2, class_3, parameterA, parameterB, parameterAName, parameterBName):
    plt.figure()
    plt.scatter(class_1[:, parameterA], class_1[:, parameterB], s=35, facecolors='green', label='Class 1')
    plt.scatter(class_2[:, parameterA], class_2[:, parameterB], s=35, facecolors='purple', label='Class 2')
    plt.scatter(class_3[:, parameterA], class_3[:, parameterB], s=35, facecolors='blue', label='Class 3')
    plt.title(f'Classification distribution based on property {parameterAName} and {parameterBName}')
    plt.ylabel(parameterAName)
    plt.xlabel(parameterBName)
    plt.legend()
    plt.show()


"""
   Visualizes the distribution of input data based on two specified (first) parameters for two classes.

   Parameters:
   - class_1, class_2: numpy arrays, input data for each class.
   - parameterA, parameterB: int, indices of the parameters to be visualized.
   - parameterAName, parameterBName: str, names of the parameters for labeling.

   Returns:
   None
   """


def drawPlotTwoClassesComparison(class_1, class_2, parameterA, parameterB, parameterAName, parameterBName):
    plt.figure()
    plt.scatter(class_1[:, parameterA], class_1[:, parameterB], s=35, facecolors='green', label='Class 1')
    plt.scatter(class_2[:, parameterA], class_2[:, parameterB], s=35, facecolors='purple', label='Class 2')
    plt.title(f'Classification distribution based on property {parameterAName} and {parameterBName}')
    plt.ylabel(parameterAName)
    plt.xlabel(parameterBName)
    plt.legend()
    plt.show()

    """
    Visualizes the decision tree model.

    Parameters:
    - model: DecisionTreeClassifier, the trained decision tree model.
    - headers: list of str, feature names.
    - class_name: list of str, class names.
    - title: str, title for the plot.

    Returns:
    None
    """


def draw_decision_tree(model, headers, class_name, title):
    plt.figure(figsize=(15, 10))
    plot_tree(model, filled=True, feature_names=headers, class_names=class_name, rounded=True)
    plt.title(title)
    plt.show()
