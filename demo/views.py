import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_external_api(request):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    return Response(response.json())

@api_view(['POST'])
def create_post(request):
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.post(url, json=request.data)
    return Response(response.json())
