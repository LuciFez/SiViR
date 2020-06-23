import sys
import json
sys.path.append('../')
from model.youtubeAPI import *
from model.util import checkJWT
from model.instagramApi import *
from model.vimeoApi import *


# def controllerSearch(environ, start_response):
#     params = environ['params']
#     user = checkJWT(environ)
#     if not user:
#         start_response('401 Unauthorized', [('Content-text', 'text/plain')])
#         message = {"message": "Bad username or password"}
#         yield json.dumps(message).encode('utf-8')
#     if 'q' in params:
#             videos = searchVideo('inca nu e relevant', params['q'])
#             template = open("view/search/video.html", "r").read()
#             html_videos = ""
#
#             for i in videos:
#                 html_video = template.format(id=i['id'],
#                                             srcthumbnail=i['thumbnail']['url'],
#                                             title=i['title'],
#                                             description=i['description'])
#                 html_videos += html_video
#
#             start_response('200 OK', [('Content-text', 'text/plain')])
#             yield html_videos.encode('utf-8')
#
#             responseInsta = instagramAPI('video')
#             for a in responseInsta['json_data']['data']:
#                 if a['media_type'] == "VIDEO":
#                     if 'permalink' in a:
#                         response = getEmbeddings(a['permalink']).content.decode('utf-8')
#                         if response != 'No Media Match':
#                             x = json.loads(response)
#                             print(x['html'])
#                             html_videos += x['html']
#
#             html = open("view/search/search.html", "r").read().format(videos=html_videos)
#
#
#
#             vimeoJson = vimeoFirst('Cat')
#             for a in vimeoJson['data']:
#                 if 'link' in a:
#                     print(a)
#             start_response('200 OK', [('Content-text', 'text/plain')])
#             yield html.encode('utf-8')
#     else:
#         start_response("400 Bad Request", [('Content-text', 'text/plain')])
#         message = {"message": "Empty query"}
#         yield json.dumps(message).encode('utf-8')


def controllerSearch(environ, start_response):
    params = environ['params']
    user = checkJWT(environ)
    if not user:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Bad username or password"}
        yield json.dumps(message).encode('utf-8')
    if 'q' in params:
            #videosYT = {'videos': searchVideo('inca nu e relevant', params['q'])}
            videosVIM = {'videos': vimeoSearch(params['q'])}
            start_response('200 OK', [('Content-text', 'text/plain')])
            yield json.dumps(videosVIM).encode('utf-8')
    else:
        start_response("400 Bad Request", [('Content-text', 'text/plain')])
        message = {"message": "Empty query"}
        yield json.dumps(message).encode('utf-8')