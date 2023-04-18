from django.shortcuts import render
#from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
# Create your views here. 
def index(request):
      
    newsapi = NewsApiClient(api_key ='246ea430950d4fb2b40b90d6afa98c52')
    top = newsapi.get_top_headlines(sources ='techcrunch')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
  
    return render(request, 'index.html', context ={"mylist":mylist})