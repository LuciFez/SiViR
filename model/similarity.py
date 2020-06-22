from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


def calculateSimilarity(info_video, suggestions):
    info_video = info_video['title'] + ' ' + info_video['description']
    info_videos = [info_video]

    for suggestion in suggestions:
        info_suggestion = suggestion['title'] + ' ' + suggestion['description'].replace('\n', ' ')
        info_videos.append(info_suggestion)
    df = pd.DataFrame(info_videos)
    vectorizer = CountVectorizer(analyzer='word')

    X = vectorizer.fit_transform(df[0])
    cosine_sim = cosine_similarity(X[1:], X[0])
    similarity = list(enumerate(cosine_sim))

    for i in range(len(suggestions)):
        suggestions[i]['similarity'] = similarity[i][1][0]
    similarity.sort(key=lambda x: x[1], reverse=True)
    return suggestions



