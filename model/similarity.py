from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def calculateSimilarity(info_video, suggestions):
    info_video = info_video['title'] + ' ' + info_video['description']
    info_videos = [info_video]

    for suggestion in suggestions:
        info_suggestion = suggestion['title'] + ' ' + suggestion['description']
        info_videos.append(info_suggestion)

    print(info_videos)
    df = pd.DataFrame(info_videos)
    vectorizer = CountVectorizer(analyzer='word')

    X = vectorizer.fit_transform(df[0])
    cosine_sim = cosine_similarity(X[1:], X[0])
    similarity = list(enumerate(cosine_sim))

    similarity.sort(key=lambda x: x[1], reverse=True)
    return suggestions

if __name__ == '__main__':

    print(calculateSimilarity(
        {"title": "muie mie", "description": "jhasuhifjbsavgguhoicnbbib j e fsgsddf  db df b dtndbfvd"},
        [{"title": "muie mie", "description": "jhasuhifjbsavgguhoicnbbib j e fsgsddf  db df b dtndbfvd"},
         {"title": "muie tie", "description": "jhassfhoicnbbib j e fsgsddf  db dsaf b sda"}]))


