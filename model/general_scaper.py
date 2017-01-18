# requests==2.11.1
import pandas as pd
import numpy as np
import pickle
import requests
import random
import time


# V_id = ["_beJmXpQPlM","_ibTYAxssQw","LlhgR0Y58ZI","zsgdzuooLUw","-HXZjkPgry8","H7Uyfqi_TE8",'QAwiyS5aTcU',"UeyP_tELq6E","E9AAlpH3ziM","JukZGqYx0gs","pWjfA4hBNe8","_4VgLfqzPxw","h7yZjSiype4","PzQlPmYoCVI","xsbkZMmO6vk","GAPqEAWW9lc","FaPtbs8VfCg"]

# V_id = ["GAgDjpawyzA","yFEILxZA6hY","K79WsDdFPTo","wWfF7KAnM58","SkZg1ZflpJs","XUKlg0XSG10","PgCBVGBHGx4","DglciBwGIHk","rYdFY35hVMA","Pr65zyDHXlc","6yEK7JRsXZk","V0Yb81yuprI","xSxgCguPEaM"]
#
# V_id = ['QgnjfkNU_HE','md8WOC35pZo','GhVKHy8bZAE','flYWffv9qqI','lCzklDp83Ck','F-aeNF8IiY4','05uFs8qVCcI','_9e21kFEG0k','iTdte3pksBs','KtgddI4qIok','3n21mMQVGWQ','DQ_9mMsieqg','O4WO9f57dTY','1aa--jf4CjY','gb8lrSp1Ghk','fdeH6Ksedwk','fp8H8EMm464','jgdPdeQZ3T8','X1nxYoWA0GI','oawB3G3B_XU']
# V_id =['wd5wovSxa18','tlZsSLe35z4','A357Za2Zhk0','99JjtRW0C2A','D7NQ12e9_3s','i3O3_xXbNm4','c80vGyzA0LI','itLYaFqKWwc','HZNy5irM2YE','H4ehjoFpdaQ','hKBHte0cc_0','x_nTfhOI8Nc','O9Z-7b7JkJY','4565PGb3laY','q9nqNoIFcfM','9B3TN2rEckQ','DbUAebkAfhs','WoDGNaQA_1o','o2VM3B_izXw','zaZKyYO_Jrk','0I-3TxjNVgk','FTGM9CX_Ugs','bD3N5MeHc3c','geyZ9c7uwGk','Ne5L1-IV858','FSH-dbbiroI','29nIXG5KJYw','cSGSzQaddFw','ZxUlPwM3AfE','yrn_MnDepaU','4Zd1HSI2EIk','6Tp0snCMoMk','EePcWVFtRCU','6vwwJ4uSreo','ahOHd_FhieI','nQy8EEODaT8','KrruWr4vePI','LtblpVfyAyk','rDve1A5EAvk','qaLTWthxm0g','PKRQHQtyn5A','WX2DfQc-pdw','LzPiqbNaafo']


# V_id= ["JOY8btlE0yU","hh2DcM1IKrU","RHri4V4duAk","wEduiMyl0ko","07Pm8ZY0XJI"]
V_id= ["vV4OIYKzsBk","Hd_ptbiPoXM","X4uUSxm8too","L8N0Xl6Taeg","ZlfIVEy_YOA"]
V_id= ['iS1g8G_njx8','O-zpOMYRi0w','oC-GflRB0y4','hXI8RQYC36Q','LjhCEhWiKXk','-CmadmM5cOk','kYtGl1dX5qI','kkx-7fsiWgg','rYEDA3JcQqw','nlcIKh6sBtc','j5-yKhDd64s','3AtDnEC4zak','JF8BRvqGCNs','nfWlot6h_JM','Pw-0pbY9JeU','pB-5XG-DbAA','Pgmx7z49OEk','AbPED9bisSc','aKuivabiOns','foE1mO2yM04','b8m9zhNAgKs','e-ORhEE9VVg','YJVmu6yttiw','OPf0YbXqDm0','UpsKGvPjAgw','rtOvBOTyX00','cmSbXsFE3l8','NUsoVlDFqZg','Io0fBr1XBUA','R4em3LKQCAQ','pXRviuL6vMY','k0BWlvnBmIE','AByfaYcOm4A','kdemFfbS5H0','Ho32Oh6b4jc','1TsVjvEkc4s','5GL9JoH4Sws','YQHsXMglC9A','bpOSxM0rNPM','DK_0jXPuIr0']

# >1,00,0000 <2000000
# V_id = ['aHjpOzsQ9YI','VT1-sitWRtY','ANS9sSJA9Yc','K_9tX4eHztY','cNw8A5pwbVI','BiQIc7fG9pA','FlsBObg-1BQ','AwAMEZsQBGI','X2BYmmTI04I','r_8ydghbGSg','Pzz4Z-O7710','6ACl8s_tBzE','0zGcUoRlhmw','nPvuNsRccVw','a7UFm6ErMPU','AgFeZr5ptV8','cHHLHGNpCSA','PVzljDmoPVs','_ovdm2yX4MA','1zfzka5VwRc','_wL3Pc-EmjA','XgJFqVvb2Ws','VA770wpLX-Q','3JWTaaS7LdU','1y6smkh6c-0','mk48xRzuNvA','o_1aF54DO60','syFZfO_wfMQ','lxw3C5HJ2XU','5y_KJAg8bHI','_kxz7WX4mLU','oiKj0Z_Xnjc','qDcFryDXQ7U','HcVv9R1ZR84','OXq-JP8w5H4','3x2ABSAMVno','jK2aIUmmdP4','LPgvNlrBfb0','uo35R9zQsAI','yUV9JwiQLog','cedoBlUvBlI','cPJUBQd-PNM','LUjn3RpkcKY','UKp2CrfmVfw','oh2LWWORoiM','B3eAMGXFw1o','V1bFr2SWP1I','-2U0Ivkn2Ds','WSeNSzJ2-Jw','Kuz3DUNZaC8']
# unseen >200,000
# V_id = ["49tpIMDy9BE","pRpeEdMmmQ0","B0nUwBBrJn8","_RRyniZG0Jo"]
# V_id = ['aE_gN8fA2xE','KlwPtIMSWyA','adQTmfXr_OQ','UsbY3YSzoRU','L83qMnbJ198','pVmV0dgWWBs','UH1x5aRtjSQ','7dIetQFw-n4','H5BiTDw9zac','-XZZyUeZG4k','U-aVkMClvBs','oDPCmmZifE8','NeXMxuNNlE8','2gxrI5CPYIM','OlofrCgODFQ','AKuBMihmVHQ','SsORb-dMwfE','hN74bOubUug','Lzlz12zws1I','wyLxuy4tPLs','fzrfrXhE-w4','fupWquPNoTc','INSPJnp1X4M','fnSBl46w82g','QVuoKMCm4K4','jX3iLfcMDCw','kLcB82y55Vk','wZr-416cfQQ','gbrbUfYSt0E','ToiDKxSOm0A','gbug3zTm3Ws','FCSBoOcGFFE','_-xEV9f1xE0','lleBWHq0kwM','4ZYVogCYsdA','IuLG6WqjOEo','QpgWc5u0PPw','FkTybqcX-Yo','DN7C_tE8H_A','-2swVic8KxY','Nx3iVbt4OrI','4dTTUDN1lV0','qzkOkh1tOqE','1sSM5lr9fnM','faQO57Iwlo0','GCipiBUnhUQ','GfxcnX7XWfg','_4LDlBCkA2g','H53183mVc2o','fyHZf3uysjk']
# # unseen >90000 <200000
# # V_id = ["dOyJqGtP-wU","qDrShJ_ItNk","SSZg1Wy7H0k"]
#
# # >30000 <50000
V_id = ['LoebZZ8K5N0','yFEILxZA6hY','FGmeA6CSIBY','k0ebrwegDr0','Edh_8LMpReY','1hyr7ZKkQbQ','EZG1K1-2omo','OFjHbN_WuVk','DoLAoOkG5gY','cweoXMacRv4','TI455Z37o30','R1IoZyhgrYw','xMk8wuw7nek','704EXbJ-b5k','2Qv0pD-Nfag','p6lNUQ3tFmA','Vzn4MJdaabw','UpwAXpA680Q','6QvEpCXzcBI','W4Fl6SUvy2A','us6u7PAdluE','cj0DxafLoz0','QbCCjhqjYc4','ipKbMMD8OEo','VeRvC4ebDyI','EAzGXqJSDJ8','H3N0ObC9klg','-ZwGeYu2pOQ','_bP0Uf3Shd0','NgWCG3f77Jk','TdQp85nN4to','ZeqsIQzs8sw','EuCh53ZG1D0','8WKgNyvsNDM','Q10cs2QJgeo','GZ-k3oblIM8','6gqk-yIDYwk','xdOykEJSXIg','qTfGxrAMQDA','tyKh4cI62CI','poL7l-Uk3I8','MRArCpmy4Hc','6iZN_5j3KUA','xNaA9wUo6GE','D9Clrc-XNiw','cwVhwavP7gs','onEfmC6HRF4','KwW9slmrKXo','BJemArTv7EI','oWTgvRGwzWg']
#
# >2000000
# # V_id = ['b8m9zhNAgKs','e-ORhEE9VVg','YJVmu6yttiw','OPf0YbXqDm0','UpsKGvPjAgw','rtOvBOTyX00','cmSbXsFE3l8','NUsoVlDFqZg','Io0fBr1XBUA','R4em3LKQCAQ','pXRviuL6vMY','k0BWlvnBmIE','AByfaYcOm4A','kdemFfbS5H0','Ho32Oh6b4jc','1TsVjvEkc4s','5GL9JoH4Sws','YQHsXMglC9A','bpOSxM0rNPM','DK_0jXPuIr0','gCYcHz2k5x0','AJtDXIazrMo','C_3d6GntKbk','nYh-n7EOtMA','QGJuMBdaqIw','IdneKLhsWOQ','mWRsgZuwf_8','IcrbM1l_BoI','OpQFFLBMEPI','CGyEd0aKWZE','34Na4j8AVgA','L8eRzOYhLuw','fLexgOxsZu0','ij_0p_6qTss','SXiSVQZLje8','HMUDVMiITOU','jGflUbPQfW8','i_kF4zLNKio','wzMrK-aGCug','o3mP3mJDL2k','-59jGD4WrmE','1ekZEVeXwek','ebXbLfLACGM','fWNaR-rxAic','hHUbLv4ThOo','fk4BbF7B29w','hiP14ED28CA','VbfpW0pbvaU','g5qU7p7yOY8','bbEoRnaOIbs']
# V_id = ["WhGnY2hTVF0","_GuOjXYl5ew","ASO_zypdnsQ","KQ6zr6kCPj8"]

# month old==2
# V_id = ['u_FBJ1kUV3g','eiEfrA6MWs4','LkxBS6GGDLs','Cpcv-g9TEPI','NxJdUTrZjts','XfmZBEcWyi4','drXGJ3ZZdvc','OYYHA3B6Ilo','PklYOfb-0QA','9Hmi3hJulEM','pz5X0BXEJ7g','FpY2VHckF3U','_fuPIpgR3pM','GReNKke1254','BsTWfcP7mjk','V81-7Rz92mg','rZmgSEYzpaw','QO4vJ99aF4M','oJyY7XtOQCM','YIamLru74nQ','TdQp85nN4to','wdsj7NmFHIg','HSnMnI7jwXo','IGdiACWiMAM','y7Og8q8dOpE','wxKRW1Z2lWo','O8q-w6aKSlA','ySd8VP8OOg8','5J4Yu9oauxY','hefKnloFxQg','rZcgL41_bYE','3cXLSr_0Yqk','MfV5FLea1PY','vu1qZCG6Yo8','VuUCWPXaAZE','Vr5Dc7Ciyf8','WMl03NKlaf4','rDInkCjhhjQ','OvLPUujF_mk','96ds226oA_U']

# V_id=["M2VvFXCR3II","67plwXQk6Ek","uC56dCzryWE","2lDzMuBWuqA","0XiiT5dR_Q","5pVBiM7KUqY"]
#2 minute
# V_id = ["1PNhuHa7lS0","heB2tD0-r-c","5PSWr2ovBvU","ImIaoKsjgUE"]
#sentdex
# V_id = ["JeamFbHhmDo","WYYxafb1A6E","HHUqhVzctQE","Y-CT_l1dnVU"]

API_KEYS = ["AIzaSyAgzszK84rYUM0ErWSdtiV-tyNGqGB3xFg","AIzaSyA3uNDJDl6WH0z8t9uB9pdmbIBpf54PVIE","AIzaSyCcLbOx4L6iTcS4NnvviLa1TfE7I1mnccU","AIzaSyAOpWL4ijH4vjO6sOF5ORIzohy_o2shL9s","AIzaSyCp8TYUqMn5LMgeHDvBcNcd2Y3pGbgVTAg"]

data={"V_id":[],"channelId":[],"publishedAt":[],"commentCount":[],"dislikeCount":[],"likeCount":[],"viewCount":[],"publishedAt":[],"categoryId":[],"ChannelPublishedAt":[],"channel_videoCount":[],"channel_subscriberCount":[],"channel_ViewCount":[]}
channel_dict = {}

columns = ['categoryId', 'channel_subscriberCount', 'definition', 'likeCount', 'dislikeCount', 'viewCount', 'commentCount', 'viewCount/channel_month_old', 'viewCount/video_month_old', 'viewCount/http_in_descp', 'viewCount/NoOfTags', 'viewCount/tags_in_desc', 'subscriberCount/videoCount', 'channelViewCount/channeVideoCount', 'channelViewCount/socialLink']
# ['dislikeCount', 'viewCount', 'commentCount','viewCount/video_month_old','subscriberCount/videoCount','channel_subscriberCount','subscriberCount/videoCount','viewCount/channel_month_old']

def get_url(Video_urls):
    v_id =  ",".join(Video_urls)
    k = random.randint(0,4)
    API_KEY = API_KEYS[k]
    url = "https://www.googleapis.com/youtube/v3/videos?part=status,snippet,topicDetails,contentDetails,statistics&id="+v_id+"&key="+API_KEY
    return url

def add_data(i,key1,key2,key3="NA"):
    if key3!="NA":
        try:
            data[key1].append(i[key2][key3])
        except Exception,err:
            print i["id"]
            print "error",err
            data[key1].append(0)
    else:
        try:
            data[key1].append(i[key2])
        except:
            data[key1].append(None)

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
            # channel_dict[i["id"]]={}
            # add_data(i,key1="channelTitle",key2="snippet",key3="title")
            # add_data(i,key1="ChannelDescription",key2="snippet",key3="description")
            add_data(i,key1="ChannelPublishedAt",key2="snippet",key3="publishedAt")

            add_data(i,key1="channel_ViewCount",key2="statistics",key3="viewCount")
            # add_data(i,key1="channel_commentCount",key2="statistics",key3="commentCount")
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
    r = requests.get(url)
    get_json = r.json()
    video_data(get_json)
    channel_data()
    # print data
    df = pd.DataFrame(data)
    df = get_final_data(df)

    continous_name = ['viewCount', 'commentCount','dislikeCount','viewCount/video_month_old','subscriberCount/videoCount']
    X_test = df[continous_name]
    filename = "model-2"
    fileObject = open(filename,'r')
    model_params = pickle.load(fileObject)
    clf = model_params
    # clf = model_params["clf"]
    # X_scaler = model_params["X_scaler"]
    # Y_scaler = model_params["Y_scaler"]

    np.set_printoptions(suppress=True)
    Y_test = df["likeCount"]
    # print "Original: ", list(Y_test)

    # X_test = X_scaler.transform(X_test)
    # Y_test = Y_scaler.transform(Y_test)

    pred  = clf.predict(X_test)
    # pred = Y_scaler.inverse_transform(pred)
    # org = Y_scaler.inverse_transform(Y_test)
    org = np.array(Y_test).astype("float32")

    # print "pred",pred
    # print "org",org
    print "org,pred"
    print zip(org, pred,((pred-org)/org)*100.0)
    # print pred-org

    # print "error",((pred-org)/org)*100.0

    print  clf.score(X_test,Y_test)

    # print clf.predict(X_test)
    # print clf.score(X_test,Y_test)
