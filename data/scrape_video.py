import pandas as pd
import numpy as np
import pickle
import requests
import random
import time

API_KEYS = ["AIzaSyAgzszK84rYUM0ErWSdtiV-tyNGqGB3xFg","AIzaSyA3uNDJDl6WH0z8t9uB9pdmbIBpf54PVIE","AIzaSyCcLbOx4L6iTcS4NnvviLa1TfE7I1mnccU","AIzaSyAOpWL4ijH4vjO6sOF5ORIzohy_o2shL9s","AIzaSyCp8TYUqMn5LMgeHDvBcNcd2Y3pGbgVTAg"]

data={"duration":[],"dimension":[],"projection":[],"V_id":[],"caption":[],"license":[],"categoryId":[],"channelId":[],"description":[],"publishedAt":[],"tags":[],"thumbnail":[],"commentCount":[],"dislikeCount":[],"likeCount":[],"viewCount":[],"embeddable":[],"licencedContent":[],"privacyStatus":[],"publishedAt":[],"title":[],"definition":[],"defaultAudioLanguage":[]}


vid_list = [1,2,10,15,17,19,20,22,23,24,25,26,27,28,29]

# This function adds the data into the "data" dictionary.
def add_data(i,key1,key2,key3="NA"):
    if key3!="NA":
        try:
            data[key1].append(i[key2][key3])
        except :
            data[key1].append(None)
    else:
        try:
            data[key1].append(i[key2])
        except:
            data[key1].append(None)


# This function returns a list of URLs for sending requests to further.
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
        url = "https://www.googleapis.com/youtube/v3/videos?part=status,snippet,topicDetails,contentDetails,statistics&id="+v_id+"&key="+API_KEY
        url_list.append(url)


    return url_list

for v_id in vid_list:

    start_time = time.time()
    filename = str(v_id)+"list"
    fileObject = open(filename,'r')
    lst = pickle.load(fileObject)


    view_count=[]
    for i in lst:
        view_count+=i[:35]

    lst = set(view_count)
    lst = list(lst)
    new_lst_len = len(lst)

    url_list = get_url_list(new_lst_len,lst)
    print "Url List Length",len(url_list)

    c=0

    for url in url_list:

        print c
        r = requests.get(url)
        get_json = r.json()

        for i in get_json["items"]:

# -----------------------------------VIDEO RELATED FEATURES   ---------------------------------------------------------------------

            add_data(i,key1="title",key2="snippet",key3="title")

            add_data(i,key1="definition",key2='contentDetails',key3="definition")

            add_data(i,key1="tags",key2="snippet",key3="tags")

            add_data(i,key1="commentCount",key2="statistics",key3="commentCount")

            add_data(i,key1="duration",key2='contentDetails',key3="duration")

            add_data(i,key1="dimension",key2='contentDetails',key3="dimension")

            add_data(i,key1="projection",key2='contentDetails',key3="projection")

            add_data(i,key1="caption",key2='contentDetails',key3="caption")

            add_data(i,key1="licencedContent",key2='contentDetails',key3="licensedContent")

            add_data(i,key1="dislikeCount",key2="statistics",key3="dislikeCount")

            add_data(i,key1="V_id",key2='id')

            add_data(i,key1="categoryId",key2="snippet",key3="categoryId")

            add_data(i,key1="defaultAudioLanguage",key2="snippet",key3="defaultAudioLanguage")

            add_data(i,key1="description",key2="snippet",key3="description")

            add_data(i,key1="publishedAt",key2="snippet",key3="publishedAt")

            try:
                data['thumbnail'].append(i["snippet"]["thumbnails"]["medium"]["url"])
            except :
                data["thumbnail"].append(None)


            add_data(i,key1="likeCount",key2="statistics",key3="likeCount")

            add_data(i,key1="viewCount",key2="statistics",key3="viewCount")

            add_data(i,key1="embeddable",key2="status",key3="embeddable")

            add_data(i,key1="license",key2="status",key3="license")

            add_data(i,key1="privacyStatus",key2="status",key3="privacyStatus")

            add_data(i,key1="channelId",key2="snippet",key3="channelId")


        c+=1

        for key in data:
            # print key,
            print len(data[key]),


    file_name = "video_datafile"
    print "-------------"+str(v_id)+"--  Saved at"+file_name
    fileObject = open(file_name,'wb')

    pickle.dump(data,fileObject)
    # here we close the fileObject
    fileObject.close()

    print("--- %s seconds ---" % (time.time() - start_time))
