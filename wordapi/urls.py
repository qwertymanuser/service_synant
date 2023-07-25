from django.urls import path
from .views import WordListCreateAPIView, WordStaticDataAPIView

urlpatterns = [
    path('words/', WordListCreateAPIView.as_view(), name='word-list-create'),
    path('words/static/', WordStaticDataAPIView.as_view(), name='word-static-data'),
]