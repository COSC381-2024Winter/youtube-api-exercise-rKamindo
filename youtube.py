import argparse
import sys
<<<<<<< Updated upstream
=======
import json
>>>>>>> Stashed changes
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

    for search_item in search_response["items"]:
        print(search_item)
    
    return search_response["items"]

if __name__ == "__main__":
    query_term = sys.argv[1]
    max_results = sys.argv[2]
    response = youtube_search(query_term, max_results)
    with open('response.json', 'w') as file: # outputs response json to a file for 
        json.dump(response, file, indent=4)
