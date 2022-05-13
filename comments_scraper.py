import pandas as pd
from KEYS import API_Key
from googleapiclient.discovery import build

service = build('youtube','v3',developerKey=API_Key)

video_data = service.commentThreads().list(
    part='snippet,replies',
    id='uxPdPpi5W4o',
    # textFormat='plainText'
).execute()
# print(video_data)
for item in video_data['items']:
    print(item['snippet']['topLevelComment']['snippet']['textDisplay'])