from django.contrib import admin
from .models import SearchHistory, Bookmark

# Register your models here.
admin.site.register(SearchHistory)
admin.site.register(Bookmark)