import requests
from django.shortcuts import render
from django.http import JsonResponse




API_KEY = '7dc6bbaa392d097570d0624e80c99577'  # Your GNews API key

def get_news(query=None):
    url = f'https://gnews.io/api/v4/search?q={query}&token={API_KEY}' if query else f'https://gnews.io/api/v4/top-headlines?token={API_KEY}'
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")  # Print the response content
    
    if response.status_code == 200:
        return response.json().get('articles', [])
    return []

def home(request):
    query = request.GET.get('q')  # Get the search query from the URL
    news_articles = get_news(query)  # Fetch news articles using the GNews API

    context = {
        'articles': news_articles,
        'query': query or ''
    }
    
    return render(request, 'news/home.html', context)


# def get_news(query=None):
#     url = f'https://gnews.io/api/v4/search?q={query}&token={API_KEY}' if query else f'https://gnews.io/api/v4/top-headlines?token={API_KEY}'
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         return response.json().get('articles', [])
#     else:
#         print(f"Error fetching data from API: {response.status_code}")
#         return []
