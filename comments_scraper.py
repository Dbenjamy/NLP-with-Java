# You will need to add your own Google API key to KEYS
from KEYS import API_Key
from googleapiclient.discovery import build
import json
# Made as a function for recursion
def get_comments(service,comment_dict,max=95,item_num=0,page_token=None):
    count = 0
    # If first time through
    if page_token is None:
        video_data = service.commentThreads().list(
            videoId='uxPdPpi5W4o',
            part='snippet',
            maxResults=100
        ).execute()

        for i, item in enumerate(video_data['items']):
            comment_dict[i] = item['snippet']['topLevelComment']['snippet']['textOriginal']
            count += 1
    # For recursive calls
    else:
        # Get 100 comments
        video_data = service.commentThreads().list(
            videoId='uxPdPpi5W4o',
            part='snippet',
            maxResults=100,
            pageToken=page_token
        ).execute()
        count = item_num
        # Adding them to dictionary
        for i, item in enumerate(video_data['items']):
            comment_dict[i+(item_num)] = item['snippet']['topLevelComment']['snippet']['textOriginal']
            count += 1
    # Checking if there it needs to grab more
    if 'nextPageToken' in video_data and count < max - 5:
        get_comments(service,comment_dict,max,count,video_data['nextPageToken'])

# Calling the function
service = build('youtube','v3',developerKey=API_Key)
com_dict = dict()
get_comments(service,com_dict,100)

# Writing results to json file
with open('data.json','w') as file:
    com_json = json.dump(com_dict,file,indent=4)
