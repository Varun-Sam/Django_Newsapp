from django.shortcuts import render

# Create your views here.
from newsapi import NewsApiClient


# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='d9c2f5465dba4dd7ad07f7b692636c09')
    top = newsapi.get_top_headlines(sources='')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})