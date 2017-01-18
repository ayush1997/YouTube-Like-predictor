import pandas as pd
import numpy as np
import pickle
import requests
import random
import time
import math
import sys

arg = sys.argv
V_id = arg[1:]
print "Video IDs",V_id

API_KEYS = ["AIzaSyAgzszK84rYUM0ErWSdtiV-tyNGqGB3xFg","AIzaSyA3uNDJDl6WH0z8t9uB9pdmbIBpf54PVIE","AIzaSyCcLbOx4L6iTcS4NnvviLa1TfE7I1mnccU","AIzaSyAOpWL4ijH4vjO6sOF5ORIzohy_o2shL9s","AIzaSyCp8TYUqMn5LMgeHDvBcNcd2Y3pGbgVTAg"]

data={"V_id":[],"channelId":[],"publishedAt":[],"commentCount":[],"dislikeCount":[],"likeCount":[],"viewCount":[],"publishedAt":[],"categoryId":[],"ChannelPublishedAt":[],"channel_videoCount":[],"channel_subscriberCount":[],"channel_ViewCount":[]}
channel_dict = {}

columns = ['categoryId', 'channel_subscriberCount', 'definition', 'likeCount', 'dislikeCount', 'viewCount', 'commentCount', 'viewCount/channel_month_old', 'viewCount/video_month_old', 'viewCount/http_in_descp', 'viewCount/NoOfTags', 'viewCount/tags_in_desc', 'subscriberCount/videoCount', 'channelViewCount/channeVideoCount', 'channelViewCount/socialLink']
# ['dislikeCount', 'viewCount', 'commentCount','viewCount/video_month_old','subscriberCount/videoCount','channel_subscriberCount','subscriberCount/videoCount','viewCount/channel_month_old']

# The function returns the final URL for request
def get_url(Video_urls):
    v_id =  ",".join(Video_urls)
    k = random.randint(0,4)
    API_KEY = API_KEYS[k]
    url = "https://www.googleapis.com/youtube/v3/videos?part=status,snippet,topicDetails,contentDetails,statistics&id="+v_id+"&key="+API_KEY
    return url

# This function populates the data dictionary
def add_data(i,key1,key2,key3="NA"):
    if key3!="NA":
        try:
            data[key1].append(i[key2][key3])
        except Exception,err:
            if key1 in ['viewCount', 'commentCount','dislikeCount','publishedAt','channel_videoCount','channel_subscriberCount']:
                print i["id"]
                print key1+"missing"
            data[key1].append(0)
    else:
        try:
            data[key1].append(i[key2])
        except:
            data[key1].append(None)

# The function is used to get the Video relevant data
def video_data(get_json):
    for i in get_json["items"]:

# -----------------------------------VIDEO RELATED FEATURES   ---------------------------------------------------------------------

        # add_data(i,key1="tags",key2="snippet",key3="tags")

        add_data(i,key1="commentCount",key2="statistics",key3="commentCount")

        add_data(i,key1="dislikeCount",key2="statistics",key3="dislikeCount")

        add_data(i,key1="V_id",key2='id')

        add_data(i,key1="categoryId",key2="snippet",key3="categoryId")

        add_data(i,key1="publishedAt",key2="snippet",key3="publishedAt")

        add_data(i,key1="likeCount",key2="statistics",key3="likeCount")

        add_data(i,key1="viewCount",key2="statistics",key3="viewCount")

        add_data(i,key1="channelId",key2="snippet",key3="channelId")

# It gets the channel relevant data

def channel_data():

    channel_id = ",".join(data["channelId"])

    k = random.randint(0,4)
    API_KEY = API_KEYS[k]
    url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id="+channel_id+"&key="+API_KEY
    # print url
    r = requests.get(url)
    get_json = r.json()

    if len(set(data["channelId"])) == len(data["channelId"]):
        for i in get_json["items"]:
            add_data(i,key1="ChannelPublishedAt",key2="snippet",key3="publishedAt")

            add_data(i,key1="channel_ViewCount",key2="statistics",key3="viewCount")
            add_data(i,key1="channel_subscriberCount",key2="statistics",key3="subscriberCount")
            add_data(i,key1="channel_videoCount",key2="statistics",key3="videoCount")
    else:
        for i in get_json["items"]:
            channel_dict[i["id"]]={}
            # add_data(i,key1="channelTitle",key2="snippet",key3="title")
            # add_data(i,key1="ChannelDescription",key2="snippet",key3="description")
            channel_dict[i["id"]]["ChannelPublishedAt"] = i["snippet"]["publishedAt"]
            channel_dict[i["id"]]["channel_ViewCount"] = i["statistics"]["viewCount"]
            channel_dict[i["id"]]["channel_subscriberCount"] = i["statistics"]["subscriberCount"]
            channel_dict[i["id"]]["channel_videoCount"] = i["statistics"]["videoCount"]
        # print channel_dict

        for j in data["channelId"]:
            add_data(channel_dict,key1="ChannelPublishedAt",key2=j,key3="ChannelPublishedAt")
            add_data(channel_dict,key1="channel_ViewCount",key2=j,key3="channel_ViewCount")
            add_data(channel_dict,key1="channel_subscriberCount",key2=j,key3="channel_subscriberCount")
            add_data(channel_dict,key1="channel_videoCount",key2=j,key3="channel_videoCount")



def get_months(x):
    return 12-x.month + 1 + (2016 - (x.year+1)+1)*12

# The function gets the data after coverting to derived features
def get_final_data(df):

    df["months_old"] = pd.to_datetime(df.publishedAt).apply(lambda x: get_months(x))
    df["channel_months_old"] = pd.to_datetime(df.ChannelPublishedAt).apply(lambda x: get_months(x))

    # print df
    df["viewCount/channel_month_old"] = df.apply(lambda x: float(x["viewCount"])/(x["channel_months_old"]+1),axis=1)
    df["viewCount/video_month_old"] = df.apply(lambda x: float(x["viewCount"]) / float(x["months_old"]+1),axis=1)

    # df["channelViewCount/channeVideoCount"] = df.apply(lambda x: (float(x["channel_ViewCount"])+1)/(float(x["channel_videoCount"])+1),axis=1)
    df["subscriberCount/videoCount"] = df.apply(lambda x: (float(x["channel_subscriberCount"])+1)/(float(x["channel_videoCount"])+1),axis=1)

    return df

if __name__ == "__main__":

    url = get_url(V_id)
    # print url
    print "Collecting data ......."
    r = requests.get(url)
    get_json = r.json()
    # print get_json
    video_data(get_json)
    channel_data()

    print "Data processing in progress ........"
    df = pd.DataFrame(data)
    df = get_final_data(df)

    features = ['viewCount', 'commentCount','dislikeCount','viewCount/video_month_old','subscriberCount/videoCount']

    X_test = df[features]
    Y_test = df["likeCount"]

    print "Fetching Model ........"
    filename = "model-final"
    fileObject = open(filename,'r')
    model = pickle.load(fileObject)
    clf = model


    np.set_printoptions(suppress=True)


    pred  = np.ceil(clf.predict(X_test))

    org = np.array(Y_test).astype("float32")

    err = ((pred-org)/org)*100.0

# This gives the difference between predicted and true like counts,(+) ->predicted more,(-) -> predicted less
    diff = pred - org

    try:
        out = pd.DataFrame({"V_ids":V_id,"Original":org,"Predicted":pred,"Difference(+/-)":diff,"Error Rate":err})
        print out[['V_ids','Original','Predicted',"Difference(+/-)","Error Rate"]]
    except:
        print "Video ID"+"              "+"Original"+"              "+"Predicted"+"             "+"Error"
        for i in zip(V_id,org, pred,((pred-org)/org)*100.0):
            print i[0]+"                "+str(i[1])+"               "+str(i[2])+"                "+str(i[3])


    print  "R^2 Score : ",clf.score(X_test,Y_test)
