import sys
import json
sys.path.append('../')
from model.youtubeAPI import *
from model.util import checkJWT
from model.instagramApi import *
from model.vimeoApi import *


def controllerSearch(environ, start_response):
    params = environ['params']
    user = checkJWT(environ)
    if not user:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Bad username or password"}
        yield json.dumps(message).encode('utf-8')
    if 'q' in params:
            videos = searchVideo('inca nu e relevant', params['q'])
            template = open("view/search/video.html", "r").read()
            html_videos = ""

            for i in videos:
                html_video = template.format(id=i['id'],
                                            srcthumbnail=i['thumbnail']['url'],
                                            title=i['title'],
                                            description=i['description'])
                html_videos += html_video

            html = open("view/search/search.html", "r").read().format(videos=html_videos)
            start_response('200 OK', [('Content-text', 'text/plain')])

            # responseInsta = instagramAPI('video')

            for a in responseInsta['json_data']['data']:
                if a['media_type'] == 'VIDEO':
                    if 'media_url' in a:
                        print(a['media_url'])
                    elif 'permalink' in a:
                        print(a['permalink'])

            vimeoJson = vimeoFirst('Cat')
            for a in vimeoJson['data']:
                if 'link' in a:
                    print(a)
            # for a in responseInsta['json_data']['data']:
            #     if a['media_type'] == 'VIDEO':
            #         print(a['media_url'])

            yield html.encode('utf-8')
    else:
        start_response("400 Bad Request", [('Content-text', 'text/plain')])
        message = {"message": "Empty query"}
        yield json.dumps(message).encode('utf-8')

