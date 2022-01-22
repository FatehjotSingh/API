import csv

all_articles = []
file = open('articles.csv')
reader = csv.reader(file)

data = list(reader)
all_articles = data[1:]

liked_articles = []
disliked_articles = []