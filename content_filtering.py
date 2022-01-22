from sklearn.feature_extraction.text import CountVectorizer as cvz
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as csy

df = pd.read_csv('articles.csv')
df = df[df['soup'].notna()]

count = cvz(stop_words = 'english')
count_matrix = count.fit_transform(df['soup'])

cosine_sim = csy(count_matrix ,count_matrix)

df = df.reset_index()
indices = pd.Series(df.index,index = df['contentId'])

def get_recommendations(contentId):
  idx = indices[int(contentId)]
  sim_scores = list(enumerate(cosine_sim[idx]))
  sim_scores = sorted(sim_scores,key = lambda x:x[1],reverse = True)
  sim_scores = sim_scores[1:11]
  article_indices = [i[0] for i in sim_scores]
  return df[['url','title','text','lang','total_events']].iloc[article_indices].values.tolist()