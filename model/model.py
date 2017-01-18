import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=4,
                        n_jobs=1, train_sizes=np.linspace(.1, 1.0, 5)):

    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    plt.show()


df = pd.read_csv("data_final.csv")
df = df.sample(frac=1).reset_index(drop=True)

Y = df.likeCount

print list(df.columns)

# Splitting into test/train
X = df[continous_name]
# X = df
print X.shape


clf = RandomForestRegressor(n_estimators = 200,max_depth = 25,min_samples_split=15,min_samples_leaf=2)

X = np.concatenate((X,X),axis=0)
Y = np.concatenate((Y,Y),axis=0)
clf.fit_transform(X,Y)
#
pred  = clf.predict(X_test)

org = Y_test
#
print "pred",pred[:20]
print "org",org[:20]
#
print "error",((pred-org)/org)*100.0
#
print  clf.score(X_test,Y_test)
print  clf.score(X_train,Y_train)

print clf.feature_importances_


file_name = "model-3"
print "---- Saved at"+file_name
fileObject = open(file_name,'wb')
#
pickle.dump(clf,fileObject)
# here we close the fileObject
fileObject.close()

# plot_learning_curve(clf,"ghg",X,Y)
# plt.show()
