from sklearn import tree, svm, neighbors
import pandas as pd

# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# Classifiers
clf_tree = tree.DecisionTreeClassifier()
clf_svm = svm.SVC()
clf_neighbors = neighbors.KNeighborsClassifier()

# Training the models
clf_tree.fit(X, Y)
clf_svm.fit(X, Y)
clf_neighbors.fit(X, Y)

data = []

while True:
    height = input('Please enter Height(cm) (or enter q to stop): ')
    if height.lower() == 'q':
        break

    # Convert height to int
    height = int(height)
    weight = int(input('Please enter Weight(kg): '))
    shoe_size = int(input('Please enter Shoe size(EU): '))
    expected_output = input('Enter expected output: ')

    print()

    # Store the input data
    data.append([height, weight, shoe_size, expected_output])

# Create a DataFrame with the collected data
df = pd.DataFrame(data, columns=['Height(cm)', 'Weight(kg)', 'Shoe size(EU)', 'Expected Gender'])

# Add prediction columns to the DataFrame

df['Tree Prediction'] = clf_tree.predict(df[['Height(cm)', 'Weight(kg)', 'Shoe size(EU)']].values)
df['SVM Prediction'] = clf_svm.predict(df[['Height(cm)', 'Weight(kg)', 'Shoe size(EU)']].values)
df['KNeighbors Prediction'] = clf_neighbors.predict(df[['Height(cm)', 'Weight(kg)', 'Shoe size(EU)']].values)

# Display the DataFrame
# print(df)
df.to_excel('gender_classifier.xlsx', index=False)

