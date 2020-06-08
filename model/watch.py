import googleapiclient.discovery

def videoPlayer(id):
    api_key = 'AIzaSyDneNr5blVqIK3Khyfht4r3kR91PR_qWgM'
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

    request = youtube.videos().list(
        part="snippet, statistics",
        id=id
    )
    response = request.execute()
    response = response['items'][0]
    print(response)
   # results = [{'id': i['id']['videoId'], 'thumbnail': i['snippet']['thumbnails']['medium'], 'title':i['snippet']['title'], 'description':i['snippet']['description']} for i in response['items']]
    result = {'title': response['snippet']['title'], 'description': response['snippet']['description']}
    return result