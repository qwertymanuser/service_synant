from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Word
from .serializers import WordSerializer

class WordListCreateAPIView(APIView):
    def get(self, request):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

words_data = [
    {"word": "happy", "synonyms": ["joyful", "content"], "antonyms": ["sad", "unhappy"]},
    {"word": "good", "synonyms": ["excellent", "great"], "antonyms": ["bad", "poor"]},
]

class WordStaticDataAPIView(APIView):
    def get(self, request):
        return Response(words_data)