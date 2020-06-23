import sys
from rfeed import *

feed = Feed(
    title="",
    link="",
    description=""
)

def setRSS(yVideos):
    itemList = []
    for i in yVideos:
        item = Item(
            title = i['title'],
            link = "https://www.youtube.com/watch?v="+i['id'],
            description = i['description']
        )
        itemList.append(item)
    feed = Feed(
        title = "RSS",
        link="google.com",
        description = "RSS",
        language = "en-US",
        items = itemList
    )
    print(feed.rss())

def getRSS():
    yield rssFeed.encode('utf-8')