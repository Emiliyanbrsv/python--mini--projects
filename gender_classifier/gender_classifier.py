from sklearn import tree
from sklearn import svm

# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']


# Classifiers
clf_tree = tree.DecisionTreeClassifier()
clf_svm = svm.SVC()


# Training the models
clf_tree.fit(X, Y)
clf_svm.fit(X, Y)


# Testing with new data
height = int(input('Please enter Height(cm): '))
weight = int(input('Please enter Weight(kg): '))
shoe_size = int(input('Please enter Shoe size(eu): '))

print()

prediction_clf_tree = clf_tree.predict([[height, weight, shoe_size]])
print(f"Tree Classifier prediction: {prediction_clf_tree[0]}")

prediction_clf_svm = clf_svm.predict([[height, weight, shoe_size]])
print(f"SVM Classifier prediction: {prediction_clf_tree[0]}")
