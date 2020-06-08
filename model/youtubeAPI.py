
import googleapiclient.discovery
import json

def searchVido(user, q, regioncode='us', ):
    api_key = 'AIzaSyDneNr5blVqIK3Khyfht4r3kR91PR_qWgM'
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        q=q,
        maxResults=10,
        regionCode=regioncode,
        type="video"
    )
    response = request.execute()
    print(response)
    results = [{'id': i['id']['videoId'], 'thumbnails': i['snippet']['thumbnails']['high'], 'title':i['snippet']['title'], 'description':i['snippet']['description']} for i in response['items']]

    for i in results:
        print(i)

    return json.dumps(results)


if __name__ == '__main__':
    searchVido('dads', 'dani mocanu')