from sklearn import tree 
import numpy as np
import pickle

# import data
csv_file = 'shoe_data.csv'
values = np.genfromtxt(csv_file, delimiter = ',', dtype ='|U')

# select model
clf = tree.DecisionTreeClassifier()

# data 
X = (values[1:,0:3])
#print("X =", values[1:,0:3])

# labels
Y = (values[1:,3])
#print("Y =", values[1:,3])

# train model
clf = clf.fit(X, Y)

# make prediction
#prediction = clf.predict([[180, 60, 35]])

#print("prediction:", prediction)

# Saving model to disk
pickle.dump(clf, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
