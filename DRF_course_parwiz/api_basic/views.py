from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

# view all the articles
@csrf_exempt
def articleList(request):
    # check if it passes the GET method
    if request.method == 'GET':
        # query all articles
        articles = Article.objects.all()
        # then serialize the articles
        serializer = ArticleSerializer(articles, many=True)
        # return the serialized data as JsonResponse
        return JsonResponse(serializer.data, safe=False)

    # check if request passes the POST method (for creating new)
    elif request.method == 'POST':
        # Parse the data before passing into serizluzer
        data = JSONParser().parse(request)
        # pass the data to serializer
        serializer = ArticleSerializer(data=data)
        # check if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            # return the JsonResponse and created status 201
            return JsonResponse(serializer.data, status=201)
        # if not valid return error status
        return JsonResponse(serializer.errors, status=400)

# view only specific article
@csrf_exempt
def articleDetatil(request, pk):
    try:
        # query the specific article
        article = Article.objects.get(id=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    # check if request passes the GET method (for getting detail)
    if request.method == 'GET':
        # then serialize the article
        serializer = ArticleSerializer(article)
        # return the serialized data as JsonResponse
        return JsonResponse(serializer.data)

    # check if request passes the POST method (for update)
    elif request.method == 'PUT':
        # Parse the data before passing into serizluzer
        data = JSONParser().parse(request)
        # pass the data to serializer
        serializer = ArticleSerializer(data=data)
        # check if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            # return the JsonResponse and created status 201
            return JsonResponse(serializer.data)
        # if not valid return error status
        return JsonResponse(serializer.errors, status=400)


    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
