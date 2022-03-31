from django.urls import path

from music_app.views import MusicListView, MusicUpdateView, MusicDetailView, MusicDeleteView

urlpatterns =[
     path('music/', MusicListView.as_view()),
     path('music-update/<int:pk>/', MusicUpdateView.as_view()),
     path('music-detail/<int:pk>/', MusicDetailView.as_view()),
     path('music-delete/<int>:id>/', MusicDeleteView.as_view()),

]