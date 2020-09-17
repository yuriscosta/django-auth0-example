from django.urls import include, path

from .views import index, logout, PostListView

urlpatterns = [
    path('', index),
    path('codes', PostListView.as_view()),
    path('logout', logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
