from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer


# Create your views here.

# same as ArticleAPIView (class based view)
class GenericAPIView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # authentication credentials
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # *args, **kwargs can also be omitted in case of basic view of form submission
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# same as ArticleDetailView (class based view)
class GenericAPIDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # authentication credentials 
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# same as articleList (function based view)
class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        # then serialize the articles
        serializer = ArticleSerializer(articles, many=True)
        # return the serialized data as Response
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        # check if the data is valid
        if serializer.is_valid():
            # save the data
            serializer.save()
            # return the JsonResponse and created status 201
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if not valid return error status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# same as articleDetail (function based view)
class ArticleDetailView(APIView):
    # select the objects
    def get_object(self, pk):
        try:
            return Article.objects.get(id=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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
