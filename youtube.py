import argparse
import sys
import json
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY =  config.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query_term, max_results, page_token=None):
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    
    # call the search.list method to retrieve results matching the specified query term
    search_response = youtube.search().list(
        q=query_term,
        part='id, snippet',
        maxResults=max_results,
        pageToken=page_token
    ).execute()
    
    next_page_token = search_response["nextPageToken"]
    print("page token: ",next_page_token)
    search_list = []
    for search_item in search_response["items"]:
        search_list.append(search_item)

    if len(search_list) == 0:
        print("No results")
    
    if len(search_list) < int(max_results):
        print("No more results")
    
    return search_list, next_page_token

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    next_page_token = None
    videos_list1, next_page_token = youtube_search(query_term, max_results)
    print(videos_list1)
    videos_list2, next_page_token = youtube_search(query_term, max_results, "CAEQAA")
    print(videos_list2)
