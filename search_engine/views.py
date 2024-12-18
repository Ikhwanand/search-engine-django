from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import SearchHistory, Bookmark
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import re
import json
# Create your views here.

def search_view(request):
    query = request.GET.get('q', '')
    def search(query):
        # this function to search the query for website
        if not query:
            return []
    
        search_results = []
        try:
            # Format the search query for URL
            formatted_query = quote_plus(query)
            
            # Get multiple pages of results
            for page in range(3):  # Get 3 pages of results
                # Make request to Google with page parameter
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/5.37.36'
                }
                url = f'https://www.google.com/search?q={formatted_query}&start={page * 10}'
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    
                    # Find all search result divs
                    search_divs = soup.find_all('div', class_='g')
                    
                    for div in search_divs:
                        try:
                            # Rest of the extraction code remains the same
                            title_element = div.find('h3')
                            if not title_element:
                                continue
                            title = title_element.text 
                            
                            link_element = div.find('a')
                            if not link_element:
                                continue
                            link = link_element.get('href')
                            if link.startswith('/url?q='):
                                link = link.split('/url?q')[1].split('&')[0]
                                
                            desc_element = div.find('div', class_='VwiC3b')
                            description = desc_element.text if desc_element else ''
                            
                            if title and link:
                                search_results.append({
                                    'title': title,
                                    'url': link,
                                    'description': description,
                                })
                        except Exception as e:
                            continue
                
                # Add a small delay between requests to be polite
                import time
                time.sleep(0.1)
        
        except Exception as e:
            print(f"Search error: {str(e)}")
        
        return search_results
        
    if query:
        # Save search query to history
        if request.user.is_authenticated:
            SearchHistory.objects.create(user=request.user, query=query)
        # Call your search function here and get results
        results = search(query)
        
        # Set up pagination
        paginator = Paginator(results, 10) # show 10 results per page
        page = request.GET.get('page', 1)
        try:
            paginated_results = paginator.page(page)
        except PageNotAnInteger:
            paginated_results = paginator.page(1)
        except EmptyPage:
            paginated_results = paginator.page(paginator.num_pages)
            
        return render(request, 'search_engine/search_results.html', 
                      {'query': query,
                       'page_obj': paginated_results,}
                    )
    return render(request, 'search_engine/search.html')


@login_required
def history_view(request):
    if request.user.is_authenticated:
        history = SearchHistory.objects.filter(user=request.user).order_by('-timestamp')
    else:
        history = []
    return render(request, 'search_engine/history.html', {'history': history})

@login_required
def bookmarks_view(request):
    if request.user.is_authenticated:
        bookmarks = Bookmark.objects.filter(user=request.user).order_by('-timestamp')
    else:
        bookmarks = []
    return render(request, 'search_engine/bookmarks.html', {'bookmarks': bookmarks})

@login_required
def add_bookmark(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                title = data.get('title')
                url = data.get('url')
            else:
                title = request.POST.get('title')
                url = request.POST.get('url')
            
            if not title or not url:
                return JsonResponse({
                    'success': False,
                    'error': 'Title and URL are required'
                }, status=400)
            
            #  Validate URL format
            try:
                URLValidator()(url)
            except ValidationError:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid URL format'
                }, status=400)
            
            # Check for duplicate bookmark
            if Bookmark.objects.filter(user=request.user, url=url).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'Bookmark already exists'
                }, status=400)
            
            # create bookmkar
            Bookmark.objects.create(
                user=request.user,
                title=title,
                url=url,
            )
            
            return JsonResponse({'success': True})
        
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON data'
            }, status=400)
        
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False,
        'error': 'Only POST method is allowed'
    }, status=405)
    

@login_required
def delete_bookmark(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            bookmark_id = data.get('bookmark_id')

            bookmark = Bookmark.objects.get(id=bookmark_id, user=request.user)
            bookmark.delete()

            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Invalid JSON data'
            }, status=400)

        except Bookmark.DoesNotExist:
            return JsonResponse({
                'success': False,
                'error': 'Bookmark does not exist'
            }, status=404)

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)

    return JsonResponse({
        'success': False,
        'error': 'Only POST method is allowed'
    }, status=405)
    

@login_required
def clear_history(request):
    if request.method == 'POST':
        try:
            # Clear the search history for the current user
            SearchHistory.objects.filter(user=request.user).delete()

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)

    return JsonResponse({
        'success': False,
        'error': 'Only POST method is allowed'
    }, status=405)