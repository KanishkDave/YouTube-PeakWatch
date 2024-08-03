import pandas as pd
import sys
import os
from googleapiclient.discovery import build

# Initilizing the Config parameters using below method
def config():

    API_KEY = 'AIzaSyD_hgi_gmyCFpD3ddgXkE_1RW0qek2UHW4'
    CHANNEL_ID = ['UCCezIgC97PvUuR4_gbFUs5g','UCfzlCWGWYyIQ0aLC5w48gBQ','UCdp6GUwjKscp5ST4M4WgIpw']

    EXTRACTED_DATA = []
    YOUTUBE = build('youtube', 'v3', developerKey=API_KEY)

    return API_KEY, CHANNEL_ID, EXTRACTED_DATA, YOUTUBE

# Results grabbed from search resource
def get_channel_details(API_KEY, CHANNEL_ID, EXTRACTED_DATA, YOUTUBE):

    for channel in CHANNEL_ID:

        try:
            request = YOUTUBE.search().list(
            part='snippet',
            channelId=channel,
            type='video',
            order='date',
            maxResults=5
            )
            response = request.execute()

        except Exception as e:

            print(f"Failed to fetch details for channel {channel}: {e}")
            sys.exit(1)

        for item in response['items']:
            
            published_date = item['snippet']['publishedAt']
            channel_id = item['snippet']['channelId']
            video_id = item['id']['videoId']
            video_title = item['snippet']['title']
            video_desc = item['snippet']['description']  

            try:
                channel_name, view_count, like_count, commment_count = get_video_details(YOUTUBE, video_id)
                EXTRACTED_DATA.append([video_id, video_title, video_desc, channel_id, channel_name,
                                    view_count, like_count, commment_count])
            except Exception as e:
                print(f"Failed to fetch statistics for video {video_id} : {e}")
                sys.exit(1)

    df = pd.DataFrame(EXTRACTED_DATA, columns=["VIDEO_ID", "VIDEO_TITLE", "VIDEO_DESC", "CHANNEL_ID",
                                               "CHANNEL_NAME", "VIEW_COUNT", "LIKE_COUNT", "COMMMENT_COUNT"])
    
    result_directory = os.path.join(os.path.dirname(__file__), '..', 'data')
    if not os.path.exists(result_directory):
        os.makedirs(result_directory)
    
    df.to_csv(os.path.join(result_directory, "YoutubeVideoResults.csv"), index=False)

    return df


def get_video_details(YOUTUBE, video_id):


    try:
        request2 = YOUTUBE.videos().list(
            part=['statistics', 'snippet'],
            id=video_id
        )
        response2 = request2.execute()

    except Exception as e:
        print(f"Failed to fetch statistics for video {video_id}: {e}")
        # The raise statement is used to re-raise the caught exception, allowing it to propagate up the call stack.
        raise
        
    for item in response2['items']:
    
        channel_name = item['snippet']['channelTitle']
        view_count = item['statistics']['viewCount']
        like_count = item['statistics']['likeCount']
        commment_count = item['statistics']['commentCount']
        
        return channel_name, view_count, like_count, commment_count
    

def fetching_most_viewed_videos(df):

    try:
        # Changed the data type from Object to Int for Int Cols 
        df['VIEW_COUNT'] = pd.to_numeric(df['VIEW_COUNT'])
        df['LIKE_COUNT'] = pd.to_numeric(df['LIKE_COUNT'])
        df['COMMMENT_COUNT'] = pd.to_numeric(df['COMMMENT_COUNT'])

        print(df.dtypes)

        # For adding Video link in the dataframe
        df['VIDEO_LINK'] = ["https://www.youtube.com/watch?v={}".format(video) for video in df['VIDEO_ID']]
        print(df)

        # For doing the sorting based on View Count
        df_most_viewed = df.sort_values(by='VIEW_COUNT',ascending=False)[['CHANNEL_NAME','VIDEO_TITLE','VIEW_COUNT','VIDEO_LINK']].head(5)
        print(df_most_viewed.head())

        # Checking the most viewed video
        print(df[df.VIEW_COUNT == df.VIEW_COUNT.max()])

        # Grouping by channel ID
        index_max_view = df.groupby('CHANNEL_NAME')['VIEW_COUNT'].idxmax()
        df_max_view_count_records = df.loc[index_max_view]

        print(df_max_view_count_records[['CHANNEL_NAME','VIDEO_TITLE','VIEW_COUNT','VIDEO_LINK']])
    
    except Exception as e:
        print(f"Error during fetching most viewed videos: {e}")
        sys.exit(1)  # Terminate program if fetching most viewed videos fails

    return df_most_viewed, df_max_view_count_records

def main():
    try:
        API_KEY, CHANNEL_ID, EXTRACTED_DATA, YOUTUBE = config()
        df = get_channel_details(API_KEY, CHANNEL_ID, EXTRACTED_DATA, YOUTUBE)
        df_most_viewed, df_max_view_count_records = fetching_most_viewed_videos(df)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()