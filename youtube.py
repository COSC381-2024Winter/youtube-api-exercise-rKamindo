import argparse
import sys
import json
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY =  config.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)
    
    # call the search.list method to retrieve results matching the specified query term
    search_response = youtube.search().list(
        q=query_term,
        part='id, snippet',
        maxResults=max_results
    ).execute()

    search_list = []
    for search_item in search_response["items"]:
        search_list.append(search_item)
    
    if len(search_list) < int(max_results):
        print("No more results")
    
    return search_list

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    response = youtube_search(query_term, max_results)
    with open('response.json', 'w') as file: # outputs response json to a file for 
        json.dump(response, file, indent=4)
