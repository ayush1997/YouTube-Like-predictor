import pandas as pd
import numpy as np
import pickle
import requests
import random

API_KEYS = ["AIzaSyAgzszK84rYUM0ErWSdtiV-tyNGqGB3xFg","AIzaSyA3uNDJDl6WH0z8t9uB9pdmbIBpf54PVIE","AIzaSyCcLbOx4L6iTcS4NnvviLa1TfE7I1mnccU","AIzaSyAOpWL4ijH4vjO6sOF5ORIzohy_o2shL9s","AIzaSyCp8TYUqMn5LMgeHDvBcNcd2Y3pGbgVTAg"]

channel_data={"channelTitle":[],"ChannelDescription":[],"ChannelPublishedAt":[],"channel_videoCount":[],"channel_commentCount":[],"channel_subscriberCount":[],"channel_ViewCount":[]}
# channel_data={"social_links":[],"twitter_url":[]}
channel_dict = {}

#extract the unique channel id list from saved "video_datafile" pickled file.
filename = "video_datafile"
fileObject = open(filename,'r')
video_dict = pickle.load(fileObject)
channel_ids = set(video_dict["channelId"])
print len(channel_ids)

file_name = "channelIdList"
print "------ Saved at----"+file_name
fileObject = open(file_name,'wb')

pickle.dump(channel_dict,fileObject)
# here we close the fileObject
fileObject.close()


# print channel_data
def add_data(i,key1,key2,key3,ch_id="",channel=False):

    if not channel:
        try:
            channel_dict[ch_id][key1]=i[key2][key3]
        except Exception,err:
            print err
            channel_dict[ch_id][key1] = None

    else:
        try:
            channel_data[key1].append(channel_dict[key2][key3])
            print len(channel_data["twitter_url"])
            print len(channel_data["social_links"]),
        except Exception,err:
            print err

def get_url_list(new_lst_len,lst):
    url_list=[]

    r = (new_lst_len - (new_lst_len)%50)+1

    for j in range(0,r,50):

        if j==r-1:
            v_id = ",".join(lst[j:])
            # print len(v_id)
        else:
            v_id = ",".join(lst[j+0:j+50])
            # print len(v_id)

        k = random.randint(0,4)
        API_KEY = API_KEYS[k]
        url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id="+v_id+"&key="+API_KEY
        url_list.append(url)
    return url_list


# Since there are videos in the dataset which are not of the same channel,therefore not unique channel ids are extacted and further requested to collect data.
filename = "channelIdList"
fileObject = open(filename,'r')
lst = pickle.load(fileObject)
lst = set(lst)
lst = list(lst)
new_lst_len = len(lst)
print "Set(channels list)",new_lst_len

url_list = get_url_list(new_lst_len,lst)
print "url list length",len(url_list)

c=0
for urls in url_list:
    print c
    # print urls
    k = random.randint(0,4)
    API_KEY = API_KEYS[k]
    url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id="+urls+"&key="+API_KEY

    r = requests.get(urls)
    get_json = r.json()

    for i in get_json["items"]:
        channel_dict[i["id"]]={}
        add_data(i,key1="channelTitle",key2="snippet",key3="title",ch_id = i["id"])
        add_data(i,key1="ChannelDescription",key2="snippet",key3="description",ch_id=i["id"])
        add_data(i,key1="ChannelPublishedAt",key2="snippet",key3="publishedAt",ch_id=i["id"])

        add_data(i,key1="channel_ViewCount",key2="statistics",key3="viewCount",ch_id=i["id"])
        add_data(i,key1="channel_commentCount",key2="statistics",key3="commentCount",ch_id=i["id"])
        add_data(i,key1="channel_subscriberCount",key2="statistics",key3="subscriberCount",ch_id=i["id"])
        add_data(i,key1="channel_videoCount",key2="statistics",key3="videoCount",ch_id=i["id"])

    # for key in channel_dict:
    #     # print key,
    #     print len(channel_dict[key]),
    print len(channel_dict)

    c+=1

file_name = "channels_dict"
print "------ Saved at----"+file_name
fileObject = open(file_name,'wb')

pickle.dump(channel_dict,fileObject)
# here we close the fileObject
fileObject.close()



# We use the saved data of unique channels and further form the final dataset of all channels.
filename = "channelIdList"
fileObject = open(filename,'r')
lst = pickle.load(fileObject)

print len(lst)
# print lst[:2]
keys = channel_dict.keys()
error=0
for i,channelId in enumerate(lst):
    if i%10000==0:
        print i
    if channelId in keys:
        # print "Alredy present"

        add_data(channelId,key1="channelTitle",key2=channelId,key3="channelTitle",channel=True)
        add_data(channelId,key1="ChannelDescription",key2=channelId,key3="ChannelDescription",channel=True)
        add_data(channelId,key1="ChannelPublishedAt",key2=channelId,key3="ChannelPublishedAt",channel=True)

        add_data(channelId,key1="channel_ViewCount",key2=channelId,key3="channel_ViewCount",channel=True)
        add_data(channelId,key1="channel_commentCount",key2=channelId,key3="channel_commentCount",channel=True)
        add_data(channelId,key1="channel_subscriberCount",key2=channelId,key3="channel_subscriberCount",channel=True)
        add_data(channelId,key1="channel_videoCount",key2=channelId,key3="channel_videoCount",channel=True)
        # add_data(channelId,key1="social_links",key2=channelId,key3="social_links",channel=True)
        # add_data(channelId,key1="twitter_url",key2=channelId,key3="twitter_url",channel=True)

    else:
        print channelId
        print "error",error
        error+=1



file_name = "channels_datafile"

fileObject = open(file_name,'wb')

pickle.dump(channel_data,fileObject)
# here we close the fileObject
fileObject.close()
print "------ Saved at---"+file_name
