#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score
from time import time

clf = AdaBoostClassifier()

t0 = time()
clf.fit(features_train, labels_train)
print "fitting time = ", round(time() -t0 , 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time = ", round(time() -t1), "s"

accuracy = accuracy_score(labels_test,pred)
print "accuracy = ", accuracy*100, "%"










try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
