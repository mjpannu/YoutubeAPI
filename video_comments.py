import requests
import json
apiKey = ""
channelID = ""
videoId = ""
comments_channel = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&allThreadsRelatedToChannelId="+channelID+"&key="+apiKey
		
channel_overall = "https://www.googleapis.com/youtube/v3/activities?part=snippet,contentDetails&channelId="+channelID+"&key="+apiKey
video_comments ="https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId="+videoId+"&key="+apiKey
test = requests.get(video_comments)

x= test.json()

d = {'a': [], 'b': []}

for i in x["items"]:
    d['a'].append(i["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"])
    d['b'].append(i["snippet"]["topLevelComment"]["snippet"]["textDisplay"])
    print(i["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

df = pandas.DataFrame(d)
df.to_csv("tst.csv")