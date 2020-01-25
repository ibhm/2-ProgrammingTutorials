from sklearn import tree

##Basic Machine Learning code using Anaconda for developing a small classifer
##Based on Machine Learning Recipe 1


features = [[140,1],[130,1],[160,0],[180,0]]
texture = [0,0,1,1]

##Importing Decision Tree Classifier
clf=tree.DecisionTreeClassifier()

#use .fit(_,_) to put objects into classifer for model to learn
clf = clf.fit(features,texture)

print (clf.predict([[120,0]]))
