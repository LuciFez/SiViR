import sys

sys.path.append('../')
import requests
import json


def instagramAPI(tag):
    creds = setCreds()

    # r = getToken(creds) #short life token
    # getLongToken(creds) #long life token
    #getUserPages(creds) #get page id to get Instagram Account ID
    #getInstagramAccount(creds) #get instagram account id

    tag_id = getHashTacgInfo(creds,tag)

    return getHashTagMedia(creds,tag_id,'top_media')

def getHashTagMedia(creds,tag_id,type):
    creds['debug'] = 'no'
    endpointParams = dict()
    endpointParams['user_id'] = creds['instagram_id']
    endpointParams['fields'] = 'id,children,caption,comment_count,like_count,media_type,media_url,permalink'
    endpointParams['access_token'] = creds['access_token']

    url = creds['endpoint_base'] + tag_id + '/'+type

    response = makeApiCall(url, endpointParams, creds['debug'])

    return response


def getHashTacgInfo(creds,tag):
    creds['debug'] = 'no'
    endpointParams = dict()
    endpointParams['user_id'] = creds['instagram_id']
    endpointParams['q'] = tag
    endpointParams['fields'] = 'id,name'
    endpointParams['access_token'] = creds['access_token']

    url = creds['endpoint_base'] + 'ig_hashtag_search'

    response = makeApiCall(url, endpointParams, creds['debug'])
    return response['json_data']['data'][0]['id']

def getInstagramAccount(creds):
    creds['debug'] = 'yes'
    endpointParams = dict()
    endpointParams['access_token'] = creds['access_token']
    endpointParams['fields'] = 'instagram_business_account'

    url = creds['endpoint_base'] + creds['page_id']

    response = makeApiCall(url, endpointParams, creds['debug'])
    return response


def getUserPages(creds):
    creds['debug'] = 'no'
    endpointParams = dict()
    endpointParams['access_token'] = creds['access_token']

    url = creds['endpoint_base'] + 'me/accounts'

    response = makeApiCall(url, endpointParams, creds['debug'])
    return response

def getLongToken(creds):
    creds['debug'] = 'no'  # tes - apare no - nu apare debug
    endpointParams = dict()
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = creds['client_id']
    endpointParams['client_secret'] = creds['client_secret']
    endpointParams['fb_exchange_token'] = creds['access_token']

    url = creds['endpoint_base'] + 'oauth/access_token'

    response = makeApiCall(url, endpointParams, creds['debug'])
    return response

def getToken(creds):
    creds['debug'] = 'no' # tes - apare no - nu apare debug
    endpointParams = dict()
    endpointParams['input_token'] = creds['access_token']
    endpointParams['access_token'] = creds['access_token']

    url = creds['graph_domain'] + '/debug_token'

    response = makeApiCall(url, endpointParams, creds['debug'])
    return response

def setCreds():
    creds = dict()
    creds['access_token'] = 'EAAJ2H6BCQIYBAHVxP78rT1hIdv3ZC89MfWhhS8ZBS09o8w0ZB4fMZCIxfITFHQYkfOckWb9p7C9ll8I1ZBKAY59kPosXAw8M2jEYMjbGJBvSHhY8LPt0NMzgDVooGXZBfPGKqZAtTGRUlKjyLgaJNjY7c88nFxIePotHutKH7aKzqgMdBZAWeZC3d'
    creds['client_id'] = '692828158181510'
    creds['client_secret'] = 'b266ec7184de14a4148f7fb7c5f3ed03'
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v6.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] +'/'
    creds['debug'] = 'no'
    creds['page_id'] = '113276420415566'
    creds['instagram_id'] = '17841436959535519'
    return creds

def makeApiCall(url,endpointParams, debug = 'no'):
    data = requests.get(url,endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams,indent=4)
    response['json_data'] = json.loads(data.content.decode('utf-8'))
    response['json_data_pretty'] = json.dumps(response['json_data'],indent=4)

    if('yes'==debug):
        displayApiCallData(response)

    return response

def displayApiCallData(response):
    print("\nURL: ")
    print(response['url'])
    print("\nEndpoint Params: ")
    print(response['endpoint_params_pretty'])
    print("\nJSON DATA: ")
    print(response['json_data_pretty'])

def getEmbeddings(url):
    response = requests.get("https://api.instagram.com/oembed?url="+url+"&access_token=EAAJ2H6BCQIYBAHVxP78rT1hIdv3ZC89MfWhhS8ZBS09o8w0ZB4fMZCIxfITFHQYkfOckWb9p7C9ll8I1ZBKAY59kPosXAw8M2jEYMjbGJBvSHhY8LPt0NMzgDVooGXZBfPGKqZAtTGRUlKjyLgaJNjY7c88nFxIePotHutKH7aKzqgMdBZAWeZC3d")
    return response