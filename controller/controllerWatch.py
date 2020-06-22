import sys
import json
sys.path.append('../')
from model.util import checkJWT
from model.youtubeAPI import videoPlayer, getcomments,getRecommendation
from model.similarity import calculateSimilarity


def controllerWatch(environ, start_response):
    params = environ['params']
    user = checkJWT(environ)
    if not user:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Not logged in."}
        yield json.dumps(message).encode('utf-8')
    if 'v' in params:
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
        print(video)
        print(videos)

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
        html = template.format(id=id, title=video['title'], description=video['description'], comments=commentsHTML, recommendations=html_videos)
        yield html.encode('utf-8')
    else:
        start_response("400 Bad Request", [('Content-text', 'text/plain')])
        message = {"message": "Empty query"}
        yield json.dumps(message).encode('utf-8')