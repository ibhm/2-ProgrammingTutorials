from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split

##train_test_split splits the data into the following categories, test size means it only puts half the info in test, other half in train
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 0.5)

#import classifier
from sklearn import tree

clf = tree.DecisionTreeClassifier()

#train classifier
clf.fit(xtrain,ytrain)

predict = clf.predict(xtest)

from sklearn.metrics import accuracy

print (accuracy, ytest,predict)
