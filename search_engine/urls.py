from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'engine'
urlpatterns = [
    path('', views.search_view, name='search'),
    path('history/', views.history_view, name='history'),
    path('history/clear/', views.clear_history, name='clear_history'),
    path('bookmarks/', views.bookmarks_view, name='bookmarks'),
    path('bookmarks/add/', views.add_bookmark, name='add_bookmark'),
    path('bookmarks/delete/', views.delete_bookmark, name='delete_bookmark'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/password_change.html', success_url='/password_change/done/'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),
]