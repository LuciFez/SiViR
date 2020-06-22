import googleapiclient.discovery

def buildAPI():
    api_key = ''
    api_service_name = "youtube"
    api_version = "v3"

    return googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)


def searchVideo(user, q, regioncode='ro'):
    youtube = buildAPI()

    request = youtube.search().list(
        part="snippet",
        q=q,
        maxResults=10,
        regionCode=regioncode,
        type="video"
    )
    response = request.execute()
    results = [{'id': i['id']['videoId'],
                'thumbnail': i['snippet']['thumbnails']['medium']['url'],
                'title':i['snippet']['title'],
                'description':i['snippet']['description']}
               for i in response['items']]
    return results

def videoPlayer(id):
    youtube = buildAPI()

    request = youtube.videos().list(
        part="snippet",
        id=id
    )
    response = request.execute()
    response = response['items'][0]
    result = {'title': response['snippet']['title'],
              'description': response['snippet']['description']}
    return result

def getcomments(id):
    youtube = buildAPI()

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=5,
        order="relevance",
        videoId=id
    )

    response = request.execute()
    response = response['items']
    comments = list()
    for i in response:
        i = i['snippet']['topLevelComment']['snippet']
        comments.append({'author': i['authorDisplayName'], 'text': i['textOriginal']})

    return comments


def getRecommendation(id, regioncode='ro'):
    youtube = buildAPI()

    request = youtube.search().list(
        part="snippet",
        maxResults=10,
        regionCode=regioncode,
        relatedToVideoId=id,
        type="video"
    )

    response = request.execute()
    results = [{'id': i['id']['videoId'],
                'thumbnail': i['snippet']['thumbnails']['high']['url'],
                'title':i['snippet']['title'],
                'description':i['snippet']['description']}
               for i in response['items']]

    return results