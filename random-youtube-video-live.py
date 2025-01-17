#!/usr/bin/env python3

from googleapiclient.discovery import build
import random

DEVELOPER_KEY = 'YOUR_DEVELOPER_KEY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

prefix = ['live', 'webcam', 'test', 'stream']

def youtube_search():
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q=random.choice(prefix),
    part='snippet',
    maxResults=5,
    type='video',
    eventType='live'
  ).execute()


  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))
  return (videos[random.randint(0, 2)])

print(youtube_search())
