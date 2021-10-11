from django.urls import path
from .views import ArticleAPIView, ArticleDetailAPIView, MyGenericAPIView

urlpatterns = [

    # FUnction base views and urls

    # path('article', article_list),
    # path('article/detail/<int:pk>', article_detail)

    # Class base views and urls

    # path('article/', ArticleAPIView.as_view()),
    # path('article/detail/<int:id>', ArticleDetailAPIView.as_view()),

    # Generic and Mixins base views
    path('generic/article/', MyGenericAPIView.as_view()),
    path('generic/article/<int:id>/', MyGenericAPIView.as_view())
]
