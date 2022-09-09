from django.urls import path
from tutorials import views

urlpatterns = [
    path('', views.TutorialListView.as_view(), name='tutorials'),
    path('tutorial/<slug:year>/<slug:month>/<slug:day>/<slug:author>/<slug:slug>/',
         views.TutorialDetailView.as_view(), name='tutorial_detail'),
    path('favourites/<slug:slug>/', views.favourite_tutorials, name='favourites'),
    path('search/', views.TutorialSearchView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', views.tagged, name='tagged'),
]