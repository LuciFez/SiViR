import vimeo

def vimeoSearch(query):
    client = vimeo.VimeoClient(
        token='1a028b267f6e92a4f90389b031d33b60',
        key='a591a007d8a09bc7fd57c50d325180224bdffa25',
        secret='4IWycSdPpr9m73k/5TTQF+WBUV631kUtK4EQETBVhzmweZXTiOZp7jYYSP3cEXrzSLfS2IrQh1lnVPevXvZPbyRJV3UKWYwfhzHr68nUHSHg+Srm3BvqOiPvc8gAjWH3'
    )
    'videos?direction=asc&filter=trending&page=1&per_page=10&query=cat&sort=likes'
    res = client.get('/videos?direction=asc&filter=trending&page=1&per_page=10&query='+query+'&sort=likes')
    jsonData = res.json()

    results = [{'id': i['link'],
                'thumbnail': i['pictures']['sizes'][6]['link'],
                'title': i['name'],
                'description': i['description']}
               for i in jsonData['data']]
    return results

def getComments(id):
    client = vimeo.VimeoClient(
        token='1a028b267f6e92a4f90389b031d33b60',
        key='a591a007d8a09bc7fd57c50d325180224bdffa25',
        secret='4IWycSdPpr9m73k/5TTQF+WBUV631kUtK4EQETBVhzmweZXTiOZp7jYYSP3cEXrzSLfS2IrQh1lnVPevXvZPbyRJV3UKWYwfhzHr68nUHSHg+Srm3BvqOiPvc8gAjWH3'
    )
    res = client.get('/videos/' + id[18:]+'/comments')
    jsonData = res.json()

    return jsonData



def getRecommendationVimeo(id):
    client = vimeo.VimeoClient(
        token='1a028b267f6e92a4f90389b031d33b60',
        key='a591a007d8a09bc7fd57c50d325180224bdffa25',
        secret='4IWycSdPpr9m73k/5TTQF+WBUV631kUtK4EQETBVhzmweZXTiOZp7jYYSP3cEXrzSLfS2IrQh1lnVPevXvZPbyRJV3UKWYwfhzHr68nUHSHg+Srm3BvqOiPvc8gAjWH3'
    )
    res = client.get('/videos/' + id[18:]+'/videos?filter=related&page=1&per_page=10')
    jsonData = res.json()
    return jsonData