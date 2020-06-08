import sys
sys.path.append('../')


def controllerQuestions(environ, start_response):
    start_response('200 OK', [('Content-text', 'text/html')])
    file = open("view/questionsPage/questionsPage.html","r").read()
    yield file.encode('utf-8')