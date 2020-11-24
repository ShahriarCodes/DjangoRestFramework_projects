from django.urls import path
from . import views

urlpatterns = [
    # path('', views.articleList, name='article_list'),
    # path('article/<str:pk>/', views.articleDetatil, name='article_detail'),
    path('', views.ArticleAPIView.as_view(), name='article_list'),
    path('article/<str:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
