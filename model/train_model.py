# This contains the implementation for training and saving the model.

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
import matplotlib.pyplot as plt
import time

start_time = time.time()
df = pd.read_csv("../dataset/data_final.csv")
df = df.sample(frac=1).reset_index(drop=True)

continous_name = ['viewCount', 'commentCount','dislikeCount','viewCount/video_month_old','subscriberCount/videoCount']


# Making the training and test set.

X = df[continous_name]
print "Training Set Shape",X.shape
Y = df.likeCount
print "Testing Set Shape",Y.shape

print "Training in progress....."
# parameters
n_estimators = 200
max_depth = 25
min_samples_split=15
min_samples_leaf=2

# Random forest classifier
clf = RandomForestRegressor(n_estimators = n_estimators, max_depth = max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)

# It is trained of 2 Epochs
X = np.concatenate((X,X),axis=0)
Y = np.concatenate((Y,Y),axis=0)

clf.fit_transform(X,Y)



print "Feature Importance ranking",clf.feature_importances_


# Saving the model for predictions

file_name = "model-final"
print "---- Saved at -----"+file_name
fileObject = open(file_name,'wb')
#
pickle.dump(clf,fileObject)
fileObject.close()

print("--- %s seconds ---" % (time.time() - start_time))
