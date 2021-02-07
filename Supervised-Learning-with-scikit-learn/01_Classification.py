# --------------------------------------------------- 
# Supervised learning wiwth scikit-learn - Classification 
# 27 jan 2021 
# VNTBJR 
# --------------------------------------------------- 
#

######################################################################
# Pre-processing data  -------------------------------------------
######################################################################
# Import packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('datasets/house-vote-votes-84.csv', sep = ',')
df.head()
df.info()
df.shape

# changing column names
df.columns = ['party', 'infants', 'water', 'budget', 'physician', 'salvador',
               'religious', 'satellite', 'aid', 'missile', 'immigration', 
               'synfuels', 'education', 'superfund', 'crime', 'duty_free_exports',
               'eaa_rsa']

# convert '?' to 0
df[df == '?'] = 0
               
# convert 'y' to 1 and 'n' to 0
df[df == 'y'] = 1
df[df == 'n'] = 0

######################################################################
# Exploratory Data Analysis - EDA  -------------------------------------------
######################################################################
# Visual EDA
# education
plt.figure()
sns.countplot(x = 'education', hue = 'party', data = df, palette = 'RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()
plt.clf()

themes = ['satellite', 'missile']
for theme in themes:
  plt.figure()
  sns.countplot(x = theme, hue = 'party', data = df, palette = 'RdBu')
  plt.xticks([0,1], ['No', 'Yes'])
  plt.show()
quit()
plt.clf()
######################################################################
# The classification challenge  -------------------------------------------
######################################################################

# k-Nearest Neighbors: fit
# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit the classifier to the data
knn.fit(X = X, y = y)

# k-Nearest Neieghbors: predict
X_new = np.array([[0.696469,  0.286139,  0.226851,  0.551315,  0.719469,  0.423106,  0.980764,
         0.68483,  0.480932,  0.392118,  0.343178,  0.72905,  0.438572,  0.059678,
         0.398044,  0.737995]])

# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis = 1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit the classifier to the data
knn.fit(X = X, y = y)

# Predict the labels for the training data X
y_pred = knn.predict(X = X)

# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X = X_new)
print("Prediction: {}".format(new_prediction))
new_prediction.shape

######################################################################
# Measuring model performance  -------------------------------------------
######################################################################
# In classification, accuracy is a commonly used metric.
# The accuracy of a classifier is defined as the number of correct predictions
# divided by the total number of data points.
# Strategy 1 - to split data onto two sets, a training set and a testt set.

# Import necessary modules
from sklearn import datasets
import matplotlib.pyplot as plt

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and DESCR of the dataset
print(digits.keys())
print(digits['DESCR'])

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()
plt.clf()

# Train/Test split + Fit/Predict/Accuracy
# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Create feature and target arrays
X = digits.data
y = digits.target
?train_test_split
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size = 0.2, 
                                                    random_state = 42, 
                                                    stratify = y)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors = 7)

# Fit the classifier to the training data
knn.fit(X = X_train, y = y_train)

# Print the accuracy
print(f'{knn.score(X_test, y_test):.2f}')

# Overfittin and underfitting
# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors = k)

    # Fit the classifier to the training data
    knn.fit(X = X_train, y = y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X = X_train, y = y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X = X_test, y = y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()
plt.clf()

# The test accuracy is highest when using 1 to 3 neighbors.

