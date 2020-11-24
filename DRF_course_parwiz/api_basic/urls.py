from django.urls import path
from . import views

urlpatterns = [
    path('function_based', views.articleList, name='article_list_function_based'),
    path('function_based/article/<str:pk>/', views.articleDetatil, name='article_detail'),

    path('class_based', views.ArticleAPIView.as_view(), name='article_list_class_based'),
    path('class_based/article/<str:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),

    path('generic_class_based', views.GenericAPIView.as_view(), name='article_list_generic_class_based'),
    path('generic_class_based/article/<str:pk>/', views.GenericAPIDetailView.as_view(), name='article_detail_generic_class_based'),
]
