from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

# view all the articles
@api_view(['GET', 'POST'])
def articleList(request):
    """
    List all code snippets, or create a new snippet.
    """

    # check if it passes the GET method
    if request.method == 'GET':
        # query all articles
        articles = Article.objects.all()
        # then serialize the articles
        serializer = ArticleSerializer(articles, many=True)
        # return the serialized data as Response
        return Response(serializer.data)

    # check if request passes the POST method (for creating new)
    elif request.method == 'POST':
        # pass the data to serializer
        serializer = ArticleSerializer(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            # return the JsonResponse and created status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid return error status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view only specific article
@api_view(['GET', 'PUT', 'DELETE'])
def articleDetatil(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        # query the specific article
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # check if request passes the GET method (for getting detail)
    if request.method == 'GET':
        # then serialize the article
        serializer = ArticleSerializer(article)
        # return the serialized data as JsonResponse
        return Response(serializer.data)

    # check if request passes the POST method (for update)
    elif request.method == 'PUT':
        # pass the data to serializer
        serializer = ArticleSerializer(article, data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            # return the JsonResponse and created status 201
            return Response(serializer.data)
        # if not valid return error status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
