from django.urls import path
from . import views
from article.views import article_detail,article_list

urlpatterns = [
#localhost:8000/admin
    path('<int:article_id>',article_detail,name='article_detail'),
    path('',article_list,name='article_list'),
]
