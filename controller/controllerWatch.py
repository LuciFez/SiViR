import sys
import json

sys.path.append('../')
from model.util import checkJWT
from model.youtubeAPI import *
from model.vimeoApi import *
from model.similarity import *
from rfeed import *


def controllerWatch(environ, start_response):
    params = environ['params']
    user = checkJWT(environ)
    if not user:
        start_response('401 Unauthorized', [('Content-text', 'text/plain')])
        message = {"message": "Not logged in."}
        yield json.dumps(message).encode('utf-8')
    if 'v' in params:
        if 'https://vimeo.com/' in params['v']:
            start_response('200 OK', [('Content-text', 'text/plain')])

            video = getVideo(params['v'])

            template = open("view/watch/comment.html", "r").read()
            comments = getComments(params['v'])
            commentsHTML = ""
            for i in comments['data']:
                comment = template.format(author=i['user']['name'], text=i['text'])
                commentsHTML += comment

            recommendation = getRecommendationVimeo(params['v'])

            ytRECOM = searchVideo(video['name'])
            # RSSSSSSSSSSSSSSSSSSSSSSS

            v = {'title': video['name'],
                 'description': video['description']}

            rec = [{'title': i['name'],
                    'description': i['description']}
                   for i in recommendation['data']]
            vimeoSim = calculateSimilarity(v, rec)
            ytRECOM = calculateSimilarity(v, ytRECOM)

            template = open("view/search/video.html", "r").read()
            html_videos = ""
            index = 0
            for i in recommendation['data']:
                if i['description']:
                    html_video = template.format(id=i['link'],
                                             srcthumbnail=i['pictures']['sizes'][-1]['link'],
                                             title=i['name'],
                                             similarity=vimeoSim[index]['similarity'],
                                             description=i['description'])
                    index= index+1
                else:
                    html_video = template.format(id=i['link'],
                                                 srcthumbnail=i['pictures']['sizes'][-1]['link'],
                                                 title=i['name'],
                                                 similarity='N/A',
                                                 description=i['description'])
                html_videos += html_video

            for i in ytRECOM:
                if i['description']:
                    html_video += template.format(id=i['id'],
                                             srcthumbnail=i['thumbnail'],
                                             title=i['title'],
                                             similarity=i['similarity'],
                                             description=i['description'])
                    index= index+1
                else:
                    html_video += template.format(id=i['id'],
                                             srcthumbnail=i['thumbnail'],
                                             title=i['title'],
                                             similarity='N/A',
                                             description=i['description'])
                html_videos += html_video

            template = open("view/watch/watch.html", "r").read()
            html = template.format(id='https://player.vimeo.com/video/' + params['v'][18:], title=video['name'],
                                   description=video['description'], comments=commentsHTML, recommendations=html_videos)
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

            videos = getRecommendationVideo(id)

            videos = calculateSimilarity(video, videos)
            template = open("view/search/video.html", "r").read()

            html_videos = ""
            for i in videos:
                html_video = template.format(id=i['id'],
                                             srcthumbnail=i['thumbnail'],
                                             title=i['title'],
                                             similarity=i['similarity'],
                                             description=i['description'])
                html_videos += html_video

            recommendationVIMEO = vimeoSearch(video['title'])


            rec = [{'title': i['title'],
                    'description': i['description']}
                   for i in recommendationVIMEO]
            sim = calculateSimilarity(video, rec)
            index = 0
            for i in recommendationVIMEO:
                if i['description']:
                    html_video = template.format(id=i['id'],
                                                 srcthumbnail=i['thumbnail'],
                                                 title=i['title'],
                                                 similarity=sim[index]['similarity'],
                                                 description=i['description'])
                    index = index + 1
                else:
                    html_video = template.format(id=i['id'],
                                                 srcthumbnail=i['thumbnail'],
                                                 title=i['title'],
                                                 similarity='N/A',
                                                 description=i['description'])
                html_videos += html_video

            itemList = []
            for i in videos:
                item = Item(
                    title=i['title'],
                    link="https://www.youtube.com/watch?v=" + i['id'],
                    description=i['description']
                )
                itemList.append(item)
            for i in recommendationVIMEO:
                item = Item(
                    title=i['title'],
                    link=i['id'],
                    description=i['description']
                )
            feed = Feed(
                title="RSS",
                link="google.com",
                description="RSS",
                language="en-US",
                items=itemList
            )
            f = open("view/img/rss.txt", "r+", encoding='utf-8',  errors='ignore')
            f.truncate(0)
            f.write(feed.rss())
            f.close()

            template = open("view/watch/watch.html", "r").read()
            html = template.format(id='https://www.youtube.com/embed/' + id + '?autoplay=1&loop=1',
                                   title=video['title'], description=video['description'], comments=commentsHTML,
                                   recommendations=html_videos)
            yield html.encode('utf-8')
    else:
        start_response("400 Bad Request", [('Content-text', 'text/plain')])
        message = {"message": "Empty query"}
        yield json.dumps(message).encode('utf-8')
