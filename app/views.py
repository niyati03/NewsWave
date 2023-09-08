import requests
from django.shortcuts import render

def fetch_news(api_url):
    response = requests.get(api_url)
    news_data = response.json()
    return news_data

def entertainment_news(request):
    api_url = "https://inshorts.me/news/topics/entertainment" 
    news_data = fetch_news(api_url)
    articles = news_data['data']['articles']
    return render(request, 'entertainment_news.html', {'articles': articles})

def top_news(request):
    api_url = "https://inshorts.me/news/top?offset=0&limit=21"
    news_data = fetch_news(api_url)
    articles = news_data['data']['articles']
    return render(request, 'top_news.html', {'articles': articles})


def all_news(request):
    api_url = "https://inshorts.me/news/all?offset=0&limit=21"
    news_data = fetch_news(api_url)
    articles = news_data['data']['articles']
    return render(request, 'all_news.html', {'articles': articles})

def trending_news(request):
    api_url = "https://inshorts.me/news/trending?offset=0&limit=21"
    news_data = fetch_news(api_url)
    articles = news_data['data']['articles']
    return render(request, 'trending_news.html', {'articles': articles})

def science_news(request):
    api_url = "https://inshorts.me/news/topics/science"
    news_data = fetch_news(api_url)
    articles = news_data['data']['articles']
    return render(request, 'science_news.html', {'articles': articles})

def sports_news(request):
    api_url = "https://inshorts.me/news/topics/sports"
    news_data = fetch_news(api_url)
    articles = news_data['data']['articles']
    return render(request, 'sports_news.html', {'articles': articles})

