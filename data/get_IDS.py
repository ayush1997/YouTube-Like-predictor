import requests
import json
import pickle
import random

# We are extracting around 5000 video of every year(2010-2017) and storing them in pickle file.

#Put API keys
API_KEYS = []


category_dict  = {29:"Non-profits & Activism",28:"Science & Technology",27:"Education",26:"Howtostyle",25:"New&politics",24:"Entertainment",23:"Comedy",22:"People&blogs",20:"Gaming",19:"Travel&events",17:"Sports",15:"Pets&Animals",10:"Music",2:"Cars&vehicles",1:"Film&Animation"}


video_id=[]
video_dict = {}

new_video_id = []
count=0


for v_id in category_dict:
    category_id = v_id
    video_id=[]
    print "----------------------------------------------"+category_dict[v_id]+"-------------------------------------"

    for year in range(2010,2017):
        print "-------------------------------------------"+str(year)+"----------------------------------------------"

        for month in range(1,12):
            if month<9:
                publishedAfter = str(year)+"-0"+str(month)+"-01T00:00:00Z"
                publishedBefore = str(year)+"-0"+str(month+1)+"-01T00:00:00Z"
            elif month==9:
                publishedAfter = str(year)+"-0"+str(month)+"-01T00:00:00Z"
                publishedBefore = str(year)+"-"+str(10)+"-01T00:00:00Z"
            else:
                publishedAfter = str(year)+"-"+str(month)+"-01T00:00:00Z"
                publishedBefore = str(year)+"-"+str(month+1)+"-01T00:00:00Z"
            count = 0
            nextPageToken = ""
            print publishedBefore
            print publishedAfter

            while count!=10:
                print count
                k = random.randint(0,4)
                API_KEY = API_KEYS[k]
                url = "https://www.googleapis.com/youtube/v3/search?publishedAfter="+publishedAfter+"&publishedBefore="+publishedBefore+"&type=video&videoCategoryId="+str(category_id)+"&key="+API_KEY+"&maxResults=50&part=id&pageToken="+nextPageToken
                # url = "https://www.googleapis.com/youtube/v3/search?type=video&videoCategoryId="+str(category_id)+"&key="+API_KEY+"&maxResults=50&eventType=completed&part=id&pageToken="+"CLwFEAA"
                r = requests.get(url)
                get_json = r.json()
                # print get_json

                nextPageToken = get_json["nextPageToken"]
                print "nextPageToken = ",nextPageToken

                for i in get_json["items"]:
                     new_video_id.append(i["id"]["videoId"])

                print new_video_id

                video_id.append(new_video_id)
                #
                video_dict[nextPageToken] = new_video_id

                if new_video_id==[]:
                    count = 10
                else:
                    count+=1

                new_video_id = []



    file_name = str(v_id)+"list"
    print "----Saved at---"+file_name
    fileObject = open(file_name,'wb')

    pickle.dump(video_id,fileObject)

    # here we close the fileObject
    fileObject.close()
