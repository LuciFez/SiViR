import sys
import json
sys.path.append('../')
from model.util import checkJWT
from model.youtubeAPI import videoPlayer, getcomments,getRecommendation
from model.vimeoApi import *
from model.similarity import calculateSimilarity
from controller.controllerRSS import setRSS


def controllerWatch(environ, start_response):
    params = environ['params']
    user = checkJWT(environ)
    if not user:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Not logged in."}
        yield json.dumps(message).encode('utf-8')
    if 'v' in params:
        if 'https://vimeo.com/'in params['v']:
            start_response('200 OK', [('Content-text', 'text/plain')])

            template = open("view/watch/comment.html", "r").read()
            comments = getComments(params['v'])
            commentsHTML = ""
            for i in comments['data']:
                comment = template.format(author=i['user']['name'], text=i['text'])
                commentsHTML += comment

            recommendation = getRecommendationVimeo(params['v'])
            #RSSSSSSSSSSSSSSSSSSSSSSS
            #SIMILARITYYYYYYYYYYYYYYYYYYYYY
            template = open("view/search/video.html", "r").read()
            html_videos = ""
            for i in recommendation['data']:
                html_video = template.format(id=i['link'],
                                             srcthumbnail=i['pictures']['sizes'][-1]['link'],
                                             title=i['name'],
                                             similarity='0.00',
                                             description=i['description'])
                html_videos += html_video

            template = open("view/watch/watch.html", "r").read()
            html = template.format(id='https://player.vimeo.com/video/'+params['v'][18:], title='TITLU', description='DESCRIERE', comments=commentsHTML,recommendations=html_videos)
            yield html.encode('utf-8')


        else:
            start_response('200 OK', [('Content-text', 'text/plain')])

            id = params['v']
            video = videoPlayer(id)

            template = open("view/watch/comment.html", "r").read()

            comments = getcomments(id)
            commentsHTML = ""
            for i in comments:
                comment = template.format(author=i['author'], text=i['text'])
                commentsHTML += comment

            videos = getRecommendation(id)
            setRSS(videos)

            videos = calculateSimilarity(video, videos)
            template = open("view/search/video.html", "r").read()

            html_videos = ""
            for i in videos:
                html_video = template.format(id=i['id'],
                                            srcthumbnail=i['thumbnail'],
                                            title=i['title'],
                                            similarity = i['similarity'],
                                            description=i['description'])
                html_videos += html_video

            template = open("view/watch/watch.html", "r").read()
            html = template.format(id='https://www.youtube.com/embed/'+id+'?autoplay=1&loop=1', title=video['title'], description=video['description'], comments=commentsHTML, recommendations=html_videos)
            yield html.encode('utf-8')
    else:
        start_response("400 Bad Request", [('Content-text', 'text/plain')])
        message = {"message": "Empty query"}
        yield json.dumps(message).encode('utf-8')