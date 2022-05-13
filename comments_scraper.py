import pandas as pd
from KEYS import API_Key
from googleapiclient.discovery import build
from pprint import pprint

service = build('youtube','v3',developerKey=API_Key)

video_data = service.commentThreads().list(
    videoId='uxPdPpi5W4o',
    part='snippet',
    maxResults=1
).execute()

for item in video_data['items']:
    pprint(item['snippet']['topLevelComment']['snippet']['textDisplay'])

