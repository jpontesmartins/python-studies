from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data[:, 2:]
y = iris.target

tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X, y)

from sklearn.tree import export_graphviz

f = open("./iris_tree.dot", 'w')
export_graphviz(tree_clf, 
    out_file=f,
    feature_names=iris.feature_names[2:],
    class_names=iris.target_names,
    rounded=True,
    filled=True)


# dot -Tpng iris_tree.dot -o iris_tree.png

# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris

# https://en.wikipedia.org/wiki/Iris_flower_data_set#The_following_Python_code_illustrates_usage.


