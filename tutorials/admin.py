from django.contrib import admin
from tutorials.models import Favourite, Tutorial, TutorialComments

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'views', 'created',]
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created', 'updated', 'tags']
    search_fields = ['title', 'author', 'tags']
    
admin.site.register(Favourite)
admin.site.register(TutorialComments)