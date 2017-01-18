import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
import pickle
import matplotlib.pyplot as plt



columns = ['categoryId', 'channel_subscriberCount', 'definition', 'likeCount', 'dislikeCount', 'viewCount', 'commentCount', 'viewCount/monthOld', 'viewCount/channel_month_old', 'viewCount/video_month_old', 'viewCount/http_in_descp', 'viewCount/NoOfTags', 'viewCount/tags_in_desc', 'social_links', 'subscriberCount/videoCount', 'channelViewCount/channeVideoCount', 'channelViewCount/socialLink']

continous_name = ['viewCount', 'commentCount','dislikeCount','viewCount/video_month_old','subscriberCount/videoCount']


df = pd.read_csv("notebook/data_final.csv")
df = df.sample(frac=1).reset_index(drop=True)

Y = df.likeCount
X= df[continous_name]

print list(df.columns)


pipeline=  Pipeline([
                    ('clf',RandomForestRegressor())
                    ])
#
parameters={
    'clf__n_estimators':([150,200]),
    'clf__max_depth':([15,25,30]),
    'clf__min_samples_split':([5,15,10]),
    'clf__min_samples_leaf':([2,5])
}


grid_search = GridSearchCV(pipeline,parameters,n_jobs=4,verbose=1,scoring="r2")

grid_search.fit(X,Y)

print "Best score:",grid_search.best_score_
print "Best parameters set:"
best_parameters = grid_search.best_estimator_.get_params()

for param_name in sorted(parameters.keys()):
    print (param_name,best_parameters[param_name])
